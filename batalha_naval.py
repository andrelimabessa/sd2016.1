import random

class BatalhaNaval(object):
    def __init__(self):
        self.tam_tabuleiro = 5
        self.tam_frota = 7
        self.max_jogadas = 10
        self.qtd_jogadas = 0
        self.nome_arquivo = 'save.txt'
        self.initTabuleiro()
        self.alocaFrota()
        self.save()

    def initTabuleiro(self):
        self.tabuleiro = [[0 for j in range(self.tam_tabuleiro)] for i in range(self.tam_tabuleiro)]

    def alocaFrota(self):
        i = 0
        while i < self.tam_frota:
            x = random.randint(0, 4)
            y = random.randint(0, 4)

            if self.tabuleiro[x][y] == 0:
                self.tabuleiro[x][y] = 1
                i += 1

    def mostraTabuleiro(self):
        return print(self.tabuleiro)

    def save(self):
        arq = open(self.nome_arquivo, 'w')

        tabuleiro = '[' + ', '.join([str(x) for x in self.tabuleiro]) + ']'

        arq.write(str(tabuleiro))
        arq.write(';')
        arq.write(str(self.qtd_jogadas))
        arq.close()

    def readSave(self):
        arq = open(self.nome_arquivo, 'r')
        save = arq.read()
        arq.close()
        save = save.split(';')
        self.tabuleiro = eval(save[0])
        self.qtd_jogadas = int(save[1])

teste = BatalhaNaval()
        
