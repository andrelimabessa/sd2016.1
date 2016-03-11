import random
import ast

class game(object):

	def starting_game(self):
		print("O que deseja fazer?")
		print("1 - Ver estado do jogo.")
		print("2 - Continuar jogo anterior.")
		print("3 - Começar novo jogo.")

		acao = input("Ação: ")

		#try:
		if int(acao) == 1:
			print("Você escolheu: Ver estado do jogo")
			print(acao)
			return acao
		elif int(acao) == 2:
			print("Você escolheu: Continuar jogo anterior.")
			print(acao)
			return acao
		elif int(acao) == 3:
			print("Você escolheu: Começar novo jogo.")
			print(acao)
			return acao
		else:
			print("Precisa escolher uma opção válida.\n\n")
			#return starting_game()
		#except :
		#	print("Precisa escolher uma opção válida.\n\n")
		#	starting_game()

#starting_game()
