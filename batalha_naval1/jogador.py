#jogador.py

class Jogador(object):

    def __init__(self, nome_jogador):
        self.nome_jogador = nome_jogador
        print("Nome do Jogador Criado!!!")

    def get_nome_jogador(self):
        return self.nome_jogador