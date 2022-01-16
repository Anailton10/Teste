dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos km percorrido? '))
r = dia * 60 + km * 0.15
print('O total a ser pago é de R${}'.format(r))

