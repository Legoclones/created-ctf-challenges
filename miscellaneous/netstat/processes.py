import random, secrets

ports = random.sample(range(10000, 60001), 99)

for port in ports:
    script = f"""import socket
HOST = '127.0.0.1'
PORT = {port}
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
while True:
    pass"""

    with open('/scripts/' + secrets.token_hex(16) + '.py', 'w') as f:
        f.write(script)

script = """import socket
HOST = '127.0.0.1'
PORT = 9876 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
while True:
    pass"""

with open('/scripts/5065fc12633a9f1fd28f0b9d27467537.py', 'w') as f:
        f.write(script)