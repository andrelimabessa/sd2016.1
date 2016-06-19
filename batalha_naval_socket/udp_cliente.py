# -*- coding: utf-8 -*-

import socket
from datetime import datetime
import menus

ENCODE = "UTF-8"
HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000          # Porta que o Servidor esta
MAX_BYTES = 65535

def client(text):

    while True:

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dest = (HOST, PORT)

        options = text.split(',')
        action = options[0]

        if action == '__start_game__':
            text = menus.opening_game()
        elif action == '__try__':
            columns = str(input("LINHAS:  \n"))
            rows = str(input("COLUNAS: \n"))

            text = '__jogada__,__try__,' + columns + ',' + rows
        elif action == '__actions_game__':
            action1 = options[1]

            if action1 == 'print':
                print options[2]
            elif action1 == 'visualizar':
                visualizar(options[2], options[3], options[4], options[5])
            text = '__jogada__,' + menus.actions_game()
        else:
            text = menus.menu_inicial()

        enviar_text(text, sock, dest)

        text = received_response_from_server(sock)
def enviar_text(text, sock, dest):
    data = str(text).encode(ENCODE)
    sock.sendto(data, dest)

def received_response_from_server(sock):
    data, address = sock.recvfrom(MAX_BYTES)  # Danger! See Chapter 2
    text = data.decode(ENCODE)

    return text

def visualizar(rows, columns, acertos, restantes):
    print("\n")
    print("### Tabuleiro:")
    print("LINHAS: %i" % int(rows))
    print("COLUNAS: %i" % int(columns))
    print("\n")
    print("### PONTUAÇÃO: ")
    print("ACERTOS: %i" % int(acertos))
    print("RESTANTE: %i" % int(restantes))
    print("\n")