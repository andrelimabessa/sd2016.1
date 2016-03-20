import socket

from play_battle_field import game

from datetime import datetime

import ast

ENCODE = "UTF-8"
HOST = '127.0.0.1'#'10.54.42.50'#
PORT = 5000
MAX_BYTES = 65535

game = game()

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
				text = acao
			else:
				#print(acao)
				acao = game.starting_game()
				text = acao
		#print(game.starting_game())
		#text = input("Digite algum comando:\n")
		conversa(text, dest, sock)

def oonversa(self, text, dest, sock)
	data = text.encode(ENCODE)
	sock.sendto(data, dest)
	print(sock.getsockname())
	data, address = sock.recvfrom(MAX_BYTES)
	#text = ast.literal_eval(data.decode(ENCODE))
	text = data.decode(ENCODE)

	#if int(acao) == 2 and int(text) == 1:
	#	resposta = game.continuar_jogo()
	print(repr(text))
	#print(address, text)