#jogo.py

from tabuleiro import Tabuleiro
from jogador import Jogador
import ast

class Jogo(object):

    def __init__(self, nome_jogador, qtd_linhas, qtd_colunas):
        self.jogador = Jogador(nome_jogador)
        self.tabuleiro = Tabuleiro(int(qtd_linhas), int(qtd_colunas))
        self.acertos = 0
        self.jogadas_restantes = self.tabuleiro.get_qtd_linhas()

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

    def informacoes_do_jogo(self):
        print("\nNome do jogador: %s"%(self.jogador.get_nome_jogador()))
        print("Quantidade de Linhas do Tabuleiro: %i"%(self.tabuleiro.get_qtd_linhas()))
        print("Quantidade de Colunas do Tabuleiro: %i"%(self.tabuleiro.get_qtd_colunas()))

    def resetar_acertos(self):
        self.acertos = 0
        print("Quantidade de acertos ajustada para %i"%(self.get_acertos()))

    def resetar_jogadas_restantes(self):
        self.jogadas_restantes = self.tabuleiro.get_qtd_linhas()
        print("Jogadas restantes: %i"%(self.get_jogadas_restante()))

    def realizar_jogada(self, linha, coluna):
        tabuleiro = self.tabuleiro.get_tabuleiro()

        if isinstance(ast.literal_eval(linha), int) or isinstance(ast.literal_eval(coluna), int):
            if tabuleiro[int(linha)][int(coluna)] == 1:
                self.set_acertos()
                self.set_jogadas_restantes()
                print("Acertou Miseráve!!!!")
                print("Você acertou %i tiros"%(self.get_acertos()))
                print("Você ainda possui %i jogadas restantes!!"%(self.get_jogadas_restante()))
                return True
            else:
                self.set_jogadas_restantes()
                print("Tiro na água chapa!!!")
                print("Você acertou %i tiros"%(self.get_acertos()))
                print("Você ainda possui %i jogadas restantes!!"%(self.get_jogadas_restante()))
                return True
        else:
            return False