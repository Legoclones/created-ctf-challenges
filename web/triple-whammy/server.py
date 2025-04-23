# imports
from flask import Flask, request
from urllib.parse import urlparse
import requests


# initialize flask
app = Flask(__name__)
SECRET = open("secret.txt", "r").read()


# index
@app.route('/', methods=['GET'])
def main():
    name = request.args.get('name','')

    return 'Nope still no front end, front end is for noobs '+name


# query
@app.route('/query', methods=['POST'])
def query():
    # get "secret" cookie
    cookie = request.cookies.get('secret')

    # check if cookie exists
    if cookie == None:
        return {"error": "Unauthorized"}
    
    # check if cookie is valid
    if cookie != SECRET:
        return {"error": "Unauthorized"}
    
    # get URL
    try:
        url = request.json['url']
    except:
        return {"error": "No URL provided"}

    # check if URL exists
    if url == None:
        return {"error": "No URL provided"}
    
    # check if URL is valid
    try:
        url_parsed = urlparse(url)
        if url_parsed.scheme not in ['http', 'https'] or url_parsed.hostname != '127.0.0.1':
            return {"error": "Invalid URL"}
    except:
        return {"error": "Invalid URL"}
    
    # request URL
    try:
        requests.get(url)
    except:
        return {"error": "Invalid URL"}
    
    return {"success": "Requested"}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1337, threaded=True)