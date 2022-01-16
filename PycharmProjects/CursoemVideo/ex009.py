carteira = float(input('Digite quanto você tem:R$'))
dolar = carteira / 5.19
euro = carteira / 6.17
can = carteira / 4.14
print('-' * 50)
print('Com R${:.2f} você pode comprar US${:.2f}'.format(carteira, dolar))
print('Com R${:.2f} você pode comprar ER${:.2f}'.format(carteira, euro))
print('Com R${:.2f} vocÊ pode comprar CA${:.2f}'.format(carteira, can))
print('-' * 50)

