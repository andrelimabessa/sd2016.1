import random

class BatalhaNaval(object):

    def __init__(self):
        print("---------------------------------------------")
        print("Defina o tamanho do tabuleiro de 5 a 10:")
        valor = 5
        tamanho = int(valor)
        self.tabuleiro = [[0 for i in range(tamanho)] for j in range(tamanho)]
        print("---------------------------------------------")
        print("Tabuleiro criado com sucesso!!!")

    def imprimeTabuleiro(self):
        for i in self.tabuleiro:
            print (i)

    def insereNavios(self):
        i = 0
        posicao = 0
        print("---------------------------------------------")
        while (i < 5):
            self.tabuleiro[posicao][posicao] = 1
            posicao = random.randint(0,4)
            # print(valores)
            i+=1
        print("saio inserir navio")    
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
