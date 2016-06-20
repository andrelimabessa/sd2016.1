import socket
from datetime import datetime

ENCODE = "UTF-8"
HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000          # Porta que o Servidor esta
MAX_BYTES = 65535

CRIAR_JOGO = '1'
JOGADA = '2'
SAIR = '3'
map = {}

def client():
    
    #Enviod de dados
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (HOST, PORT)

    while True:
    
        print("1 - Iniciar Jogo")
        print("2 - Jogada")
        print("3 - Sair")
    
        text = input("Digite o numero correspondente a opcao desejada:\n")
        print("Opcao Escolhida" + str(text))
        if str(text) == CRIAR_JOGO:
            map['tamanho_tabuleiro'] = input("Qual o tamanho do tabuleiro:\n")
            map['quantidade_navios'] = input("Quantos navios deseja:\n")
            quantidade_jogadas = int(map['quantidade_navios'])
        elif str(text) == JOGADA and quantidade_jogadas != 0:
            map['linha'] = input("Qual a linha:\n")
            map['coluna'] = input("Quantos a coluna:\n")
            quantidade_jogadas = quantidade_jogadas - 1
            print("Restam " + str(quantidade_jogadas) + " jogadas")
        elif str(text) == SAIR:
            exit()
        elif quantidade_jogadas == 0:
            print("GAME OVER")
            exit()

        
        map['opcaoMenu'] = text
    
        data = str(map).encode(ENCODE)
        #print(data)
        sock.sendto(data, dest)
    
        #Resposta de envio ao servidor
        print(sock.getsockname())
        data, address = sock.recvfrom(MAX_BYTES)  # Danger! See Chapter 2
        text = data.decode(ENCODE)
        print(text)