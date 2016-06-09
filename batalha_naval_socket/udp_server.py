import socket
from datetime import datetime

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000            # Porta que o Servidor esta
HOST = ''     # Endereco IP do Servidor

def server():
    #Abrindo uma porta UDP
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)
    while True:
        #recebi dados
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode(ENCODE)
        print(address, text)
        tratar_requisicao(text)
        #Envia resposta
        text = "Your data was " + str(len(data)) + " bytes long"
        data = text.encode(ENCODE)
        sock.sendto(data, address)
    sock.close()

def tratar_requisicao(text):
    if text == "1":
        return input("Testando:")
