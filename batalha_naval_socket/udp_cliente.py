import socket
from datetime import datetime
import menus

ENCODE = "UTF-8"
HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000          # Porta que o Servidor esta
MAX_BYTES = 65535

def client():
    """ Procedimento responsável por enviar dados para o servidor e receber alguma resposta por conta disso """
    #Enviod de dados
    while True:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dest = (HOST, PORT)

        text = menus.menu_inicial()
        enviar_text(text, sock, dest)

        #data = text.encode(ENCODE)
        #sock.sendto(data, dest)
        #Resposta de envio ao servidor
        #print(sock.getsockname())
        #data, address = sock.recvfrom(MAX_BYTES)  # Danger! See Chapter 2
        #text = data.decode(ENCODE)
        address, text = tratar_respota(sock)
        print(address, text)

        #text = tratar_reposta(text)
def enviar_text(text, sock, dest):
    #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #dest = (HOST, PORT)
    data = text.encode(ENCODE)
    sock.sendto(data, dest)

def tratar_respota(sock):
    data, address = sock.recvfrom(MAX_BYTES)  # Danger! See Chapter 2
    text = data.decode(ENCODE)
    return (address, text)