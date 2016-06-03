#jogar.py

from jogador import Jogador
from jogo import Jogo
from tabuleiro import Tabuleiro
class Jogar(object):

    jogador = Jogador(input("Digite o nome do jogador: \n"))
    tabuleiro = Tabuleiro(input("Digite a quantidade de linhas: \n"), input("Digite a quantidade de colunas: \n"))

    print(jogador.get_nome_jogador())
    print(tabuleiro.get_tabuleiro())

    input()