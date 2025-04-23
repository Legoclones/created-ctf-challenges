# imports
from flask import Flask, g, render_template, request, redirect, make_response, send_file, after_this_request
import uuid, os


# initialize flask
app = Flask(__name__)


# ensure each user has a uuid session
@app.before_request
def check_uuid():
    uuid_cookie = request.cookies.get('uuid', None)

    # ensure user has uuid_cookie
    if uuid_cookie is None:
        response = make_response(redirect('/'))
        response.set_cookie('uuid', str(uuid.uuid4()))
        return response
    
    # ensure uuid_cookie is valid UUID
    try:
        uuid.UUID(uuid_cookie)
    except ValueError:
        response = make_response(redirect('/'))
        response.set_cookie('uuid', str(uuid.uuid4()))
        return response
    
    g.uuid = uuid_cookie

    if not os.path.exists(f'uploads/{g.uuid}'):
        os.mkdir(f'uploads/{g.uuid}')


# main dashboard
@app.route('/', methods=['GET'])
def main():
    return render_template('index.html', files=os.listdir(f'uploads/{g.uuid}'))
    

# upload file
@app.route('/api/upload', methods=['POST'])
def upload():
    file = request.files.get('file', None)
    if file is None:
        return 'No file provided', 400
    
    # check for path traversal
    if '..' in file.filename or '/' in file.filename:
        return 'Invalid file name', 400
    
    # check file size
    if len(file.read()) > 1000:
        return 'File too large', 400
    
    file.save(f'uploads/{g.uuid}/{file.filename}')
    return 'Success! <script>setTimeout(function() {window.location="/"}, 3000)</script>', 200


# download file
@app.route('/api/download', methods=['GET'])
def download():
    @after_this_request
    def remove_file(response):
        os.system(f"rm -rf uploads/{g.uuid}/out.tar")
        return response

    # make a tar of all files
    os.system(f"cd uploads/{g.uuid}/ && tar -cf out.tar *")

    # send tar to user
    return send_file(f"uploads/{g.uuid}/out.tar", as_attachment=True, download_name='download.tar', mimetype='application/octet-stream')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1337, threaded=True)