from Entities.FieldManager import FieldManager
from Entities.Player import Player

class GameManager:
	__fieldSize = 5
	__chances = 10
	__player1 = None
	__player2 = None
	__turnPlayer = 1
	def __init__(self):
		self.__handleGame()
	def __handleGame(self):
		if self.__player1 is None or self.__player2 is None:
			self.__getFirstPlayer()
		else:
			self.__playTurn()
		self.__handleGame()

	def __showGameTitle(self):
		print('|||||||||||||||||||||')
		print('!!!!BATALHA NAVAL!!!!')
		print('|||||||||||||||||||||')
	def __getFirstPlayer(self):
		self.__showGameTitle()
		if (self.__player1 is None): 
			print("Qual o nome do jogador 1?")
			playerName = input("")
			self.__player1 = Player(playerName, self.__chances)
			self.__player1.setField(FieldManager(self.__fieldSize))
		elif(self.__player2 is None):
			print("Qual o nome do jogador 2?")
			playerName = input("")
			self.__player2 = Player(playerName, self.__chances)
			self.__player2.setField(FieldManager(self.__fieldSize))
	def __playTurn(self):
		self.__showGameTitle()
		print("Jogador "+str(self.__turnPlayer)+":")
		print("Informe um numero para coluna X(de 1 a "+ str(self.__chances)+")")
		x = playerName = input("")
		print("Informe um numero para coluna Y(de 1 a "+ str(self.__chances)+")")
		y = playerName = input("")
		if(self.__turnPlayer == 1):
			self.__player1.play(int(x),int(y))
			self.__turnPlayer = 2
		else:
			self.__player2.play(int(x),int(y))
			self.__turnPlayer = 1
		
