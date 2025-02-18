preco = float(input('Qual é o salário do Funcionário? R$'))
porcentagem = (15 / 100) * preco
preco_final = preco + porcentagem
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(preco, preco_final))