import socket

from datetime import datetime

from acoes import Acoes

from play_battle_field import game

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000 #Porta que o Servidor esta
HOST = '' #Endereco Ip do Servidor

acoes = Acoes()
game = game()

def server():
    #Abrindo uma porta UDP
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)
    while True:
        #recebi dados
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode(ENCODE)
        if int(text[0]) == 1:
            print("Usuario deseja ver estado do jogo.")
            text = acoes.ler_jogo()
            print("Resposta enviada.")
        elif int(text[0]) == 2:
            print("Usuario deseja continuar jogo anterior.")
            resposta = acoes.continuar_jogo()
            if int(resposta) ==  1:
                text = str(resposta)
                print("Resposta enviada.")
        elif int(text[0]) == 3:
            if int(text[2]) == 1:
                print("Usuario deseja iniciar novo jogo.")
                text = "1 - Diga o Nome do Jogador. O tamanho do tabuleiro e a quantidade de Navios"
            elif int(text[2]) == 2:
                text = "teste!!!!!!"
        data = text.encode(ENCODE)
        sock.sendto(data, address)
    sock.close()
#