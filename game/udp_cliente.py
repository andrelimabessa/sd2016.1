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

    print("1 - Iniciar jogo")

    text = input("Digite algum comando:\n")
    print(text)
    if (text == "1"):
        sock.sendto('START_GAME'.encode(ENCODE), dest)
    # data = text.encode(ENCODE)
    # sock.sendto(data, dest)

    #Resposta de envio ao servidor
    while True:
        data, address = sock.recvfrom(MAX_BYTES)  # Danger! See Chapter 2
        text = data.decode(ENCODE)

        if (text == 'JOGUE'):
            print("Informe as coordenadas no tabuleiro")
            x = input("X: ")
            y = input("Y: ")
            message = 'RESPOSTA,' + str(x) + ',' + str(y)
            sock.sendto(message.encode(ENCODE), dest)
        if (text == 'A'):
            print("Acertou")
        if (text == 'E'):     
            print("Errou")
      