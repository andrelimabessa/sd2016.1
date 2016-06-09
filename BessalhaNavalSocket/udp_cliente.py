import socket
from datetime import datetime
from index import Index
from bessalha_naval import Bessalha_Naval
import ast

ENCODE = "UTF-8"
HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000          # Porta que o Servidor esta
MAX_BYTES = 65535

def client():

    exibe = Index()
    """ Procedimento responsável por enviar dados para o servidor e receber alguma resposta por conta disso """
    qt_Tiros = 1
    BarcosAbatidos = 0
    deveContinuar = True
    while (deveContinuar):
        #Enviod de dados
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dest = (HOST, PORT)
        text = exibe.valorJogada(qt_Tiros)
        data = text.encode(ENCODE)
        sock.sendto(data, dest)

        #Resposta de envio ao servidor
        #print(sock.getsockname())
        data, address = sock.recvfrom(MAX_BYTES)  # Danger! See Chapter 2
        text = data.decode(ENCODE)
        batalha = Bessalha_Naval()
        map = ast.literal_eval(text)
        J1 = map["J1"]
        J2 = map["J2"]

        if (J1 == 1):
            BarcosAbatidos += 1
            qt_Tiros += 1
        else:
            qt_Tiros += 1

        print(J2)

        if (BarcosAbatidos == 2):
            deveContinuar = False
            print ("Ganhou Mizerávi !!!")
        
        elif (qt_Tiros >= 6):
            deveContinuar = False
            print ("Perdeu! Pior é na guerra.")
        
