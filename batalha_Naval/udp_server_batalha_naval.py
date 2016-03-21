import socket

import ast

from datetime import datetime

from protocolo_servidor import ProtocoloServidor

ENCODE = "utf-8"
MAX_BYTES = 65535
PORT = 5000#Porta do SErvidor
HOST = ''#endereço do servidor

protocolo_servidor = ProtocoloServidor

def server():
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)

    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        requisicao_cliente = data.decode(ENCODE)

        protocolo = tratar_requisicao(requisicao_cliente)

        protocolo_servidor.tratar_requisicao(protocolo)

        print(type(requisicao_cliente))

        print(text)

        text = "Recebi o novo formato de solicitação!"
        data = text.encode(ENCODE)
        sock.sendto(data, address)
    sock.close()

def tratar_requisicao(requisicao):
    requisicao = ast.literal_eval(requisicao)
    if int(requisicao["comeco_interacao"]) == 1:
        if int(requisicao["novo_jogo"]) == 1:
            if int(requisicao["requisicao"]) == 1:
                resposta_requisicao_servidor = "criar_tabuleiro"
                return resposta_requisicao_servidor