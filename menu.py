from jogo import BatalhaNaval

class Menu(object):

    def exibeMenu(self):
        print("=============================================\n")
        print("=      Bem vindo ao Jogo Batalha Naval!     =\n")
        print("=============================================\n")
        print("O que deseja fazer?\n")
        print("1 - Novo Jogo.")
        print("2 - Continuar Jogo Salvo.")
        print("3 - Informar Jogada")
        print("4 - Imprimir Tabuleiro")

        opcao = input('\n')

        map_comand = {}
        map_comand["opcao"] = opcao

        if opcao == "1":
            print("Defina o tamanho do tabuleiro de 5 a 10:")
            tamanho_tabuleiro = input("Valor: \n")
            print("Deseja inserir os navios(S - Sim; N - Não)?")
            inserir_navios = input("Resposta: \n")
            map_comand["tamanho_tabuleiro"] = tamanho_tabuleiro
            map_comand["inserir_navios"] = inserir_navios
            #map_comand["naviosInseridos"] = "sim"
            print("Dados recebidos com sucesso. Enviando Requisição para o servidor...")

        if opcao == "3":
            posX = input("Informe Linha:\n")
            posY = input("Informe Coluna:\n")
            mapComand["posX"] = posX
            mapComand["posY"] = posY

        if opcao == "4":
            print("Solicitação de visualização de tabuleiro aceita...")
        return str(map_comand)
