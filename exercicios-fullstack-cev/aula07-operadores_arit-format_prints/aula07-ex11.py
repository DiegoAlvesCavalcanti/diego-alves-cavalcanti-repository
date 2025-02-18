l = float(input('Digite a lagura da parede (m): '))
h = float(input('Digite a altura da parede (m): '))
a = l * h
t = a / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(l, h, a))
print('Para pintar essa parede, você presará de {} de tinta.'.format(t))
