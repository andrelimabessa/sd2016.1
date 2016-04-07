from batalhanaval import Batalha_Naval

batalha = Batalha_Naval(5,3)

while batalha.chances != 0:
    linha = input("linha: ")
    coluna = input("coluna: ")
    batalha.jogada(linha,coluna)

input()