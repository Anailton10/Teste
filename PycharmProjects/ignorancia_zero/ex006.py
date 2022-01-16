'''O programa deverá pedir tamanho em m² a ser pintada, a cobertura da tinta é de 1 litro para
cada 3 m², e que a tinta é vendida em lata de 18 litros a R$80, informe o usuario a quantidade de latas de tintas
e o total da compra'''
area = float(input('Digite a área a ser pintada em m²: '))
litros = area // 3
if litros % 3 > 0:
    litros = litros + 1
lata = litros // 18
if lata % 18 > 0:
    lata = lata + 1
print('Você precisará de {:.0f} latas de tinta. \nVocê pagará R${:.0f}.'.format(lata, lata * 80))




