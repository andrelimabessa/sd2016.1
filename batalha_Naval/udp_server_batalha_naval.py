import socket

from datetime import datetime

ENCODE = "utf-8"
MAX_BYTES = 65535
PORT = 5000#Porta do SErvidor
HOST = ''#endereço do servidor

def server():
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)

    while True:
        data, address = sock.recvfrom(MAX_BYTES)

        text = data.decode(ENCODE)
        print(text)

        text = "Recebi o novo formato de solicitação!"
        data = text.encode(ENCODE)
        sock.sendto(data, address)
    sock.close()