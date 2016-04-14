import random
import ast

class game(object):

	def starting_game(self):
		print("O que deseja fazer?")
		print("1 - Ver estado do jogo.")
		print("2 - Continuar jogo anterior.")
		print("3 - Comecar novo jogo.")

		acao = input("Acao: ")

		#try:
		if int(acao) == 1:
			print("Voce escolheu: Ver estado do jogo")
			#print("classe game")
			return acao
		elif int(acao) == 2:
			print("Voce escolheu: Continuar jogo anterior.")
			#print(acao)
			return acao
		elif int(acao) == 3:
			print("Voce escolheu: Comecar novo jogo.")
			#print(acao)
			return acao
		else:
			print("Precisa escolher uma opcao valida.\n\n")
			return acao
		#except :
		#	print("Precisa escolher uma opcao valida.\n\n")
		#	starting_game()

	def continuar_jogo(self):
		self.arq = open("memory_card_battle_field.txt","r")
		self.memory_card = ast.literal_eval(self.arq.readline())
		self.arq.close()

		self.tabuleiro = self.memory_card["tabuleiro"]
		self.jogadas = self.memory_card["jogadas"]
		self.acertos = self.memory_card["acertos"]


		print("Você tem %d acertos e ainda possui %d jogadas."%(self.acertos, self.jogadas))
		self.linha = input("Diga a linha que deseja: ")
		self.coluna = input("Diga a coluna que deseja: ")
		self.jogada = game.jogar(self,int(self.linha), int(self.coluna), self.tabuleiro)

		if self.jogada == "agua":
			self.arq = open("memory_card_battle_field.txt","r")
			self.memory_card = ast.literal_eval(self.arq.readline())
			self.arq.close()

			self.memory_card["jogadas"] = self.memory_card["jogadas"] - 1

			self.arq = open("memory_card_battle_field.txt","w")
			self.arq.write(repr(self.memory_card)+"\n")
			self.arq.close()

			resposta = "Errou abestado!!!"
			return resposta
		else:
			self.arq = open("memory_card_battle_field.txt","r")
			self.memory_card = ast.literal_eval(self.arq.readline())
			self.arq.close()

			self.memory_card["acertos"] = self.memory_card["acertos"] + 1
			self.memory_card["jogadas"] = self.memory_card["jogadas"] - 1

			self.arq = open("memory_card_battle_field.txt","w")
			self.arq.write(repr(self.memory_card)+"\n")
			self.arq.close()

			resposta = "Acertou um navio miserave!!!"
			return resposta

	def jogar(self,linha, coluna, tabuleiro):
		self.tabuleiro = tabuleiro
		self.linha = linha
		self.coluna = coluna

		if self.tabuleiro[self.linha][self.coluna] == 1:
			return "navio"
		else:
			return "agua"

	def jogadas_esgotadas(self):
		self.arq = open("memory_card_battle_field.txt","r")
		self.memory_card = ast.literal_eval(self.arq.readline())
		self.arq.close()

		self.tabuleiro = self.memory_card["tabuleiro"]
		self.jogadas = self.memory_card["jogadas"]
		self.acertos = self.memory_card["acertos"]

	def novo_jogo(self):
		resposta = "Testando comunicacao"
		return resposta

		return("\nSuas jogadas esgotaram\nResultado Final\n Acertos: %d\n"%(self.acertos))