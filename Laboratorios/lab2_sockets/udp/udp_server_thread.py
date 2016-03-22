# -*- coding: utf-8 -*-

import socket
import threading#threads a nível de usuário
from datetime import datetime

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000            # Porta que o Servidor esta
HOST = ''     # Endereco IP do Servidor

""" Forma Procedural """
def server_thread():
    #Abrindo uma porta UDP
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)
    while True:
        #recebi dados
        data, address = sock.recvfrom(MAX_BYTES)
        # Criação de thread procedural
        #t = threading.Thread(target=tratar_conexao, args=tuple([sock, data, address]))
        #t.start()

        #Criação de thread orientada a objeto
        tratador = ThreadTratador(sock, data, address)
        tratador.start()
    sock.close()

def tratar_conexao(sock, data, address):
    text = data.decode(ENCODE)
    print(text)
    #Envia resposta
    text = "Your data was " + str(len(data)) + " bytes long"
    data = text.encode(ENCODE)
    sock.sendto(data, address)

""" Forma Orientado a objeto """
class ThreadTratador(threading.Thread):

    def __init__(self, a, b, c):
        threading.Thread.__init__(self)
        self.sock = a
        self.data = b
        self.address = c

    def run(self):

        tratar_conexao(self.sock, self.data, self.address)
