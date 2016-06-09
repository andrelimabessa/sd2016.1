from bessalha_naval import Bessalha_Naval



batalha = Bessalha_Naval()
batalha.checkSave()
batalha.barquinhos()

qt_Tiros = 1
BarcosAbatidos = 0
deveContinuar = True

while (deveContinuar):
	print ("%d Tiro: " %(qt_Tiros))
	print ("Informe a Coordenada X: ")
	X = input()
	print ("Informe a Coordenada Y: ")
	Y = input()
	jogada = batalha.tiro(X,Y)
	if (jogada):
		BarcosAbatidos += 1
		qt_Tiros += 1
		batalha.save(qt_Tiros)
	else:
		qt_Tiros += 1
	batalha.save(qt_Tiros)
	#batalha.mostrarTabuleiro()

	if (BarcosAbatidos == 2):
		deveContinuar = False
		batalha.save(qt_Tiros)
		print("Ganhou Mizerávi !!!")
	
	elif (qt_Tiros >= 6):
		deveContinuar = False
		print("Perdeu! Pior é na guerra.")
batalha.mostrarTabuleiro()

input()