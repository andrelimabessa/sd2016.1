# -*- coding: utf-8 -*-

import socket
from datetime import datetime
import arquivo
from jogo import Jogo

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000
HOST = ''
JOGO = None

def server():
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode(ENCODE)

        print(address, text)

        text = tratar_requisicao(text)
        print "Your data was " + str(len(data)) + " bytes long"

        data = text.encode(ENCODE)
        sock.sendto(data, address)
    sock.close()

def tratar_requisicao(text):
    options = text.split(',')
    action = options[0]

    msg = ''

    if action == "1":
        arquivo.delete(arquivo.CONST_PATH_FILE)
        return '__start_game__'
    elif action == '__jogada__':
        global JOGO

        option = options[1]

        if option == '1':
            msg = 'print,'+JOGO.tabuleiro.distribuir_navios()
        elif option == '__try__':
            row = options[2]
            column = options[3]

            msg = 'print,'+JOGO.realizar_jogada(row, column)
        elif option == '2':
            return '__try__'
        elif option == '3':
            msg = 'visualizar' + ',' + JOGO.visualizar()
        elif option == '4':
            JOGO.salvar_jogo()

        return '__actions_game__,' + msg
    elif action == '__create_player__':
        global JOGO
        JOGO = Jogo(options[1], options[2], options[3])

        return '__actions_game__,' + msg