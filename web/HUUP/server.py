# imports
from flask import Flask


# initialize flask
app = Flask(__name__)
FLAG = open('flag.txt', 'r').read()


# main page
@app.route('/', methods=['GET'])
def main():
    return f"Unfortunately, I had much more planned for this, but it was already so hard to get ANY content body returned, so I'll just give you the flag I guess (yes, it's supposed to take dozens of requests to get the flag). {FLAG}"
    #return "Congrats on making it here! But you'll have to work a little more to get the flag. :)<br><br>A list of possible endpoints can be found <a href='/endpoints.txt'>here</a>. Use that to find the flag!"

# list of possible endpoints
@app.route('/endpoints.txt', methods=['GET'])
def endpoints():
    return open("endpoints.txt", "r").read()

# fake endpoint
@app.route('/2D8264CBAC0F22C57EBAB31B2D149B29', methods=['GET'])
def fake1():
    return "Haha nope, that is not the flag. Keep trying!"

# fake endpoint
@app.route('/8C340AACC359745D078DAC2C1A54C4A8', methods=['GET'])
def fake2():
    return "Wait, what? That's not the flag. Try again!"

# fake endpoint
@app.route('/B9FB45DE2122E9726E8D82328F0CA0C5', methods=['GET'])
def fake3():
    return "STRIKE!"

# flag endpoint
@app.route('/52791158BA3797F345C202E3D92C6735', methods=['GET'])
def flag():
    return "Okay, I guess you can have the flag.... " + FLAG


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1337, threaded=True)