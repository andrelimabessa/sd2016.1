class Manager_File(object):
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.carregaInfo()

    def carregaInfo(self):
        try:
            arq = open(self.nome_arquivo, 'r')
        except FileNotFoundError:
            arq = open(self.nome_arquivo, 'w')

            arq.write("tam_tabuleiro=5\n")
            arq.write("frota=[[0, 3], [2, 4], [4, 2]]\n")
            arq.write("jogadas=5\n")
            arq.close()

        for linha in arq:
            aux = linha.split('=')
            if aux[0] == 'tam_tabuleiro':
                self.tam_tabuleiro = aux[-1]
            elif aux[0] == 'frota':
                self.frota = aux[-1]
            elif aux[0] == 'max_jogadas':
                self.max_jogadas = aux[-1]