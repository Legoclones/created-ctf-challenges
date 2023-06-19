import socket

UDP_IP = "byuctf.xyz"
UDP_PORT = 40011
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send(path=b"/"):
    data = b"\r\n\r\n"
    while data.endswith(b"\r\n\r\n"):
        sock.sendto(b"GET "+path+b" HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n", (UDP_IP, UDP_PORT))
        data,addr = sock.recvfrom(7000)
        print(data)

    return data

print(send(b"/"))