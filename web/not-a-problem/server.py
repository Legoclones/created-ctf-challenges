# imports
from flask import Flask, request
import uuid, subprocess


# initialize flask
app = Flask(__name__)
SECRET = open("secret.txt", "r").read()
stats = []


# index
@app.route('/', methods=['GET'])
def main():
    return 'Bro did you really think I care about the front end enough to make one?'


# get stats
@app.route('/api/stats/<string:id>', methods=['GET'])
def get_stats(id):
    for stat in stats:
        if stat['id'] == id:
            return str(stat['data'])
        
    return '{"error": "Not found"}'


# add stats
@app.route('/api/stats', methods=['POST'])
def add_stats():
    try:
        username = request.json['username']
        high_score = int(request.json['high_score'])
    except:
        return '{"error": "Invalid request"}'
    
    id = str(uuid.uuid4())

    stats.append({
        'id': id,
        'data': [username, high_score]
    })
    return '{"success": "Added", "id": "'+id+'"}'


# current date
@app.route('/api/date', methods=['GET'])
def get_date():
    # get "secret" cookie
    cookie = request.cookies.get('secret')

    # check if cookie exists
    if cookie == None:
        return '{"error": "Unauthorized"}'
    
    # check if cookie is valid
    if cookie != SECRET:
        return '{"error": "Unauthorized"}'
    
    modifier = request.args.get('modifier','')
    
    return '{"date": "'+subprocess.getoutput("date "+modifier)+'"}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1337, threaded=True)