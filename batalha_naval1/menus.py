#__author__ = 'Christian'
#menus.py

def menu_inicial():
    print("Escolha a opção: ")
    print("1 - Novo Jogo.")
    print("2 - Continuar Jogo.")

    return input("Opção: \n")

def menu_novo_jogo_abertura():
    nome_jogador = (input("Digite o nome do jogador: \n"))
    print("Diga a quantidade de linhas do tabuleiro: ")
    qtd_linhas = input("Quantidade de Linhas: \n")
    print("Diga a quantidade de colunas do tabuleiro: ")
    qtd_colunas= input("Quantidade de Colunas: \n")

    return(nome_jogador, qtd_linhas, qtd_colunas)

def menu_novo_jogo():
    print("Escolha o que deseja fazer: ")
    print("1 - Distribuir Navios.")
    print("2 - Realizar Jogada.")
    print("3 - Ver estado do jogo.")
    print("4 - Salvar")
    print("5 - Sair.")
    print("6 - Imprimir Tabuleiro")

    return input("Opção: \n")