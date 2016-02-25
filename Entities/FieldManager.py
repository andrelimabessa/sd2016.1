class FieldManager:
	__field = []
	__size = 0
	def __init__(self, size):
		self.__size = size
		self.__creatField()

	def __creatField(self):
		self.__field = [[0 for x in range(self.__size-1)] for x in range(self.__size-1)] 
		
	def getField(self):
		return self.__field
	
	def markCoords(self, x, y, newShip):
		fld = self.__field
		rtn = false;
		if (newShip):
			fld[x][y] = '#SHIP#'
		elif(fld[x][y] == '#SHIP#'):
			rtn = true
			fld[x][y] = '#HIT#'
		else:
			fld[x][y] = '#MISS#'
		
