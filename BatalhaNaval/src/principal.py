from random import randint

tabuleiro = []
maxJogadas = 5
jogadas = 0

for x in range(5):
    tabuleiro.append(["O"] * 5)

def escreverTabuleiro(tabuleiro):
    for linha in tabuleiro:
        print (" ".join(linha))

print ("[Início]")
escreverTabuleiro(tabuleiro)

def randomLinha(tabuleiro):
    return randint(0, len(tabuleiro) - 1)

def randomColuna(tabuleiro):
    return randint(0, len(tabuleiro[0]) - 1)

navioLinha = (randomLinha(tabuleiro) + 1)
navioColuna = (randomColuna(tabuleiro) + 1)
print (navioLinha)
print (navioColuna)
while (maxJogadas-jogadas) > 0:
    print ("Jogadas disponíveis: ", maxJogadas-jogadas)
    linhaInformada = int(input("Linha: "))
    colunaInformada = int(input("Coluna: "))
    linhaReal = linhaInformada - 1
    colunaReal = colunaInformada - 1
    if linhaInformada == navioLinha and colunaInformada == navioColuna:
        print ("Parabéns! Você afundou o navio!")
    else:
        if (linhaInformada <= 0 or linhaInformada > 5) or (colunaInformada <= 0 or colunaInformada > 5):
            print ("Essa foi longe!")
        elif(tabuleiro[linhaReal][colunaReal] == "X"):
            print ("Você já tentou essa posição antes.")
        else:
            print ("Você errou o navio.")
            tabuleiro[linhaReal][colunaReal] = "X"
        #
        jogadas = jogadas + 1
        escreverTabuleiro(tabuleiro)
print ("Suas jogadas disponíveis acabaram. Você perdeu!")
