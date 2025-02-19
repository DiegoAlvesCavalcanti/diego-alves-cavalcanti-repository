"""
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é igual a {:.2f}'.format(num, raiz))
print('A raiz quadrada de {} é igual a {}'.format(num, math.ceil(raiz)))
print('A raiz quadrada de {} é igual a {}'.format(num, math.floor(raiz)))
print('A raiz quadrada de {} é igual a {}'.format(num, math.trunc(raiz)))
"""

"""
from math import sqrt, ceil, floor, trunc # <- A partir do momento em que é feito a importação assim, o método é trazido diretamente para a sua pasta não precisando utilizar a referência math.funcionalidade
num2 = int(input('Digite um número: '))
raiz2 = sqrt(num2)
print('A raiz quadrada de {} é igual a {:.2f}'.format(num2, raiz2))
print('A raiz quadrada de {} é igual a {}'.format(num2, ceil(raiz2))) # <- Não precisa de mat.funcionalidade
print('A raiz quadrada de {} é igual a {}'.format(num2, floor(raiz2))) # <- Não precisa de mat.funcionalidade
print('A raiz quadrada de {} é igual a {}'.format(num2, trunc(raiz2))) # <- Não precisa de mat.funcionalidade
"""

import random
num = random.random() # <- Randomiza um número de 0 a 1
num2 = random.randint(1, 10) # <- Ramdomiza um número inteiro de 1 a 10 
print(num)
print(num2)