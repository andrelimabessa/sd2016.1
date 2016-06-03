#tabuleiro.py

class Tabuleiro(object):

	def __init__(self, qtd_linhas, qtd_colunas):
		self.qtd_colunas = int(qtd_colunas)
		self.qtd_linhas = int(qtd_linhas)
		self.tabuleiro = cria_tabuleiro()

	def cria_tabuleiro(self):
		tabuleiro = []
		for linha in range(self.qtd_linhas):
			for coluna in range(self.qtd_colunas):
				tabuleiro[linha][coluna] = 0

		return tabuleiro

	def get_qtd_colunas(self):
		return self.qtd_colunas

	def get_qtd_linhas(self):
		return self.qtd_linhas

	def get_tabuleiro(self):
		return self.tabuleiro