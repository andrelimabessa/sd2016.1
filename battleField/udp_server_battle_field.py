import socket
from datetime import datetime
from acoes import Acoes

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000 #Porta que o Servidor esta
HOST = '' #Endereco Ip do Servidor

acoes = Acoes()

def server():
    #Abrindo uma porta UDP
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)
    while True:
        #recebi dados
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode(ENCODE)
        if int(text) == 1:
            print("Usuário deseja ver estado do jogo.")
            text = acoes.ler_jogo()
            print("Solicitação enviada.")
        elif int(text) == 2:
            print("Usuário deseja continuar jogo anterior.")
            resposta = acoes.continuar_jogo()
            if int(reposta) ==  1:
                text = resposta
        #elif int(text) == 3:
            #print(acao)
            #option = False#break
            #text = acao

        #print(address, text)
        #Envia resposta
        #text = "Your data was " + str(len(data)) + " bytes long."
        data = text.encode(ENCODE)
        sock.sendto(data, address)
    sock.close()
#