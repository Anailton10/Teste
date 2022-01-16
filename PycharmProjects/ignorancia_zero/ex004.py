valor = float(input('Quanto você ganha por hora?'))
horas = float(input('Quantas horas você trabalhou no mês?'))
salario = valor * horas
print('Muito bem, sua hora é R${}. \nNo mês você trabalhou {} horas \nSeu salário vair ser R${:.1f}'.format(valor, horas, salario))
