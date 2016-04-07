class Batalha_Naval():
    
    
    def __init__(self, dimensoes, chances):
        self.agua = 0
        self.barco = 1
        self.acerto = 2
        self.erro = 3
        self.dimensoes = dimensoes
        self.chances = chances
        self.criarTabuleiro()
        self.popularTabuleiro()
        
    def criarTabuleiro(self):
        self.tabuleiro = [[ 0 for j in range(self.dimensoes) ] for w in range(self.dimensoes)]
            
    def popularTabuleiro(self):
        self.tabuleiro[0][1] = self.barco
        self.tabuleiro[2][3] = self.barco
        self.tabuleiro[4][2] = self.barco
        print(self.tabuleiro)
        
    def jogada(self,linha,coluna):
        if self.tabuleiro[int(linha)][int(coluna)] == self.barco: 
            self.tabuleiro[int(linha)][int(coluna)] = self.acerto
            self.chances = self.chances - 1
            print("Acerto ")
        elif self.tabuleiro[int(linha)][int(coluna)] == self.acerto or self.tabuleiro[int(linha)][int(coluna)] == self.erro:
            print("Escolha outra posição")
        else: 
            self.tabuleiro[int(linha)][int(coluna)] = self.erro
            self.chances = self.chances - 1
            print("Água ")
        
    
        
        


