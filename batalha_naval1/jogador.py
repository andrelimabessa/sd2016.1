#jogador.py

class Jogador(objrct):

    def __init__(self, nome_jogador):
        self.nome_jogador = nome_jogador

    def get_nome_jogador(self):
        return self.nome_jogador