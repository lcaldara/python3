nome = str(input('Digite seu nome: '))
print('Seu nome em letras maiúsculas: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas: {}'.format(nome.lower()))
print('Seu nome tem {} letras sem contar os espaços.'.format(len(nome.strip())-nome.count(' ')))
pri = (nome.split())
print('Seu primeiro nome tem {} letras.'.format(len(pri[0])))
# ou print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
