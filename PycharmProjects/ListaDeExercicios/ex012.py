km = float(input('Digite o Km percorrido:'))
dia = float(input('Dias alugados:'))
t = ((dia * 90) + (km * 0.20))
print('Percorreu {}km durante {} dias, o cliente irá pagá R${}'.format(km, dia, t))

