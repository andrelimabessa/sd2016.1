import ast

class Bessalha_Naval(object):
    
    tabuleiro = []
    qt_Tiros = 1

    def __init__(self):
    
        self.tabuleiro = [[0 for i in range(5)] for j in range(5)]

    def checkSave(self):
        arq = open("lista.txt", "r")
        linha = arq.readlines()
        if int(linha[1]) < 6:
            self.tabuleiro = ast.literal_eval(linha[0])
            self.qt_Tiros = int(linha[1])
        arq.close()

    def mostrarTabuleiro(self):
        for i in self.tabuleiro:
            print (i)

    def barquinhos(self):

            self.tabuleiro[0][4] = 1
            self.tabuleiro[4][1] = 1

    def tiro(self):

        qt_Tiros = 1
        navioAbatido = 0
        deveContinuar = True

        while (deveContinuar):
            print ("%d Tiro: " %(qt_Tiros))
            print ("Informe a Coordenada X: ")
            X = input()
            print ("Informe a Coordenada Y: ")
            Y = input()

            if (self.tabuleiro[int(X)][int(Y)] == 1):
                print("KabOoOm !!!")
                self.tabuleiro[int(X)][int(Y)] = 'x'
                navioAbatido += 1

            elif (self.tabuleiro[int(X)][int(Y)] == 0):
                print("Água mané !!!")
                self.tabuleiro[int(X)][int(Y)] = '~'

            elif (self.tabuleiro[int(X)][int(Y)] == '~' or 'x'):
                print("Já jogou aí ¬¬'")

            qt_Tiros += 1
            
            if(qt_Tiros <= 5):
                deveContinuar = True
            else:
                deveContinuar = False

            if (navioAbatido == 2):
                deveContinuar = False

            arq = open("lista.txt", "w")
            arq.write(str (self.tabuleiro) + '\n')
            arq.write(str (qt_Tiros))
            arq.close()

        if (navioAbatido == 2):
            #qt_Tiros = 6
            print("Ganhou Mizerávi !!!")
            
        else:
            print("Perdeu! Pior é na guerra.")

        

            
