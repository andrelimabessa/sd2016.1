import socket

from datetime import datetime

from protocolo_cliente import ProtocoloCliente

ENCODE = "UTF-8"
HOST = '127.0.0.1'
PORT = 5000
MAX_BYTES = 65535

interacao = {}
interacao["comeco_interacao"] = 0

protocolo_cliente = ProtocoloCliente()

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (HOST, PORT)

    while True:
        if interacao["comeco_interacao"] == 0:
            requisicao = protocolo_cliente.comeco_interacao()
            print(requisicao)
            resposta = input("Digite sua opção: ")

            interacao["novo_jogo"] = int(resposta)
            interacao["comeco_interacao"] = 1

            server_answer = envio_de_dados(interacao["comeco_interacao"], interacao["novo_jogo"], resposta, sock, dest)

            print(server_answer)

        #text = requisicao
        #data = text.encode(ENCODE)
        #sock.sendto(data, dest)
        #data, address = sock.recvfrom(MAX_BYTES)

        #text = data.decode(ENCODE)
        #print(text)

def envio_de_dados(comeco_interacao, novo_jogo, resposta, sock, dest):
    if comeco_interacao == 1:
        if novo_jogo == 1:
            interacao["requisicao"] = resposta
            requisicao_servidor = str(interacao).encode(ENCODE)
            sock.sendto(requisicao_servidor, dest)

            resposta_servidor, address = sock.recvfrom(MAX_BYTES)
            resposta_requisicao = resposta_servidor.decode(ENCODE)

            return resposta_requisicao