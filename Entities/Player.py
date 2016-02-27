class Player:
	__name: ''
	__chances: 0
	def __init__(self, name, chances):
		self.__name = name
		self.__chances = chances
	
	def play(self):
		if (self.__chances>0)
			self.__chances--
		else
			print('theres no more availiable chances')
