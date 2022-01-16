import random
#lista = ['Maria', 'João', 'José', 'Carmen']
#print('O aluno a pagar a lousa é: {}'.format(random.choice(lista)))
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

