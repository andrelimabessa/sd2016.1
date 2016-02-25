import random

linha = 0

def cria_campo_de_batalha():
        print("Qual o tamanho do campo de batalha?: ")
        entrada_tamanho = input()
        tamanho_do_campo = int(entrada_tamanho)
        campo_de_batalha = [[0 for j in range(tamanho_do_campo)] for i in range(tamanho_do_campo)]
for i in campo_de_batalha:
    print("Na linha %d diga onde você quer colocar um navio: " %(linha))
    entrada = input()
    coluna = int(entrada)
    i[coluna] = 1
    linha = linha + 1

for j in campo_de_batalha:
    print(j)
