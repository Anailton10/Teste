'''import math''' # importando_todo_modulo_math
from math import hypot #importando apenas um função do modulo
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('O valor da hipotenusa é {:.2f}'.format(hi))
