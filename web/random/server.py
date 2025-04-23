# imports
from flask import Flask, abort, request, make_response, Response
import hashlib, time, jwt, os


# initialize flask
app = Flask(__name__)
time_started = round(time.time())
APP_SECRET = hashlib.sha256(str(time_started).encode()).hexdigest()


# check authorization before request handling
@app.before_request
def check_auth():
    # ensure user is an administrator
    session = request.cookies.get('session', None)

    if session is None:
        abort(403)

    try:
        payload = jwt.decode(session, APP_SECRET, algorithms=['HS256'])
        if payload['userid'] != 0:
            abort(401)
    except:
        abort(Response(f'<h1>NOT AUTHORIZED</h1><br><br><br><br><br> This system has been up for {round(time.time()-time_started)} seconds fyi :wink:', status=403))


# list files
@app.route('/api/files', methods=['GET'])
def list_files():
    return os.listdir('files/')


# get a file
@app.route('/api/file', methods=['GET'])
def get_file():
    filename = request.args.get('filename', None)

    if filename is None:
        abort(Response('No filename provided', status=400))

    # prevent directory traversal
    while '../' in filename:
        filename = filename.replace('../', '')

    # get file contents
    return open(os.path.join('files/', filename),'rb').read()



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1337, threaded=True)