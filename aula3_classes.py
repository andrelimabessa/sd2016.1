campo_de_batalha = [[0 for j in range(5)] for i in range(5)]

def colocando_barcos(quant_barcos):
    for i in range(quant_barcos):
        for j in range(quant_barcos):
            campo_de_batalha[i][j] = 1

colocando_barcos(3)

for i in range(5):
    print(campo_de_batalha[i])
