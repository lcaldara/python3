c = 0
cond = ' '
s = 0
maior = 0
menor = 0
while cond != 'S':
    c = c + 1
    n = int(input('Digite o {}º número: '.format(c)))
    s = s + n
    cond = str(input('Deseja sair do programa? [S/N] ')).upper()[0]
    if c == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print('''Média: {}
Maior: {}
Menor: {}'''.format(s/c, maior, menor))
