#acoes.py

import ast

class Acoes(object):
	
	def ler_jogo(self):
		arq = open("memory_card_battle_field.txt", "r")
		line = arq.readline()
		if len(line) > 0:
			return line
