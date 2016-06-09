#jogar.py

from jogo import Jogo
import ast
import sys
import menus

class Jogar(object):

    def inicio(self):
        self.opcao = False
        self.ativo = False

        while self.opcao == False:
            self.set_opcao(menus.menu_inicial())
            #self.opcao = menus.menu_inicial()

            try:
                if isinstance(ast.literal_eval(self.opcao), int):
                    if int(self.get_opcao()) == 1:
                        self.set_opcao(novo_jogo(self))
                    elif int(self.get_opcao()) == 2:
                        self.set_opcao(continuar_jogo(self))
                    elif int(self.get_opcao()) == 3:
                        self.set_opcao(True)
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

def acoes(self, jogo):
    while self.get_ativo():
        opcao = menus.menu_novo_jogo()

        if isinstance(ast.literal_eval(opcao), str):
            print("Opção Inválida!!!\n\n")
        elif int(opcao) == 1:
            jogo.tabuleiro.distribuir_navios()
            jogo.resetar_acertos()
            jogo.resetar_jogadas_restantes()
            self.set_ativo(True)
            print("\n")

        elif int(opcao) == 2:
            if jogo.get_jogadas_restantes() > 0:
                deu_certo = False
                while deu_certo == False:
                    linha = input("Digite a linha: \n")
                    coluna = input("Digite a colluna: \n")

                    deu_certo = jogo.realizar_jogada(linha, coluna)
                    print("\n")
            else:
                print("Suas Jogadas esgotaram!!!")
                print("\n")

            self.set_ativo(True)

        elif int(opcao) == 3:
            jogo.ver_estado_do_jogo()
            self.set_ativo(True)

        elif int(opcao) == 4:
            jogo.salvar_jogo()
            print("Jogo Salvo!")
            self.set_ativo(True)
            print("\n")

        elif int(opcao) == 5:
            self.set_ativo(False)
            print("Saindo do Jogo!!!!")
            print("\n")

        elif int(opcao) == 6:
            print("\n")
            print("Tabuleiro:")
            jogo.tabuleiro.imprime_tabuleiro()
            self.set_ativo(True)
            print("\n")

        else:
            print("Opção Inválida!!!\n\n")

def novo_jogo(self):
    self.set_ativo(True)

    #Atribuição de múltiplos atributos através do retorno de uma tupla de valores na função que está sendo chamada.
    nome_jogador, qtd_linhas, qtd_colunas = menus.menu_novo_jogo_abertura()

    jogo = Jogo(nome_jogador, qtd_linhas, qtd_colunas)
    jogo.informacoes_do_jogo()

    acoes(self, jogo)

    return False

def continuar_jogo(self):
    self.set_ativo(True)
    jogo = Jogo()

    if jogo.verificar_se_tem_algo_salvo():
        memoria = ast.literal_eval(jogo.ler_arquivo())

        jogo = Jogo(memoria["jogador"], memoria["qtd_linhas"], memoria["qtd_colunas"], memoria["tabuleiro"])
        jogo.atualizar_acertos(memoria["acertos"])
        jogo.atualizar_jogadas_restantes(memoria["jogadas_restantes"])

        jogo.informacoes_do_jogo()

        acoes(self, jogo)

    return False

jogar = Jogar()
jogar.inicio()