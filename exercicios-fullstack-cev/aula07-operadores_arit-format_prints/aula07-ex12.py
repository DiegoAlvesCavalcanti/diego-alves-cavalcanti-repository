preco = float(input('Qual é o preço do produto? R$'))
porcentagem = (5 / 100) * preco
preco_final = preco - porcentagem
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, preco_final))
