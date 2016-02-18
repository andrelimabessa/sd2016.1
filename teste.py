arq = open("ad.txt", "r")
print(arq.readline())
for linha in arq:
	print(linha)
arq.close()