### IMPORTS ###
from flask import Flask, request, make_response
from webauthn import (
    generate_registration_options, 
    verify_registration_response, 
    base64url_to_bytes, 
    generate_authentication_options,
    verify_authentication_response,
)
from webauthn.helpers import options_to_json
from webauthn.helpers.structs import PublicKeyCredentialDescriptor
from webauthn.helpers.exceptions import InvalidAuthenticationResponse
import json, secrets, os


### INITIALIZATIONS ###
app = Flask(__name__)
FLAG1 = open('flag1.txt', 'r').read()
FLAG2 = open('flag2.txt', 'r').read()
RP = os.environ.get('RP', 'localhost')
ORIGIN = os.environ.get('ORIGIN', f'http://{RP}:1337')
users = {}
credentials = {}



### HELPER FUNCTIONS ###
def db_init():
    global users, credentials # super sophisticated database

    # admin user
    admin_cred_id = secrets.token_hex(16)
    users['admin'] = admin_cred_id
    credentials[admin_cred_id] = {
        'pubkey': 'a50102032620012158204fc8eaf4491b71e6c0a774d27335af49b028c64beeee9231a70823cf6d2493692258200b95e479141655cb2ea1cf6892931c15e722552460f1e5a32587e51be5b98dcd',
        'sign': 0,
        'backed_up': False,
        'transports': 'usb'
    }

def handle_webauthn_reg(reg: dict) -> tuple[int, dict]:
    try:
        verified = verify_registration_response(
            credential=reg,
            expected_challenge=base64url_to_bytes(json.loads(base64url_to_bytes(reg['response']['clientDataJSON']))['challenge']),
            expected_rp_id=RP,
            expected_origin=ORIGIN,
            require_user_verification=True,
        )
        if not verified:
            return (-1, {})

        to_store_data = {
            'cred_id': verified.credential_id.hex(),
            'pubkey': verified.credential_public_key.hex(),
            'sign': verified.sign_count,
            'backed_up': verified.credential_backed_up,
            'transports': str(reg["response"]["transports"][0])
        }

        return (0, to_store_data)
    except Exception as e:
        return (-2, {})

def handle_webauthn_auth(auth: dict, username: str) -> tuple[int, dict]:
    global users, credentials

    try:
        cred = credentials[users[username]]

        verification = verify_authentication_response(
            credential=auth,
            expected_challenge=base64url_to_bytes(json.loads(base64url_to_bytes(auth['response']['clientDataJSON']))['challenge']),
            expected_rp_id=RP,
            expected_origin=ORIGIN,
            credential_public_key=bytes.fromhex(cred['pubkey']),
            credential_current_sign_count=cred['sign'],
            require_user_verification=True,
        )

        to_update_data = {
            'cred_id': verification.credential_id.hex(),
            'sign': verification.new_sign_count,
            'backed_up': verification.credential_backed_up,
        }
        return (0, to_update_data)

    except InvalidAuthenticationResponse as e:
        # thrown if bad signature or sign count
        return (-1, {})

    except Exception as e:
        return (-2, {})

def save_data(data: dict):
    global users, credentials

    users[data['username']] = data['cred_id']
    credentials[data['cred_id']] = {
        'pubkey': data['pubkey'],
        'sign': data['sign'],
        'backed_up': data['backed_up'],
        'transports': data['transports']
    }

def update_data(data: dict):
    global users, credentials

    credentials[data['cred_id']]['sign'] = data['sign']
    credentials[data['cred_id']]['backed_up'] = data['backed_up']



### ENDPOINTS ###
@app.route('/api/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        opts = generate_registration_options(
            rp_id=RP,
            rp_name="Hackers Challenge: WebAuthn",
            user_name=secrets.token_hex(16),
        )

        resp = make_response(options_to_json(opts))
        resp.mimetype = 'application/json'
        return resp

    elif request.method == 'POST':
        # parse data
        data = request.get_json()
        if not data:
            return make_response("Invalid request", 400)

        # ensure required fields are present
        if not all(key in data for key in ['username', 'reg']):
            return make_response("Missing fields", 400)

        # extract username and registration data
        username = data['username']
        reg = data['reg']

        # ensure username is a string
        if not isinstance(username, str):
            return make_response("Invalid username", 400)

        # retrieve webauthn data to store
        status, to_store_data = handle_webauthn_reg(reg)
        if status == -1:
            return make_response("Registration failed", 400)
        elif status == -2:
            return make_response("Error during verification", 500)

        to_store_data['username'] = username

        # ensure username and ID are unique
        if username in users or base64url_to_bytes(reg['id']).hex() in credentials:
            return make_response("Username or ID already exists", 400)

        # store the data
        save_data(to_store_data)

        return make_response("Registration successful", 200)


@app.route('/api/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # optional username parameter
        username = request.args.get('username')

        # get allowed credentials for the user
        if username != None and username in users:
            creds = [PublicKeyCredentialDescriptor(id=bytes.fromhex(users[username]))]
        else:
            creds = []

        opts = generate_authentication_options(
            rp_id=RP,
            allow_credentials=creds,
        )

        resp = make_response(options_to_json(opts))
        resp.mimetype = 'application/json'
        return resp

    elif request.method == 'POST':
        # get data
        data = request.get_json()
        if not data:
            return make_response("Invalid request", 400)

        # ensure required fields are present
        if 'auth' not in data:
            return make_response("Missing fields", 400)

        # extract username and authentication data
        auth = data['auth']
        username = base64url_to_bytes(auth['response']['userHandle']).decode()

        # check if user exists
        if username not in users:
            return make_response("Unauthorized", 401)

        # check credentials
        status, to_update_data = handle_webauthn_auth(auth, username)
        if status == -1:
            return make_response("Unauthorized", 401)
        elif status == -2:
            return make_response("Error during authentication", 500)

        # update the data
        update_data(to_update_data)

        if username == 'admin':
            msg = f"Login successful! Here is flag 2: {FLAG2}"
        else:
            msg = f"Login successful! Here is flag 1: {FLAG1}"

        return make_response(msg, 200)



if __name__ == "__main__":
    db_init()
    app.run(host='0.0.0.0', port=1337, threaded=True)