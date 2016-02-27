num = 13

nome = "Nome"

hello = "Hello"

print(hello)

print(hello + "World")

print(hello * 3)

print(hello[0])

print(hello[-1])

print(len(hello))

print('e' in hello)

var = "Faculdade 7 de Setembro"

print(var[1:7])

print(var[1:7:2])

print(var[::-1])

print(var.split())

print(var.count("7"))

var2 = var.split()

print(var2)

print("/".join(var2))

tupla = ("Bom", "Dia")

lista = ["Boa", "Noite", ["Boa", "Tarde"], 2]

lista.append("texto")

#tupla.append("texto")

print(lista[1])

a = list(range(5))

print(a)

a.insert(0, 42)

print(a)

a.reverse()

print(a)

a.sort()

print(a)

a = {"pera":5, "laranja":1}

print(a["pera"])

a["banana"] = 3

print(a)

print(a.items())

nome = input("Digite alguma coisa: ")

print("Você digitou %s"%(nome))

def func(x):
	print(type(x))

func("nome")

x = 20

while x>10:
	print(x)
	x = x -1

for i in range(5):
	print(i)

for letra in "Miguel":
	print("Miguel")

pares = [i for i in range(100) if(i%2) == 0]
print(pares)
print(pares[::-1])

impares = [i for i in range(100) if(i % 2) != 0]
print(impares)
print(impares[::-1])

lista_zeros = [0 for i in range(10)]
print(lista_zeros)

matriz = [ [0 for j in range(3) for i in range(5)] ]
print(matriz)

def nome_sobrenome(nome, sobrenome):
	print(nome + " " + sobrenome)

nome = input("Digite um nome: ")
sobrenome = input("Digite o sobrenome: ")

nome_sobrenome(nome, sobrenome)