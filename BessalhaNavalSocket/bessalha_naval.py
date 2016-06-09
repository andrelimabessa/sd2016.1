import ast
import random

class Bessalha_Naval(object):
    
    tabuleiro = []
    #qt_Tiros = 1

    def __init__(self):
        self.tabuleiro = [[0 for i in range(5)] for j in range(5)]

    def checkSave(self):
        qt_Tiros = 0
        arq = open("lista.txt", "r")
        linha = arq.readlines()
        if int(linha[1]) <= 5:
            self.tabuleiro = ast.literal_eval(linha[0])
            self.qt_Tiros = int(linha[1])
            return self.qt_Tiros
        arq.close()

    def save(self,qt_Tiros):
        arq = open("lista.txt", "w")
        arq.write(str (self.tabuleiro) + '\n')
        arq.write(str (qt_Tiros))
        arq.close()

    def mostrarTabuleiro(self):
        for i in self.tabuleiro:
            print (i)

    def barquinhos(self):
            self.tabuleiro[0][4] = 1
            self.tabuleiro[4][1] = 1

            ## Pq ele fica apagando a porra da matriz
            #i = 0
            #posicao = 0
            #while (i < 5):
            #    self.tabuleiro[posicao][posicao] = 1
            #    posicao = random.randint(0,4)
            #    i+=1

            ##pq ele n pode mostrar a porra da matriz no inicio
            #self.mostrarTabuleiro()

    def tiro(self, X, Y):
        #qt_Tiros = 1
        #navioAbatido = 0
        #deveContinuar = True
        #acertou = 0

        if (self.tabuleiro[int(X)][int(Y)] == 1):
            mapComand = {}
            self.tabuleiro[int(X)][int(Y)] = 'x'
            J1 = 1
            J2 = "KabOoOm !!!"
            mapComand["J1"] = J1
            mapComand["J2"] = J2
            self.mostrarTabuleiro()
            return str(mapComand)

        elif (self.tabuleiro[int(X)][int(Y)] == 0):
            mapComand = {}
            self.tabuleiro[int(X)][int(Y)] = '~'
            J1 = 0
            J2 = "Água mané !!!"
            mapComand["J1"] = J1
            mapComand["J2"] = J2
            self.mostrarTabuleiro()
            return str(mapComand)

        elif (self.tabuleiro[int(X)][int(Y)] == '~' or 'x'):
            mapComand = {}
            J1 = 0
            J2 = "Já jogou aí ¬¬'"
            mapComand["J1"] = J1
            mapComand["J2"] = J2
            self.mostrarTabuleiro()
            return str(mapComand)