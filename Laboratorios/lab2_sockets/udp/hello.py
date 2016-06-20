from batlefield import Batle_Field

class Hello(object):

    def jogo(self):

        print("----------------------------")
        print("Bem Vindo ao Batalha Naval")
        print("----------------------------\n")

        tam = input("Digite o tamanho da matriz")

        navios = input("Digite a quantidade de navios")

        b = Batle_Field(tam)

        b.preencher(tam,navios)

        for i in range(int(tam)):
            eixoX = input("Digite o posicao x")
            eixoY = input("Digite o posicao y")
            if b.jogar(eixoX, eixoY):
                print("acertou")
            else:
                print("errou")

input()