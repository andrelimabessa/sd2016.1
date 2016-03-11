import socket
from play_battle_field import game
from datetime import datetime

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
		#while option:
		acao = game.starting_game()
		if acao == 1:
			print(acao)
			option = False#break
		elif acao ==2:
			print(acao)
			option = False#break
		elif acao ==3:
			print(acao)
			option = False#break
		else:
			print(acao)
		#print(game.starting_game())
		text = input("Digite algum comando:\n")
		data = text.encode(ENCODE)
		sock.sendto(data, dest)
		print(sock.getsockname())
		data, address = sock.recvfrom(MAX_BYTES)
		text = data.decode(ENCODE)
		print(address, text)
