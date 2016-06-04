#jogar.py

from jogo import Jogo
import ast

class Jogar(object):

    def inicio(self):
        self.opcao = False
        self.ativo = False

        while self.opcao == False:
            print("Escolha a opção: ")
            print("1 - Novo Jogo.")
            self.opcao = input("Opção: \n")

            if isinstance(ast.literal_eval(self.opcao), str):
                print("Opção Inválida!!!\n\n")
                opcao = False
            elif int(self.opcao) == 1:
                novo_jogo(self)
            else:
                print("Opção Inválida!!!\n\n")
                self.opcao = False

def novo_jogo(self):
    self.ativo = True

    nome_jogador = (input("Digite o nome do jogador: \n"))
    print("Diga a quantidade de linhas do tabuleiro: ")
    qtd_linhas = input("Quantidade de Linhas: \n")
    print("Diga a quantidade de colunas do tabuleiro: ")
    qtd_colunas= input("Quantidade de Colunas: \n")

    jogo = Jogo(nome_jogador, qtd_linhas, qtd_colunas)
    jogo.informacoes_do_jogo()

    while self.ativo:
        print("Escolha o que deseja fazer: ")
        print("1 - Distribuir Navios.")
        print("2 - Realizar Jogada.")

        opcao = input("Opção: \n")

        if isinstance(ast.literal_eval(opcao), str):
            print("Opção Inválida!!!\n\n")
        elif int(opcao) == 1:
            jogo.tabuleiro.distribuir_navios()
            jogo.resetar_acertos()
            jogo.resetar_jogadas_restantes()
        elif int(opcao) == 2:
            deu_certo = False
            while deu_certo == False:
                linha = input("Digite a linha: \n")
                coluna = input("Digite a colluna: \n")

                deu_certo = jogo.realizar_jogada(linha, coluna)
        else:
            print("Opção Inválida!!!\n\n")

    jogo.tabuleiro.distribuir_navios()
    jogo.tabuleiro.imprime_tabuleiro()

jogar = Jogar()
jogar.inicio()