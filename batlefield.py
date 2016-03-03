class Batle_Field(object):

    def __init__(self,tam):
        self.matriz = [[0 for i in range(int(tam))] for j in range(int(tam))]
        for i in range(int(tam)):
            for j in range(int(tam)):
                self.matriz[i][j] = "agua"
        
    def preencher(self,tam,navios):
        import sys
        import random
        for i in range(int(navios)):
            x = random.randint(0,int(tam)-1)
            y = random.randint(0,int(tam)-1)
            self.matriz[x][y] = "navio"
        print(self.matriz)

    def jogar(self,eixoX,eixoY):
        import sys
        try:
            if self.matriz[int(eixoX)][int(eixoY)]=="navio":
                return "acertou"
            else:
                return "errou"
        except:
            val = sys.exc_info()[0]
            print(val)
