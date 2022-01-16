'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''
turno = str(input('Qual tudo estuda? '))
#print('M - Matutino \nV - Vespertino \nN - Noturno')
if turno == 'm':
    print('Bom Dia!!')
if turno == 't':
    print('Boa Tarde!!')
if turno == 'n':
    print('Boa Noite!!')
else:
    print('Valor Invalido!!')

