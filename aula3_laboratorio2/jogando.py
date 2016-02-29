#jogando.py

from batalha_naval import BatalhaNaval
import random
#import json
import ast

t = BatalhaNaval()

tentar = False

salvar = False

memory_card = {}

def comecando_jogo():
	arq = open("memory_card.txt", "r")
	linha = arq.readline()
	if len(linha) > 0:
		memory_card = ast.literal_eval(linha)
		t.tabuleiro = memory_card["tabuleiro"]
		t.jogadas = memory_card["jogadas"]
		t.acertos = memory_card["acertos"]
		arq.close()
	else:
		t.cria_tabuleiro(5,5)
		t.distribuir_navios()

comecando_jogo()

while t.jogadas > 0:

	print("Você tem %d jogada(s). Deseja Jogar nesse momento? \'Sim\' ou \'Não\': "%(t.jogadas))
	
	tentar = input()

	if tentar == "Sim":
		tentar = True
	else:
		tentar = False

	if tentar == True:
		t.jogada(random.randint(0,4),random.randint(0,4))
		salvar = input("Deseja Salvar suas jogadas?\'Sim\' ou \'Não\': ")
	else:
		salvar = input("Deseja Salvar suas jogadas?\'Sim\' ou \'Não\': ")

	if salvar == "Sim":
		salvar = True
		memory_card["jogadas"] = t.jogadas
		memory_card["acertos"] = t.acertos
		memory_card["tabuleiro"] = t.tabuleiro
		print(memory_card)
		arq = open("memory_card.txt", "w")
		arq.write(repr(memory_card)+"\n")
		#arq.write("Quantidade de Jogadas Restantes: %d \n"%(t.jogadas))
		#arq.write("Quantidade de Acertos: %d \n"%(t.acertos))
		arq.close()
		break
	else:
		salvar = False
		arq.close()
		break

if t.jogadas <= 0:
	print("Sinto Muito, suas jogadas Terminaram!!")

#arq = open("memory_card.txt", "r")
#print(arq.readline())
#for linha in arq:
#	print(linha)
#arq.close()