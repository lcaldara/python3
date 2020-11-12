contid = conth = contm20 = 0
cont = ' '
while True:
    id = int(input('Digite a idade: '))
    sx = str(input('Digite o sexo: [M/F] ')).upper().strip()[0]
    while sx not in 'MF':
        sx = str(input('Escolha um sexo válido [M/F]: ')).upper().strip()[0]
    cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while cont not in 'SN':
        cont = str(input('Digite uma opção válida [S/N]: ')).upper().strip()[0]
    if id >= 18:
        contid += 1
    if sx == 'M':
        conth += 1
    if id < 20 and sx == 'F':
        contm20 += 1
    if cont == 'N':
        break
print(f'{contid} pessoas tem mais de 18 anos.')
print(f'{conth} homens foram cadastrados.')
print(f'{contm20} mulheres tem menos de 20 anos.')
