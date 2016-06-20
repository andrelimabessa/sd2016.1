print("1 - Iniciar Jogo")
print("2 - Sair")

opcao = input("Digite o numero correspondente a opcao desejada")

if int(opcao)==1:
    from hello import Hello

    h = Hello()

    h.jogo()
else:
    exit()


