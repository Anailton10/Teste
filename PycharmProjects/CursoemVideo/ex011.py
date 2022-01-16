produto = float(input('Qual o preço do produto? R$'))
desconto = float(input('Quantos porcento é o desconto? '))
r = produto - (produto * (desconto / 100))
print('O produto custava {}. \nNa promoção com o desconto de {}% vai custar R${:.2f}'.format(produto, desconto, r))

