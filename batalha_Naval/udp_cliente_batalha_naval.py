import socket

from datetime import datetime

from protocolo_cliente import ProtocoloCliente

ENCODE = "UTF-8"
HOST = '127.0.0.1'
PORT = 5000
MAX_BYTES = 65535

interacao = {}
interacao["comeco_interacao"] = 0
interacao["novo_jogo"] = 0
interacao["criar_tabuleiro"] = 0
interacao["distribui_navios"] = 0
interacao["realizar_jogada"] = 0
interacao["ver_jogo"] = 0
interacao["continuar_jogo"] = 0

protocolo_cliente = ProtocoloCliente()

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (HOST, PORT)
    while True:
        if interacao["comeco_interacao"] == 0:
          print("Comecando nova conexao...")
          protocolo_cliente.comeco_interacao(interacao)
          if interacao["novo_jogo"] == 1:
            print("estou entrando nesse if mas nao devia")
            print(envio_de_dados(interacao, sock, dest))
        elif interacao["comeco_interacao"] == 1:
          print("Estou no segundo if!!!!")
          print(interacao)
          input()

def envio_de_dados(interacao, sock, dest):
    if interacao["comeco_interacao"] == 1:
        if interacao["novo_jogo"] == 1:
            requisicao_servidor = str(interacao).encode(ENCODE)
            sock.sendto(requisicao_servidor, dest)
            resposta_servidor, address = sock.recvfrom(MAX_BYTES)
            resposta_requisicao = resposta_servidor.decode(ENCODE)
            return resposta_requisicao