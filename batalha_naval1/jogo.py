#jogo.py

class Jogo(object):

    def __init__(self, nome_jogador, tabuleiro):
        self.jogador = nome_jogador
        self.tabuleiro = tabuleiro
        self.acertos = 0
        self.jogadas_restantes = len(tabuleiro)

    def set_acertos(self):
        self.acertos = self.acertos + 1

    def get_acertos(self):
        return self.acertos

    def set_jogadas_restantes(self):
        if self.jogadas_restantes == 0:
            self.jogadas_restantes = self.jogadas_restantes
        else:
            self.jogadas_restantes = self.jogadas_restantes - 1

    def get_jogadas_restante(self):
        return self.jogadas_restantes