lista = []
listapar = []
listaimpar = []
while True:
    x = int(input('Digite um número para a lista: '))
    lista.append(x)
    cont = str(input('Deseja continuar? [S/N] ')).upper().strip()
    while cont not in 'NS':
        cont = str(input('Digite um valor válido: [S/N] ')).upper().strip()
    if cont == 'N':
        break
for c in lista:
    if c % 2 == 0:
        listapar.append(c)
    else:
        listaimpar.append(c)
print(f'Lista completa: {lista}')
print(f'Lista par: {listapar}')
print(f'Lista impar: {listaimpar}')
