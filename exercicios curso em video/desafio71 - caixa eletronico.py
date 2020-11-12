from math import floor
vlr = int(input('Informe o valor a ser sacado: '))
div50 = floor(vlr / 50)
resto50 = vlr % 50
div20 = floor(resto50 / 20)
resto20 = resto50 % 20
div10 = floor(resto20 / 10)
resto10 = resto20 % 10
div1 = floor(resto10 / 1)
resto1 = resto10 % 1
while True:
    if resto50 == 0:
        print(f'Total de {div50:.0f} cedulas de R$ 50.')
        break
    if resto50 != 0 and resto20 == 0:
        print(f'Total de {div50:.0f} cedulas de R$ 50.')
        print(f'Total de {div20:.0f} cedulas de R$ 20.')
        break
    if resto20 != 0 and resto10 == 0:
        print(f'Total de {div50:.0f} cedulas de R$ 50.')
        print(f'Total de {div20:.0f} cedulas de R$ 20.')
        print(f'Total de {div10:.0f} cedulas de R$ 10.')
        break
    if resto10 != 0 and resto1 == 0:
        print(f'Total de {div50:.0f} cedulas de R$ 50.')
        print(f'Total de {div20:.0f} cedulas de R$ 20.')
        print(f'Total de {div10:.0f} cedulas de R$ 10.')
        print(f'Total de {div1:.0f} cedulas de R$ 1.')
        break
