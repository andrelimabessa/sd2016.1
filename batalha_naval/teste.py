import ast
from _ast import *

opcao = "[1,2,3,4]"
teste = "teste"

coisa = compile(teste, '<unknow>', 'exec', PyCF_ONLY_AST)

print(type(ast.literal_eval(opcao)))
print(coisa)
print(repr(coisa))

input()