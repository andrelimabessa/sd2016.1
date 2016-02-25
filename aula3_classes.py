import random

campo_de_batalha = [[0 for j in range(5)] for i in range(5)]

for i in campo_de_batalha:
    for j in i:
        marca = random.randint(0,1)
        print(marca)
        if marca == 1:
            i[j] = 1
print(campo_de_batalha)
