class Batalha_Naval(object):
    def __init__(self,tam_tabuleiro):
        self.tabuleiro = [[0 for j in range(tam_tabuleiro)] for i in range(tam_tabuleiro)]

    def mostraTabuleiro(self):
        print(self.tabuleiro)

    def alocarFrota(self, posicoes):
        for i in range(len(posicoes)):
            self.tabuleiro[posicoes[i][0]][posicoes[i][1]] = 1

    def atirar(self, posicao):
        if self.tabuleiro[posicao[0]][posicao[1]] == 1:
            print("Navio abatido!")
            self.tabuleiro[posicao[0]][posicao[1]] = 'X'
            self.mostraTabuleiro()
        else:
            print("Água!")