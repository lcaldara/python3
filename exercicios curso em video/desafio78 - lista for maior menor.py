lista = []
maior = 0
menor = 0
x = 0
for c in range(0, 5):
    lista.insert(c, (int(input(f'Digite um valor para a pos {c}: '))))
    x = lista[c]
    if c == 0:
        maior = x
        menor = x
    if x < menor:
        menor = x
    if x > maior:
        maior = x
print('-='*30)
for pos, num in enumerate(lista):
    print(f'Número {num} na pos {pos}')
print('-='*30)
print(f'Lista: {lista}')
print(f'O maior valor digitado foi o {maior} nas posições ', end='')
for pos, num in enumerate(lista):
    if num == maior:
        print(f'{pos}... ', end='')
print()
print(f'O menor valor digitado foi o {menor} nas posições ', end='')
for pos, num in enumerate(lista):
    if num == menor:
        print(f'{pos}... ', end='')
