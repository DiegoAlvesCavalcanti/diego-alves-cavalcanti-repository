n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('Analisando o valor {}, seu antecessor é {} e o seu sucessor é {}.'.format(n, a, s))

n = int(input('Digite outro número: '))
print('Analisando o valor {}, seu antecessor é {} e o seu sucessor é {}.'.format(n, (n-1), (n+1)))