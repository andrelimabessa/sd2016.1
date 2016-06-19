# -*- coding: utf-8 -*-

from tabuleiro import Tabuleiro
from jogador import Jogador
import ast
import arquivo

class Jogo(object):
    nome_jogador = ""
    qtd_linhas = 0
    qtd_colunas = 0

    def __init__(self, nome_jogador = None, qtd_linhas = None, qtd_colunas = None, matriz = None):#TypeError
        if (nome_jogador is not None) and (qtd_linhas is not None) and (qtd_colunas is not None):
            if matriz is not None:
                self.matriz = matriz
            else:
                self.matriz = [ [0 for coluna in range(int(qtd_colunas))] for linha in range(int(qtd_linhas)) ]
            self.jogador = Jogador(nome_jogador)
            self.tabuleiro = Tabuleiro(int(qtd_linhas), int(qtd_colunas), matriz)
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

    def set_nome_jogador(self, nome_jogador):
        self.jogador = Jogador(nome_jogador)

    def set_tabuleiro(self, qtd_linhas, qtd_colunas):
        self.tabuleiro = Tabuleiro(qtd_linhas, qtd_colunas)

    def informacoes_do_jogo(self):
        print("\n")
        print("Nome do jogador: %s"%(self.get_nome_jogador()))
        print("Quantidade de Linhas do Tabuleiro: %i"%(self.get_qtd_linhas()))
        print("Quantidade de Colunas do Tabuleiro: %i"%(self.get_qtd_colunas()))
        print("\n")

    def resetar_acertos(self):
        self.acertos = 0
        print("Quantidade de acertos ajustada para %i"%(self.get_acertos()))

    def atualizar_acertos(self, value):
        self.acertos = value

    def resetar_jogadas_restantes(self):
        self.jogadas_restantes = self.get_qtd_linhas()
        print("Jogadas restantes: %i"%(self.get_jogadas_restantes()))

    def atualizar_jogadas_restantes(self, value):
        self.jogadas_restantes = value

    def realizar_jogada(self, linha, coluna):
        tabuleiro = self.get_tabuleiro()

        if isinstance(ast.literal_eval(linha), int) and isinstance(ast.literal_eval(coluna), int):
            if tabuleiro[int(linha)][int(coluna)] == 1:
                self.set_acertos()
                self.set_jogadas_restantes()

                return 'Show acertou'
            else:
                self.set_jogadas_restantes()

                return 'Errou'
        else:
            return 'Errou'

    def visualizar(self):
        return str(self.get_qtd_linhas()) + ',' + str(self.get_qtd_colunas()) + ',' + str(self.get_acertos()) + ',' + str(self.get_jogadas_restantes())

    def salvar_jogo(self):
        memoria = {}
        memoria["jogador"] = self.get_nome_jogador()
        memoria["qtd_linhas"] = self.get_qtd_linhas()
        memoria["qtd_colunas"] = self.get_qtd_colunas()
        memoria["tabuleiro"] = self.get_tabuleiro()
        memoria["acertos"] = self.get_acertos()
        memoria["jogadas_restantes"] = self.get_jogadas_restantes()
        arq = open(arquivo.CONST_PATH_FILE, "w")
        arq.write(str(memoria))
        arq.close()

    def verificar_se_tem_algo_salvo(self):
        arq = open(arquivo.CONST_PATH_FILE, "r")
        memoria = arq.readline()
        arq.close()
        if len(memoria) <= 0:
            return False
        else:
            return True

    def ler_arquivo(self):
        arq = open(arquivo.CONST_PATH_FILE, "r")
        memoria = arq.readline()
        arq.close()
        return memoria