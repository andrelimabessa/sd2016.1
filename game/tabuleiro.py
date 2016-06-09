
class Tabuleiro(object):
    'Classe dp tabuleiro'

    def __init__(self, tam):
        self.matriz = [[0 for i in range(int(tam))] for j in range(int(tam))]
        for i in range(int(tam)):
            for j in range(int(tam)):
                self.matriz[i][j] = "erro"

    def preencher(self, tam, navios):
        import sys
        import random

        for i in range(int(navios)):
            x = random.randint(0, int(tam) -1)
            y = random.randint(0, int(tam) -1)
            self.matriz[x][y] = "ok"

        arq = open("rafael.txt", "w")
        arq.write(str(self.matriz))
        arq.close()

    def jogar(self, x, y):
        import sys
        try:
            x = int(x)
            y = int(y)
            if self.matriz[x][y] == "ok":
                self.matriz[x][y] = "acertou"

                arq = open("rafael.txt", "w")
                arq.write(str(self.matriz))
                arq.close()

                return True
            else:

                return False
        except:
            val = sys.exc_info()[0]
            print(val)

