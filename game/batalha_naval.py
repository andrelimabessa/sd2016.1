from random import randint
class Batalha_naval(object):
	"""docstring for Batalha_naval"""
	def __init__(self, matrix):
		super(Batalha_naval, self).__init__()
		matrix =  [ [ 0 for j in range(5) ] for i in range(5)]
		self.matrix = matrix
		print(matrix)
		for n in range(25):
			pointi = randint(0,4)
			pointj = randint(0,4)
			matrix[pointi][pointj]=1
		while 1:	
			x = int (input("Digite  o numero para x: "))	
			y = int (input("Digite  o numero para y: "))	

			if matrix[x][y]==1:
				print("parabéns")
			else:
				print("agua")	
				print(matrix)			