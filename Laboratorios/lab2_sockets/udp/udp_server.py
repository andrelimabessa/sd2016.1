import socket
import ast
from datetime import datetime
from batlefield import Batle_Field

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000            # Porta que o Servidor esta
HOST = ''     # Endereco IP do Servidor
CRIAR_JOGO = '1'
JOGADA = '2'
SAIR = '3'

def server():
    #Abrindo uma porta UDP
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)
    while True:
        #recebi dados
        data, address = sock.recvfrom(MAX_BYTES)
        map = ast.literal_eval(data.decode(ENCODE))
        #print(map)

        opcaoMenu = map['opcaoMenu']
        quantidade_navios = map['quantidade_navios']
        tamanho_tabuleiro = map['tamanho_tabuleiro']

        print(str(opcaoMenu) + " " + CRIAR_JOGO)
    
        if str(opcaoMenu) == CRIAR_JOGO:
            print("Criar novo jogo")
            jogo = Batle_Field(tamanho_tabuleiro)
            text = str(jogo.preencher(tamanho_tabuleiro,quantidade_navios))
        elif str(opcaoMenu) == JOGADA:
            print("Nova jogada")
            linha = map['linha']
            coluna = map['coluna']
            status_jogada = jogo.jogar(linha,coluna)
            if status_jogada == True:
                text = 'Acertou jogada'
            else:
                text = 'Errou jogada'

            
        #print(address, text)
        #Envia resposta
        data = text.encode(ENCODE)
        sock.sendto(data, address)
    sock.close()