nome = str(input('Digite seu nome:')).strip()
print('Analisando seu nome....')
print('Seu nome em Maiúscula é {}'.format(nome.upper()))
print('Seu nome em Minúsculo fica {}'.format(nome.lower()))
print('Seu nome sem espaço fica {} letras'.format(len(nome.replace(' ', ''))))#len(nome) - nome.count(' ')
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))








