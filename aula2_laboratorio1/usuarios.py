#usuarios.py
from user import User

class Usuarios(object):
	u1 = User("Miguel", 4)
	u2 = User("Camila", 22)

	u1.save()
	u2.save()

	print(User.all())