#protocolo_cliente.py

class ProtocoloCliente(object):

    def comeco_interacao(self,interacao):
        self.interacao = interacao
        if interacao["novo_jogo"] == 0:
            print("Escolha a opcao:")
            print("0 - Para sair da Interacao.")
            print("1 - Para Comecar um Novo Jogo.")
            self.resposta_usuario = input("Opcao Desejada: ")

            if int(self.resposta_usuario) == 1:
                self.interacao["comeco_interacao"] = 1
                self.interacao["novo_jogo"] = 1
            return self.interacao

def criar_tabuleiro(self, interacao):
  self.interacao = interacao
  if interacao["criar_tabuleiro"] == 1:
    print("Esta disponivel a criacao de um novo tabuleiro.")
    print("Escolha a opcao:")
    print("0 - Para nao criar o tabuleiro.")
    print("1 - Para enviar solicitacao de criacao de tabuleiro.")
    self.resposta_usuario = input("Opcao desejada: ")
    
    if int(self.resposta_usuario) == 1:
      self.interacao["criar_tabuleiro"] = 1
      self.interacao["novo_jogo"] = 2
    return self.interacao