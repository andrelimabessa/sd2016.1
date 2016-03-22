# -*- coding: utf-8 -*-

import socket
from datetime import datetime

ENCODE = "UTF-8"
HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000          # Porta que o Servidor esta
MAX_BYTES = 65535

def client():
    #Enviod de dados
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (HOST, PORT)
    text = input("Digite algum comando:\n")

    print("1 - Iniciar jogo")
    if (text == 1):
        sock.sendto('START_GAME', dest)

    # data = text.encode(ENCODE)
    # sock.sendto(data, dest)

    #Resposta de envio ao servidor

    print(sock.getsockname())
    data, address = sock.recvfrom(MAX_BYTES)  # Danger! See Chapter 2
    text = data.decode(ENCODE)
    print(address, text)
