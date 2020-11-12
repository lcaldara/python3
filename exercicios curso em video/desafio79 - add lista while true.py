lista = []
while True:
    add = int(input('Digite um valor: '))
    if lista.count(add) == 0:
        lista.append(add)
        print('Número adicionado com sucesseo...')
    else:
        print('Este número já consta na lista. Não adicionado.')
    cont = str(input('Deseja continuar [S/N]: ')).upper().strip()
    while cont not in 'SN':
        cont = str(input('Digite um valor válido [S/N]: ')).upper().strip()
    if cont == 'N':
        break
print('=-'*30)
print(f'Lista final: {sorted(lista)}')
