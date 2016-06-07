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

    def get_jogadas_restantes(self):
        return self.jogadas_restantes

    def get_qtd_linhas(self):
        return self.tabuleiro.get_qtd_linhas()

    def get_qtd_colunas(self):
        return self.tabuleiro.get_qtd_colunas()

    def get_nome_jogador(self):
        return self.jogador.get_nome_jogador()

    def get_tabuleiro(self):
        return self.tabuleiro.get_tabuleiro()

    def informacoes_do_jogo(self):
        print("\nNome do jogador: %s"%(self.get_nome_jogador()))
        print("Quantidade de Linhas do Tabuleiro: %i"%(self.get_qtd_linhas()))
        print("Quantidade de Colunas do Tabuleiro: %i"%(self.get_qtd_colunas()))

    def resetar_acertos(self):
        self.acertos = 0
        print("Quantidade de acertos ajustada para %i"%(self.get_acertos()))

    def resetar_jogadas_restantes(self):
        self.jogadas_restantes = self.get_qtd_linhas()
        print("Jogadas restantes: %i"%(self.get_jogadas_restantes()))

    def realizar_jogada(self, linha, coluna):
        tabuleiro = self.get_tabuleiro()

        if isinstance(ast.literal_eval(linha), int) and isinstance(ast.literal_eval(coluna), int):
            if tabuleiro[int(linha)][int(coluna)] == 1:
                self.set_acertos()
                self.set_jogadas_restantes()
                print("Acertou Miseráve!!!!")
                print("Você acertou %i tiros"%(self.get_acertos()))
                print("Você ainda possui %i jogadas restantes!!"%(self.get_jogadas_restantes()))
                return True
            else:
                self.set_jogadas_restantes()
                print("Tiro na água chapa!!!")
                print("Você acertou %i tiros"%(self.get_acertos()))
                print("Você ainda possui %i jogadas restantes!!"%(self.get_jogadas_restantes()))
                return True
        else:
            return False

    def ver_estado_do_jogo(self):
        print("\n")
        print("Tabuleiro:")
        print("Qtd de linhas: %i"%(self.get_qtd_linhas()))
        print("Qtd de colunas: %i"%(self.get_qtd_colunas()))
        print("Pontuação: ")
        print("Acertos: %i"%(self.get_acertos()))
        print("Jogadas restantes: %i"%(self.get_jogadas_restantes()))
        print("\n")