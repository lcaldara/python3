vlrt = maismil = c = menor = 0
menornome = ' '
while True:
    c = c + 1
    nome = str(input('Digite o nome do produto: '))
    vlr = int(input('Digite o valor do produto: '))
    cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while cont not in 'SN':
        cont = str(input('Digite uma opção válida [S/N] ')).upper().strip()[0]
    vlrt = vlrt + vlr
    if vlr > 1000:
        maismil += 1
    if c == 1:
        menor = vlr
        menornome = nome
    if vlr < menor:
        menor = vlr
        menornome = nome
    if cont == 'N':
        break
print(f'O total gasto na compra foi de {vlrt}.')
print(f'{maismil} produtos custam mais de R$ 1.000.')
print(f'O nome do produto mais barato é {menornome} e custou {menor}')
