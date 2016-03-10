from random import randint

tabuleiro = []

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

navioLinha = randomLinha(tabuleiro)
navioColuna = randomColuna(tabuleiro)
print (navioLinha)
print (navioColuna)

linhaInformada = int(input("Linha: "))
colunaInformada = int(input("Coluna: "))

if linhaInformada == navioLinha and colunaInformada == navioColuna:
    print ("Parabéns! Você afundou o navio!")
else:
    if (linhaInformada < 0 or linhaInformada > 4) or (colunaInformada < 0 or colunaInformada > 4):
        print ("Essa foi longe!")
    elif(tabuleiro[linhaInformada][colunaInformada] == "X"):
        print ("Você já tentou essa posição antes.")
    else:
        print ("Você errou o navio.")
        tabuleiro[linhaInformada][colunaInformada] = "X"
    # 
    escreverTabuleiro(tabuleiro)
