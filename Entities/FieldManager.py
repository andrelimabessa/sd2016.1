class FieldManager:
	__field = []
	__size = 0
	def __init__(self, size):
		self.__size = size
		self.__creatField()

	def __creatField(self):
		self.__field = [['000000' for x in range(self.__size)] for x in range(self.__size)] 
		
	def getField(self):
		return self.__field
	
	def markCoords(self, x, y, newShip):
		fld = self.__field
		rtn = False;
		x = x-1
		y = y-1
		if (newShip):
			fld[x][y] = '#SHIP#'
		elif(fld[x][y] == '#SHIP#'):
			rtn = True
			fld[x][y] = '#HIT!#'
		else:
			fld[x][y] = '#MISS#'
		return rtn
	def printFieldAsText(self):
		text = ''
		fld = self.__field
		for i in range(len(fld)):
			text += "Line " + str(i+1)+': '
			for j in range(len(fld)):
				text += fld[i][j]+' , '
			print(text)
			text = ''
