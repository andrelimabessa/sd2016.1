# -*- coding: utf-8 -*-

import socket
from datetime import datetime
from mercurial.templatefilters import tabindent

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

            sock.sendto('JOGUE', address)
        else:
            message = text.split(',')
            if (message[0] == 'RESPOSTA'):
                x = message[1]
                y = message[2]

                resposta = tabuleiro.jogar(x, y)
                if (resposta):
                    print('Acertou')
                else:
                    print('Erro')


    sock.close()
