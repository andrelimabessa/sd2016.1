#jogar.py

from jogo import Jogo
import ast
import sys

class Jogar(object):

    def inicio(self):
        self.opcao = False
        self.ativo = False

        while self.opcao == False:
            print("Escolha a opção: ")
            print("1 - Novo Jogo.")
            self.opcao = input("Opção: \n")

            try:
                if isinstance(ast.literal_eval(self.opcao), int):
                    if int(self.opcao) == 1:
                        novo_jogo(self)
            except ValueError:
                print(("Opção inválida: " + repr(self.opcao)))
                self.opcao = False

    def get_opcao(self):
        return self.opcao

    def set_opcao(self, value):
        self.opcao = value

    def get_ativo(self):
        return self.ativo

    def set_ativo(self, value):
        self.ativo = value

def novo_jogo(self):
    self.set_ativo(True)

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
        print("3 - Ver estado do jogo.")
        print("4 - Salvar")
        print("5 - Sair.")

        opcao = input("Opção: \n")

        if isinstance(ast.literal_eval(opcao), str):
            print("Opção Inválida!!!\n\n")
        elif int(opcao) == 1:
            jogo.tabuleiro.distribuir_navios()
            jogo.resetar_acertos()
            jogo.resetar_jogadas_restantes()
        elif int(opcao) == 2:
            if jogo.get_jogadas_restante() > 0:
                deu_certo = False
                while deu_certo == False:
                    linha = input("Digite a linha: \n")
                    coluna = input("Digite a colluna: \n")

                    deu_certo = jogo.realizar_jogada(linha, coluna)
            else:
                print("Suas Jogadas esgotaram!!!")
        elif int(opcao) == 3:
            print("Tabuleiro:")
            print("Qtd de linhas: %i"%(jogo.tabuleiro.get_qtd_linhas()))
            print("Qtd de colunas: %i"%(jogo.tabuleiro.get_qtd_colunas()))
            print("Pontuação: ")
            print("Acertos: %i"%(jogo.get_acertos()))
            print("Jogadas restantes: %i"%(jogo.get_jogadas_restante()))
        elif int(opcao) == 4:
            arq = open("memory_card.txt", "w")
            arq.write(repr(jogo)+"\n")
            arq.close()
            print("Jogo Salvo!")
        elif int(opcao) == 5:
            print("Testando a saida")
        else:
            print("Opção Inválida!!!\n\n")

    jogo.tabuleiro.distribuir_navios()
    jogo.tabuleiro.imprime_tabuleiro()

jogar = Jogar()
jogar.inicio()