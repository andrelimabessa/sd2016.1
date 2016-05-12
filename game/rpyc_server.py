import rpyc
from datetime import datetime

from tabuleiro import Tabuleiro

class MyService(rpyc.Service):

    def exposed_new_game(self):
            tabuleiro = Tabuleiro(5)
            tabuleiro.preencher(5, 3)

            print('### Jogo Criado ####')

    def exposed_print_name(self, nome, sobrenome):
        return nome + " " + sobrenome

def server():
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port = 18861)
    t.start()
