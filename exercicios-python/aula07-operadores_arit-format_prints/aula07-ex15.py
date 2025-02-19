dias = int(input('Quantos dias alugados? '))
quilometros = float(input('Quantos Km rodados? '))
preco_dias = dias * 60
preco_quilometros = quilometros * 0.15
preco_total = preco_dias + preco_quilometros
print('O total a pagar é de R${:.2f}'.format(preco_total))