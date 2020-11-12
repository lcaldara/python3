s = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite o valor: '))
    if n % 2 == 0:
        s = s + n
        cont = cont + 1
print('O somatório dos números pares foi {}'.format(s))
print(cont)
