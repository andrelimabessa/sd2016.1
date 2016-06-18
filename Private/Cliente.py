import socket
from datetime import datetime

ENCODE = "UTF-8"
HOST = '127.0.0.1'
PORT = 5000
MAX_BYTES = 65535

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (HOST, PORT)
    lastResp = ''
    while True:
        lastResp = input("Digite algum comando:\n")
        data = lastResp.encode(ENCODE)
        sock.sendto(data, dest)
        data, address = sock.recvfrom(MAX_BYTES)
        lastResp = data.decode(ENCODE)
        print(address, lastResp)
