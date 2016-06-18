import socket
from datetime import datetime
from Helper.GameManager import GameManager

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000
HOST = ''
def server():
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)
    connec1 = 0
    connec2 = 0
    keepAlive = True
    while keepAlive:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode(ENCODE)
        if connec1 == 0:
            gm = GameManager()
            connec1 = address
            gm.turn("setPlayer", address)
        elif connec2 == 0:
            connec2 = address
            gm.turn("setPlayer", address)
        if (address != connec1) or (address != connec2):
            text = "Jogo está cheio, aguarde a proxima jogada"
        print(connec1);
        print(connec2);
        text = "Your data was " + str(len(data)) + " bytes long"
        data = text.encode(ENCODE)
        sock.sendto(data, address)
    sock.close()
