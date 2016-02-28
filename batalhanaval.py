import random

class BatalhaNaval(object):

    def __init__(self):
        print ("Defina o tamanho do tabuleiro de 5 a 10: ")
        valor = input()

        if (int(valor) < 5) or (int(valor) > 10):
            print("Digite um valor Válido de 5 e 10")
        else:
            tamanho = int(valor)
            self.tabuleiro = [[0 for i in range(tamanho)] for j in range(tamanho)]
            print("Tabuleiro criado com sucesso!!!")

    def imprimeTabuleiro(self):
        for i in self.tabuleiro:
            print (i)

    def insereNavios(self):
        i = 0
        posicao = 0
        while (i < 5):
            self.tabuleiro[posicao][posicao] = 1
            posicao = random.randint(0,4)
            # print(valores)
            i+=1

    def jogada(self):

        numJogada = 0
        chance = 1
        erro = 0
        acerto = 0
        print ("================================================")
        print ("Você terá 5 Chances!!!")

        while (numJogada != 5):
            print ("%d Chance: " %(chance))
            print ("Informe a linha: ")
            linha = input()
            print ("Informe a coluna: ")
            coluna = input()

            print ("JOGADA ( " + linha + ", " + coluna + " )")

            if (self.tabuleiro[int(linha)][int(coluna)] == 1):
                print("Você acertou o navio!")
                acerto+=1
            else:
                print("Tiro na água, tente novamente!")
                erro+=1

            chance+=1
            numJogada+=1
            # print(numJogada)

        arquivo = open("resultado.txt", "w")
        arquivo.write("=====================================================================================\n")
        arquivo.write("                        JOGO - BATALHA NAVAL - Versão 1.0\n")
        arquivo.write("=====================================================================================\n")
        arquivo.write("# Estatísticas do jogo:\n")
        arquivo.write("\n- Numero de Jogadas: %d " %(numJogada))
        arquivo.write("\n-------------------------------------------------------------------------------------\n")
        arquivo.write("\n- Total de acertos: %d" %(acerto))
        arquivo.write("\n-------------------------------------------------------------------------------------\n")
        arquivo.write("\n- Total de erros: %d" %(erro))
        arquivo.write("\n-------------------------------------------------------------------------------------\n")
        arquivo.write("\n")
        arquivo.write("\n================================= by: Lucas Albuquerque =============================")
        arquivo.close()
