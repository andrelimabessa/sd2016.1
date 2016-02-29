#batalha_naval.py

import random

class BatalhaNaval(object):
	
	tabuleiro = None
	jogadas = 5
	acertos = 0

	def cria_tabuleiro(self, linhas, colunas):
		self.linhas = linhas
		self.colunas = colunas
		self.tabuleiro = [[0 for j in range(self.colunas)] for i in range(self.linhas)]

	def distribuir_navios(self):
		for i in self.tabuleiro:
			i[random.randint(0,4)] = 1


	def jogada(self, linha, coluna):
		self.linha = linha
		self.coluna = coluna

		if self.tabuleiro[self.linha][self.coluna] == 1:
			print("Acertou miseráve!!")
			self.acertos = self.acertos + 1
		else:
			print("Foi mal chapa!!!")

		self.jogadas = self.jogadas -1

	def atualiza_jogadas(self, jogadas):
		if jogadas < self.jogadas:
			self.jogadas = jogadas
		else:
			jogadas = 5

	def atualiza_acertos(self, acertos):
		if acertos > self.acertos:
			self.acertos = acertos
		else:
			acertos = 0