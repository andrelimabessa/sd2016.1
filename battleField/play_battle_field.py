import random
import ast

def starting_game():
	print("O que deseja fazer?")
	print("1 - Ver estado do jogo.")
	print("2 - Continuar jogo anterior.")
	print("3 - Começar novo jogo.")

	acao = input("Ação: ")

	try:
		if int(acao) == 1:
			print("Você escolheu: Ver estado do jogo")
			return 1
		elif int(acao) == 2:
			print("Você escolheu: Continuar jogo anterior.")
			return 2
		elif int(acao) == 3:
			print("Você escolheu: Começar novo jogo.")
			return 3
		else:
			raise Exception
	except :
		print("Precisa escolher uma opção válida.\n\n")
		starting_game()

#starting_game()
