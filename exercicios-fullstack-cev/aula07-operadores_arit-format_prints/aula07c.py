# Formatação do print
"""
\n -> Quebrar linha
end='  ' -> Não quebrar linha

{:.3f} -> Formata a variável para 3 casas decimais float
"""

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' >>> ')
print('Divisão inteira {} e potência {}'.format(di, e))
