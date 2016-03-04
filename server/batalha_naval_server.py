import random

class BatalhaNavalServer(object):
    def __init__(self, tipo):
        self.nome_arquivo = 'save.txt'
        self.max_jogadas = 10

        if tipo == 1:
            self.readSave()
        else:
            self.novoJogo()
        
    def novoJogo(self):
        self.tam_tabuleiro = 5
        self.qtd_jogadas = 0
        self.tam_frota = 7
        self.initTabuleiro()
        self.alocaFrota()

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

    def atirar(self, posicao):
        if self.tabuleiro[posicao[0]][posicao[1]] == 1:
            result_ataque = "Navio abatido!"
            self.tabuleiro[posicao[0]][posicao[1]] = 'X'
        elif self.tabuleiro[posicao[0]][posicao[1]] == 'X':
            result_ataque = "Navio já abatido! Ataque em outro local!"
        else:
            result_ataque = "Água!"

        return result_ataque

    def save(self):
        tabuleiro = '[' + ', '.join([str(x) for x in self.tabuleiro]) + ']'
        
        arq = open(self.nome_arquivo, 'w')
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

teste = BatalhaNavalServer(1)
        
