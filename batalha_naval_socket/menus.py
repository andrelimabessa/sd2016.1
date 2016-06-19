# -*- coding: utf-8 -*-

def menu_inicial():
    print("Escolha a opção: ")
    print("1 - Novo Jogo.")

    opcao = input("Opção: \n")

    if opcao == 1:
        print("### Iniciando Jogo ###")
    else:
        print("Opção inválida.")

    return opcao

def opening_game():
    print("\n")

    print("### JOGADOR ###")
    name = (raw_input("NOME: : \n"))

    print("### TABULEIRO ###")

    columns = input("LINHAS:  \n")
    rows = input("COLUNAS: \n")

    return '__create_player__,' + name + ',' + str(rows) + ',' + str(columns)

def actions_game():
    print("Escolha o que deseja fazer: ")
    print("1 - Distribuir")
    print("2 - Jogar")
    print("3 - Visualizar")
    print("4 - Salvar")

    return str(input("Opção: \n"))