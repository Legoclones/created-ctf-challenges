import socket
from hashlib import sha256
from datetime import datetime

UDP_IP = "0.0.0.0"
UDP_PORT = 40000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

messages = {}

while True:
    # get data from client
    data, addr = sock.recvfrom(1024) # max message size is 1024 bytes, any message longer will have extra bytes ignored
    id = sha256(str(addr).encode()).hexdigest()
    print(id, addr, data)

    # delete long messages
    for key in list(messages):
        if (len(messages[key]) > 8000) or (datetime.now() - messages[key][1]).total_seconds() > 10:
            del messages[key]

    # add data to messages
    if id not in messages:
        messages[id] = [data, datetime.now()]
    else:
        messages[id][0] += data

    # check to see if full HTTP request has been received
    if "\r\n\r\n" in messages[id][0].decode():
        print("Full HTTP request received!")

        # forward HTTP request to flask server
        httpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        httpsock.connect(("127.0.0.1", 1337))
        httpsock.sendall(messages[id][0])
        response = httpsock.recv(10000)
        httpsock.close()

        print(response)

        # send response to client and delete message
        sock.sendto(response, (addr[0], addr[1]))
        del messages[id]

    print(messages)