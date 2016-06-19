# -*- coding: utf-8 -*-

import random

class Tabuleiro(object):

	def __init__(self, qtd_linhas, qtd_colunas, tabuleiro):
		self.qtd_colunas = int(qtd_colunas)
		self.qtd_linhas = int(qtd_linhas)
		self.tabuleiro = tabuleiro
		print("Tabuleiro Criado com Sucesso!!!")
		print("\n")

	def get_qtd_colunas(self):
		return self.qtd_colunas

	def get_qtd_linhas(self):
		return self.qtd_linhas

	def get_tabuleiro(self):
		return self.tabuleiro

	def set_qtd_linhas(self, qtd_linhas):
		self.qtd_linhas = qtd_linhas

	def set_qtd_colunas(self, qtd_colunas):
		self.qtd_colunas = qtd_colunas

	def set_tabuleiro(self, tabuleiro):
		self.tabuleiro = tabuleiro

	def imprime_tabuleiro(self):
		for linha in self.tabuleiro:
			print(linha)

	def reset_tabuleiro(self):
		self.tabuleiro = [ [0 for coluna in range(self.get_qtd_colunas())] for linha in range(self.get_qtd_linhas()) ]

	def distribuir_navios(self):
		self.reset_tabuleiro()
		for linha in self.tabuleiro:
			linha[random.randint(0, len(linha)-1)] = 1

		return 'Navios Distribuidos com Sucesso!!'