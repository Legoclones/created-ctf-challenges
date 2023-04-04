from flask import Flask, request
from flag import FLAG

app = Flask(__name__)

@app.route('/')
def index():
    page = "Wrong."
    useragent = request.headers.get('User-Agent', "Bad")
    if useragent == "Lorem ipsum":
        page = FLAG
    return page

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=40003)