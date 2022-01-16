parede = float(input('Largura da parede:'))
altura = float(input('Altura da parede:'))
area = parede * altura
print('Com as medidas de {:.0f} x {:.0f}, você tem {:.1f}m²'.format(parede, altura, area))
tinta = area / 2
print('Com {:.1f}m², você vai precisar de {:.1f} litros de tinta'.format(area, tinta))
