from batlefield import Batle_Field

tam = input("Digite o tamanho da matriz")

navios = input("Digite a quantidade de navios")

b = Batle_Field(tam)

b.preencher(tam,navios)

for i in range(int(tam)):
    eixoX = input("Digite o posicao x")
    eixoY = input("Digite o posicao y")
    print(b.jogar(eixoX, eixoY))

input()