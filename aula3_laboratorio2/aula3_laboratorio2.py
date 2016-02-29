#aula3_laboratorio2.py
#arq = open("texto.txt",'w')

#arq.write("linha1\n")
#arq.write("linha2\n")
#arq.close()

arq = open("texto.txt","r")

print(arq.readline())
for linha in arq:
	print(linha)

arq.close()