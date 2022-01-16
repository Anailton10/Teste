'''Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou
em galões de 4 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 4 litros;
    misturar latas e galões, de forma que o preço seja o menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
considere latas cheias'''
area = float(input('Digite a area a ser pintada:'))
area = area * 1.1
excesso = area - int(area)
area = int(area)
if excesso > 0:
    area = area + 1

litro = area // 6
if area > 0:
    litro = litro + 1
print('Litros nescessario:{}\n'.format(litro))

lata = litro // 18
if litro % 18 > 0:
    lata = lata + 1
valor_lata = lata * 80

print('1- Comprar apenas latas de 18 litros')
print('Latas nescessaria:{}'.format(lata))
print('Teremos {} litros'.format(lata * 18))
print('Irá custar R${}\n'.format(valor_lata))

galão = litro // 4
if litro % 4 > 0:
    galão = galão + 1
valor_galão = galão * 25

print('2- Comprar apenas galões de 4 litros')
print('Galão nescessario:{}'.format(galão))
print('Teremos {} litros'.format(galão * 4))
print('Irá custar R${}\n'.format(valor_galão))

print('3-Misturar latas e galõess de forma que o preço seja menor.')
lata = litro //18
galão = 0
litro_restante = litro % 18
if litro_restante < 3 * 4:
    galão = litro_restante // 4
    if litro_restante % 4 > 0:
        galão = galão + 1
else:
    lata = lata + 1
print('Serão necessárias {} latas'.format(lata))
print('Serão necessárias {} galoes'.format(galão))
print('Oteremos {} litros'.format(lata * 18 + galão * 4))
print('Total: R${}'.format(valor_galão + valor_lata))






