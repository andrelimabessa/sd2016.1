class Batle_Field(object):

    def __init__(self):
        self.matriz = [[0 for i in range(5)] for j in range(5)]
        self.matriz[1][1] = "achou"

    
    def jogar(self,eixoX, eixoY):
        try:
            if self.matriz[int(eixoX)][int(eixoY)]=="achou":
                return "acertou"
            
        except:
            val = sys.exc_info()[0]
            print(val)