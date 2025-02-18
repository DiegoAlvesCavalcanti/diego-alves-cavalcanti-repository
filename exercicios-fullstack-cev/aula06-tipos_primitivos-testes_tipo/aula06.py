# Tipos Primitivos Básicos

"""
-> int : 7, -4, 0, 9875
-> float : 4.5, 0.076, -15.223, 7.0
-> bool : True, False
-> str : 'Olá', '7.5', ' '
"""


""" Prática 1

n1 = int(input('Digite um valor: '))        # int() -> faz com que o valor de entrada seja INTEIRO (int)
n2 = int(input('Digite outro valor: '))     # int() -> faz com que o valor de entrada seja INTEIRO (int)
s = n1 + n2
print('A soma entre {} e {} vale {}'.format(n1, n2, s))     # Concatenação com .format()

print('n1 ->', type(n1))    # type() -> faz com que seja possivel visualizar o tipo primitivo da variável
print('n2 ->', type(n2))    # type() -> faz com que seja possivel visualizar o tipo primitivo da variável
print('s ->', type(s))    # type() -> faz com que seja possivel visualizar o tipo primitivo da variável
"""

""" Prática 2

n = input('Digite algo: ')
print(n.isnumeric())    # n.isnumeric() -> Testa se o valor da variável é numérico
print(n.isalpha())      # n.isalpha() -> Testa se o valor davariável é alfabético
print(n.isalnum())      # n.isalnum() -> Testa se o valor davariável é alfanumérico
print(n.isupper())      # n.isupper() -> Testa se o valor davariável tem somente letras maiúsculas
"""
