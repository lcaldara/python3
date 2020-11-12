dec = int(input('Escreva o número a ser convertido: '))
base = int(input('''Escolha a base
[1] Binária
[2] Octal
[3] Hexadecimal
Escolha: '''))
if base == 1:
    print('O binário de {} é {}'.format(dec, bin(dec)[2:]))
elif base == 2:
    print('O octal de {} é {}'.format(dec, oct(dec)[2:]))
elif base == 3:
    print('O hexagonal de {} é {}'.format(dec, hex(dec)[2:]))
else:
    print('Opção inválida.')
