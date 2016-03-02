class Player:
	__name = ''
	__chances = 0
	__field = None
	def __init__(self, name, chances):
		self.__name = name
		self.__chances = chances
	
	def play(self):
		if self.__chances>0:
			self.__chances = self.__chances-1;
		else:
			print('theres no more availiable chances')
	def setField(self, field):
		if self.__field is None:
			self.__field = field
	def play(self, x, y):
		self.__field.markCoords(x,y,False)
		self.__field.printFieldAsText()