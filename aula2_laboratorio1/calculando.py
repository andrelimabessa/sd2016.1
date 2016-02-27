#calculando.py

from calculadora2 import Calculadora

c = Calculadora()

print("Soma = %d, Subtração = %d, Multiplicação = %d, Divisão = %f"%(c.soma(2, 3), c.subtrai(2, 10), c.multiplica(3, 3), c.divide(128, 2)))
