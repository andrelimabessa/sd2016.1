import socket
from datetime import datetime
from jogo import BatalhaNaval

import ast
ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000            # Porta que o Servidor esta
HOST = ''     # Endereco IP do Servidor

def server():
    #Abrindo uma porta UDP
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)
    while True:
        #recebi dados
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode(ENCODE)
        map = ast.literal_eval(text)
        text = map["opcao"]

        if text == "1":
            jogo = BatalhaNaval(map["tamanho_tabuleiro"])
            if map["inserir_navios"] == "S":
                jogo.insereNavios()
                resp = "Tabuleiro criado com sucesso e navios inseridos!!!!"
            else:
                resp = "Tabuleiro criado com sucesso!!!"
        elif text == "2":
            resp = "Opção 2"
        elif text == "3":
            resp = jogo.jogada(map["posX"], map["posY"])
        elif text == "4":
            jogo.imprimeTabuleiro()
            resp = "Tabuleiro impresso!!"
        else:
            resp = "Opção Inválida!"
        #print(address, text)
        #Envia resposta
        #text = "Your data was " + str(len(data)) + " bytes long"
        data = resp.encode(ENCODE)
        sock.sendto(data, address)
    sock.close()
