import sys
from udp_server_batalha_naval import server
from udp_cliente_batalha_naval import client

print("Você quer executar: ")
print("1 - para servidor.")
print("2 - para cliente.")
opcao = input("Opção: ")

try:
    if int(opcao) == 1:
        print("Servidor ativado:\n")
        server()
    elif int(opcao) == 2:
        print("Cliente ativado:\n")
        client()
except :
    for val in sys.exec_info():
        print(val)

input()