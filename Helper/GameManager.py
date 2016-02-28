from Entities.FieldManager import FieldManager
from Entities.Player import Player

class GameManager:
	__fieldSize = 5
	__chances = 10
	__player1 = None
	__player2 = None
	__field = None
	def __init__(self):
		self.__handleGame()
	def __handleGame(self):
		if self.__field is None:
			__field = FieldManager(self.__fieldSize)	
		if self.__player1 is None:
			self.__getFirstPlayer()	
		if self.__player2 is None:
			 self.__getSecondPlayer()
		

	def __showGameTitle(self):
		print('!!!!BATALHA NAVAL!!!!')
	def __getFirstPlayer(self):
		self.__showGameTitle()
		print("Qual o nome do jogador 1?")
		playerName = input("")
		self.__player1 = Player(playerName, self.__chances)
	def __getSecondPlayer(self):
		self.__showGameTitle()
		print("Qual o nome do jogador 2?")
		playerName = input("")
		self.__player2 = Player(playerName, self.__chances)
