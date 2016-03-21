import socket

from play_battle_field import game

from datetime import datetime

import ast

ENCODE = "UTF-8"
HOST = '127.0.0.1'#'10.54.42.50'#
PORT = 5000
MAX_BYTES = 65535

game = game()
jogo = {}

def client():
	while True:
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		dest = (HOST, PORT)

		option = True
		while option:
			acao = game.starting_game()
			if int(acao) == 1:
				#print(acao)
				option = False#break
				text = acao
			elif int(acao) == 2:
				#print(acao)
				option = False#break
				text = acao
			elif int(acao) == 3:
				option = False#break
				text = str(acao) + ";1"
			else:
				#print(acao)
				acao = game.starting_game()
				text = acao
		conversa(acao,text, dest, sock)

def conversa(acao,text, dest, sock):
	data = text.encode(ENCODE)
	sock.sendto(data, dest)
	#print(sock.getsockname())
	data, address = sock.recvfrom(MAX_BYTES)
	#text = ast.literal_eval(data.decode(ENCODE))
	text = data.decode(ENCODE)
	resposta = tratar_requisicoes(acao,text, dest, sock)

def tratar_requisicoes(acao,text, dest, sock):
	if int(acao) == 2:
		if int(text) == 1:
			resposta = game.continuar_jogo()
			print(resposta)
		elif int(text) == 2:
			resposta = game.jogadas_esgotadas()
			print(resposta)
	elif int(acao) == 3:
		resposta = text[0]
		if int(resposta) == 1:
			print(text[4::])
			text = str(acao) + ";2;"# + str(envio_dados_do_jogo())

def envio_dados_do_jogo():
	jogo["jogador"] = input("Nome do Jogador: ")
	jogo["linhas"] = input("Quantas Linhas: ")
	jogo["colunas"] = input("Quantas Colunas: ")
	jogo["navios"] = input["Quantos Navios: "]
	return(repr(jogo))