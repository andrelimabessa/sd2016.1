#protocolo_cliente.py

class ProtocoloCliente(object):

    def comeco_interacao(self,interacao):
        self.interacao = interacao
        if interacao["novo_jogo"] == 0:
            print("Escolha a opção:")
            print("0 - Para sair da Interação.")
            print("1 - Para Começar um Novo Jogo.")
            self.resposta_usuario = input("Opção Desejada: ")

            if int(self.resposta_usuario) == 1:
                self.interacao["comeco_interacao"] = 1
                self.interacao["novo_jogo"] = 1
            return self.interacao