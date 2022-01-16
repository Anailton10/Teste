salario = float(input('Salário atual:'))
aumento = float(input('Qunatos porcento de aumento?'))
sal = salario + (salario * (aumento / 100))
print('Um funcionário que ganhava R${} \ncom um aumento de {}% \npassa a receber R${:.2f}.'.format(salario, aumento, sal))
