nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {}!'.format(nome)) # Msg normal
print('Prazer em te conhecer {:20}!'.format(nome)) # Faz a var nome ocupar 20 caracteres
"""
{:>20} -> Faz a string alinhar-se a direita dos 20 caracteres
{:<20} -> Faz a string alinhar-se a esquerda dos 20 caracteres
{:^20} -> Faz a string alinhar-se no centro dos 20 caracteres
"""
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
"""
{:=^20} -> Preenche os espaços em branco com algum caractere
"""
print('Prazer em te conhecer {:=^20}!'.format(nome))