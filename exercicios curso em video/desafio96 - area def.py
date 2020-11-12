def linha(msg):
    print('--'*20)
    print(f'{msg:^40}')
    print('--'*20)


def area():
    linha('Controle de Terrenos')
    m = a * b
    print(f'A área do terreno de {a}x{b} é de {m}m².')


a = float(input('Largura (m): '))
b = float(input('Comprimento (m): '))
area()
