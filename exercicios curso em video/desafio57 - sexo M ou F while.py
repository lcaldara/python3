#sexo = ' '
#fem = 0
#masc = 0
#while sexo != 'P':
#    sexo = str(input('Digite o sexo: [P para ENCERRAR] ')).upper()
#    if sexo == 'F':
#        fem = fem + 1
#    elif sexo == 'M':
#        masc = masc + 1
#    else:
#        print('Digite o sexo correto [M/F]')
#print(fem)
#print(masc)

sexo = str(input('Informe o sexo: [M/F]')).upper()[0]
while sexo not in 'MF':
    sexo = str(input('Informe um sexo válido: [M/F]')).upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
