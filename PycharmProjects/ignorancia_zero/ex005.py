#faça um programa que leia dois numeros e que imprima o maior deles.
n1 = int(input('Digite um numero:'))
n2 = int(input('Dgite outro numero: '))
if n1 > n2:
    print('{} é maior que {}'.format(n1, n2))
else:
    print('{} é menor que {}'.format(n1, n2))
