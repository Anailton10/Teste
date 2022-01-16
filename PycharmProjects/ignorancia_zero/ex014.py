'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
'''
horas = float(input('Horas trabalhadas: '))
valor = float(input('Valor por hora: '))
salario_bruto = horas * valor
print('Salário Bruto:({:.0f}*{:.0f})   :R${:.0f}'.format(horas, valor, salario_bruto))
#Os descontos do Imposto (%)
ir5 = salario_bruto * 0.05
ir10 = salario_bruto * 0.10
ir20 = salario_bruto * 0.20
#O desconto do INSS (%)
inss = salario_bruto * 0.03
#O desconto do FGTS
fgts = salario_bruto * 0.11
#Total de desconto
total1 = salario_bruto - (salario_bruto - inss)
total2 = salario_bruto - (salario_bruto - ir5 - inss)
total3 = salario_bruto - (salario_bruto - ir10 - inss)
total4 = salario_bruto - (salario_bruto - ir20 - inss)
#As condições
if salario_bruto <= 900:
    print('(-) IR (0%)             :R${}'.format(10*0))
    print('(-) INSS (3%)           :R${}'.format(inss))
    print('FGTS (11%)              :R${}'.format(fgts))
    print('Total de desconto       :R${}'.format(total1))
    print('Salário Liquido         :R${:.0f}'.format(salario_bruto - total1))
if salario_bruto <= 1500:
    if salario_bruto > 900:
        print('(-) IR (5%)             :R${}'.format(ir5))
        print('(-) INSS (3%)           :R${}'.format(inss))
        print('FGTS (11%)              :R${}'.format(fgts))
        print('Total de desconto       :R${}'.format(total2))
        print('Salário Liquido         :R${:.0f}'.format(salario_bruto - total2))
if salario_bruto <= 2500:
    if salario_bruto > 1500:
        print('(-) IR (10%)            :R${}'.format(ir10))
        print('(-) INSS (3%)           :R${}'.format(inss))
        print('FGTS (11%)              :R${}'.format(fgts))
        print('Total de desconto       :R${}'.format(total3))
        print('Salário Liquido         :R${:.0f}'.format(salario_bruto - total3))
if salario_bruto > 2500:
    print('(-) IR (20%)            :R${}'.format(ir20))
    print('(-) INSS (3%)           :R${}'.format(inss))
    print('FGTS (11%)              :R${}'.format(fgts))
    print('Total de desconto       :R${}'.format(total4))
    print('Salário Liquido         :R${:.0f}'.format(salario_bruto - total4))








