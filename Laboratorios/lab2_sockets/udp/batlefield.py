import sys
import random

class Batle_Field(object):

    def __init__(self,tam):
        self.matriz = [[0 for i in range(int(tam))] for j in range(int(tam))]
        for i in range(int(tam)):
            for j in range(int(tam)):
                self.matriz[i][j] = "agua"
        
    def preencher(self,tam,navios):
        for i in range(int(navios)):
            x = random.randint(0,int(tam)-1)
            y = random.randint(0,int(tam)-1)
            self.matriz[x][y] = "navio"
        arq = open("arq.txt", "a")
        arq.write(str(self.matriz))
        arq.close()
        return self.matriz

    def jogar(self,eixoX,eixoY):
        import sys
        try:
            arq = open("arq.txt", "r")
            print(arq.readline())
            for linha in arq:
                print(linha)
            arq.close()
            if self.matriz[int(eixoX)][int(eixoY)]=="navio":
                self.matriz[int(eixoX)][int(eixoY)]="acertou"
                arq = open("arq.txt", "w")
                arq.write(str(self.matriz))
                arq.close()
                return True
            else:
                return False
        except:
            val = sys.exc_info()[0]
            print(val)
