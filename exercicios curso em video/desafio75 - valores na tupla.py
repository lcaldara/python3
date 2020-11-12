cont = tot = 0
tupla = (int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')), int(input('Digite o terceiro valor: ')), int(input('Digite o quarto valor: ')))
print(f'Você digitou os números {tupla}.')
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição.')
else:
    print(f'O valor 3 não foi digitado.')
print(f'Os valores pares digitados foram: ', end='')
for cont in tupla:
    if cont % 2 == 0:
        tot += 1
        print(cont, end=' ')
print(f'\nForam digitados {tot} valores pares.')
