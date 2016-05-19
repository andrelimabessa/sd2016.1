import socket

import ast

from datetime import datetime

from protocolo_servidor import ProtocoloServidor

ENCODE = "utf-8"
MAX_BYTES = 65535
PORT = 5000#Porta do SErvidor
HOST = ''#endereco do servidor

protocolo_servidor = ProtocoloServidor
jogo = {}
jogo["jogo1"] = {}
jogo["jogo1"]["qtd_colunas"] = 0
jogo["jogo1"]["qtd_linhas"] = 0
jogo["jogo1"]["tabuleiro"] = []

def server():
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)

    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        requisicao_cliente = ast.literal_eval(data.decode(ENCODE))
        resposta_tratamento = tratar_requisicao(requisicao_cliente)

        if resposta_tratamento == "criar_tabuleiro":
            requisicao_cliente["criar_tabuleiro"] = 1
            print("Solicitando dados de tabuleiro.")
            resposta_requisicao = str(requisicao_cliente)
        data = resposta_requisicao.encode(ENCODE)
        sock.sendto(data, address)
    sock.close()

def tratar_requisicao(requisicao):
  if int(requisicao["comeco_interacao"]) == 1:
      if int(requisicao["novo_jogo"]) == 1:
        if int(requisicao["criar_tabuleiro"]) == 0:
          resposta_requisicao = "criar_tabuleiro"
          return resposta_requisicao
      elif int(requisicao["novo_jogo"]) == 2:
        if int(requisicao["criar_tabuleiro"]) == 1:
          protocolo_servidor.criar_tabuleiro(jogo)