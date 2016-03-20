#acoes.py

import ast

class Acoes(object):
	arq = open("memory_card_battle_field.txt", "r")
	line = arq.readline()
	arq.close()
	dados = ast.literal_eval(line)

	def ler_jogo(self):
		if len(line) > 0:
			retorno = "Acertos: %d ; Jogadas Restantes: %d"%(dados["acertos"],dados["jogadas"])
			return retorno

	def continuar_jogo(self):
		if len(line) > 0:
			if dados["jogadas"] > 0:
				return 1
			else:
				return 2
#