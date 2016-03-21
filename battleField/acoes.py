#acoes.py

import ast

class Acoes(object):
	arq = open("memory_card_battle_field.txt", "r")
	memory_card = arq.readline()
	arq.close()
	dados = ast.literal_eval(memory_card)

	def ler_jogo(self):
		if len(self.memory_card) > 0:
			retorno = "Acertos: %d; Jogadas Restantes: %d"%(self.dados["acertos"], self.dados["jogadas"])
			return retorno

	def continuar_jogo(self):
		if self.dados["jogadas"] > 0:
			return 1
		else:
			return 2

	def novo_jogo(self):
		pass