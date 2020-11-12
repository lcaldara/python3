lista = []
dados = []
c = 0
maior = 0
menor = 0
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso: ')))
    lista.append(dados[:])
    if c == 0:
        maior = dados[1]
        menor = dados[1]
    elif dados[1] > maior:
        maior = dados[1]
    elif dados[1] < menor:
        menor = dados[1]
    c += 1
    dados.clear()
    cont = str(input('Deseja continuar? [S/N] ')).upper().strip()
    while cont not in 'SN':
        cont = str(input('Digite um valor válido: [S/N] ')).upper().strip()
    if cont == 'N':
        break
print('=-'*30)
print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'Pessoas mais leves com {menor}kgs: ', end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
print()
print(f'Pessoas mais pesadas com {maior}kgs: ', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print('Fim') #SOLUÇÃO 1ª FORMA

'''if dados[1] >= 100:
        pesados.append(dados[:])
    if dados[1] <= 50:
        leves.append(dados[:])
    dados.clear()
    cont = str(input('Deseja continuar? [S/N] ')).upper().strip()
    while cont not in 'SN':
        cont = str(input('Digite um valor válido: [S/N] ')).upper().strip()
    if cont == 'N':
        break
print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'A lista dos leves: ', end='')
c = 0
for p in leves:
    print(leves[c][0], end=' ')
    c += 1
print()
print(f'A lista dos pesados: ', end='')
c = 0
for p in pesados:
    print(pesados[c][0], end=' ')
    c += 1''' #SOLUÇÃO 2ª FORMA

