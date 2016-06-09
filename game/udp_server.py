# -*- coding: utf-8 -*-

import socket
from datetime import datetime

from tabuleiro import Tabuleiro

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000            # Porta que o Servidor esta
HOST = '127.0.0.1'     # Endereco IP do Servidor

def server():
    #Abrindo uma porta UDP
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)

    arq = open("shots.txt", "r")
    shots = int(arq.readline())
    arq.close()
    while True:
        #recebi dados
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode(ENCODE)
        
        # print(address, text)

        if (text == 'START_GAME'):
            data = text.encode(ENCODE)

            tabuleiro = Tabuleiro(5)
            tabuleiro.preencher(5, 3)
            print('### Jogo Criado ####')
            sock.sendto('JOGUE'.encode('utf-8'), address)
        if (text == 'SAIR'):
            sock.sendto('QUIT'.encode('utf-8'), address)
        else:
            message = text.split(',')
            print(shots)
            if (shots>5):
                sock.sendto('ACABOU'.encode('utf-8'), address)   
                arq = open("shots.txt", "w")
                arq.write("0")
                arq.close()                                   
            if (message[0] == 'RESPOSTA'):
                shots =shots+1
                arq = open("shots.txt", "w")
                arq.write(str(shots))
                arq.close()                
                x = message[1]
                y = message[2]

                resposta = tabuleiro.jogar(x, y)
                if (resposta):
                    print('Acertou')
                    sock.sendto('A'.encode('utf-8'), address)
                    sock.sendto('JOGUE'.encode('utf-8'), address)
                else:
                    print('Errou')
                    sock.sendto('E'.encode('utf-8'), address)
                    sock.sendto('JOGUE'.encode('utf-8'), address)


    sock.close()
