class Menu(object):

    def exibeMenu(self):
        print("=============================================\n")
        print("=      Bem vindo ao Jogo Batalha Naval!     =\n")
        print("=============================================\n")
        print("O que deseja fazer?\n")
        print("1 - Novo Jogo.")
        print("2 - Continuar Jogo Salvo.")
        print("3 - Informar Jogada")

        opcao = input('\n')

        mapComand = {}
        mapComand["opcao"] = opcao
        if opcao == "3":
            posX = input("Informe Linha:\n")
            posY = input("Informe Coluna:\n")
            mapComand["posX"] = posX
            mapComand["posY"] = posY
        return str(mapComand)
