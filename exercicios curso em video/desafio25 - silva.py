nome = input('Digite seu nome: ')
#mai = nome.upper()
log = 'SILVA' in nome.upper()
#log = 'SILVA' in mai
if log is True:
    print('Seu nome contém Silva')
else:
    print('Seu nome não contém Silva')
#print('Seu nome contém Silva' if log is True else 'Seu nome não contém Silva')
