a = [1,2,3]

try:
	print(str(a[5]))
except (IndexError, TypeError):
	print("Posição inexistente no array!")
finally:
	print("Fim do teste de impressão de posições")