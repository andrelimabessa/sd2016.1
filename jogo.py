import random

class BatalhaNaval(object):

    def __init__(self, tamanho_tabuleiro):
        print("---------------------------------------------")

        self.tabuleiro = [[0 for i in range(int(tamanho_tabuleiro))] for j in range(int(tamanho_tabuleiro))]
        self.acertos = 0
        self.jogadas = int(tamanho_tabuleiro)

        print("---------------------------------------------")
        print("Tabuleiro criado com sucesso!!!")

    def imprimeTabuleiro(self):
        for linha in self.tabuleiro:
            print(linha)

    def insereNavios(self):
        print("---------------------------------------------")
        for linha in self.tabuleiro:
            posicao = random.randint(0,len(linha)-1)
            linha[posicao] = 1
        print("Navios inseridos com sucesso!!!!")

    def jogada(self, linha, coluna):

        numJogada = 0
        chance = 1
        erro = 0
        acerto = 0
        #print ("================================================")
        #print ("Você terá 5 Chances!!!")

        #print ("%d Chance: " %(chance))

        print ("JOGADA ( " + linha + ", " + coluna + " )")

        if (self.tabuleiro[int(linha)][int(coluna)] == 1):
            acerto+=1
            return "Você acertou o navio!"
        else:
            erro+=1
            return "Tiro na água, tente novamente!"


            chance+=1
            numJogada+=1
            # print(numJogada)
