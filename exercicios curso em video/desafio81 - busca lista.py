lista = []
while True:
    lista.append(int(input('Insira um valor na lista: ')))
    cont = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    while cont not in 'SN':
        cont = str(input('Digite um valor válido [S/N]: ')).upper().strip()
    if cont == 'N':
        break
print(f'Foram digitados {len(lista)} valores.')
print(f'Lista: {lista}')
if lista.count(5) > 0:
    print('Existe um 5 nas posições: ', end='')
    for pos, num in enumerate(lista):
        if num == 5:
            print(pos, end=' ')
    print()
else:
    print('Não existem números 5 nesta lista.')
lista.sort()
print(f'Lista crescente: {lista}')
lista.sort(reverse=True)
print(f'Lista decrescente: {lista}')
