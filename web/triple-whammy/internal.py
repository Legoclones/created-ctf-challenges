# imports
from flask import Flask, request
import pickle, random


# initialize flask
app = Flask(__name__)
port = random.randint(5700, 6000)
print(port)


# index
@app.route('/pickle', methods=['GET'])
def main():
    pickle_bytes = request.args.get('pickle')

    if pickle_bytes is None:
        return 'No pickle bytes'
    
    try:
        b = bytes.fromhex(pickle_bytes)
    except:
        return 'Invalid hex'
    
    try:
        data = pickle.loads(b)
    except:
        return 'Invalid pickle'

    return str(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, threaded=True)