import socket
from datetime import datetime
from bessalha_naval import Bessalha_Naval
import ast

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000            # Porta que o Servidor esta
HOST = ''     # Endereco IP do Servidor

def server():
    #Abrindo uma porta UDP
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)
    batalha = None
    while True:
        #recebi dados
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode(ENCODE)

        map = ast.literal_eval(text)
        print(address, text)
        if batalha is None:
            batalha = Bessalha_Naval()
            batalha.barquinhos()

        text = batalha.tiro(map["X"], map["Y"])
        #Envia resposta
        #text = "Your data was " + str(len(data)) + " bytes long"
        data = text.encode(ENCODE)
        sock.sendto(data, address)
    sock.close()
