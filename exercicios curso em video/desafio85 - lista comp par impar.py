lista = []
par = []
impar = []
dados = []
maior = 0
menor = 0
for c in range(0, 7):
    dados.append(int(input(f'Digite o {c+1}º valor: ')))
    lista.append(dados[:])
    if dados[0] % 2 == 0:
        par.append(dados[:])
    else:
        impar.append(dados[:])
    dados.clear()
print(f'Lista final: {sorted(lista)}')
print(f'Lista de pares: {sorted(par)}')
print(f'Lista de impares: {sorted(impar)}')



