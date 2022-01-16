'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
desenvolver o programa que calculará os reajustes.Faça um programa que recebe o salário de um colaborador e o
reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''
atual = float(input('Sálario atual: '))
print('Antigo sálario:R${}'.format(atual))
#adicionando as porcentagens
a1 = atual + (atual * 20 / 100)
a2 = atual + (atual * 15 / 100)
a3 = atual + (atual * 10 / 100)
a4 = atual + (atual * 5 / 100)
if atual == 280:
    prit('Percentual aumentado de 20%')
    print('Equivalente a R${}'.format(a1 - (atual + 20 // 100)))
    print('Atual salário R${}'.format(a1))
if atual > 280:
    if atual < 700:
        print('Percentual aumentado de 15%')
        print('Equivalente a R${}'.format(a2 - (atual - 15 // 100)))
        print('Atual salário R${}'.format(a2))
if atual >= 700:
    if atual <= 1500:
        print('Percentual aumentado de 10%')
        print('Equivalente a R${}'.format(a3 - (atual - 10 // 100)))
        print('Atual salário R${}'.format(a3))
if atual > 1500:
    print('Percentual aumentado de 5%')
    print('Equivalente a R${}'.format(a4 - (atual - 5 // 100)))
    print('Atual salário R${}'.format(a4))





