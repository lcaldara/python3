from datetime import date
maior = 0
menor = 0
for c in range(0, 7):
    nasc = int(input('Digite a data de nascimento: '))
    idade = date.today().year - nasc
    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print('''Maior: {}
Menor: {}'''.format(maior, menor))
