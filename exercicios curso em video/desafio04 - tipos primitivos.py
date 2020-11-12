x = input('Digite algo: ')
y = input('Digite outra coisa: ')
print(' ')
num = x.isnumeric()
num2 = y.isnumeric()
alpha = x.isalpha()
alnum = x.isalnum()
tipo = type(x)
if num is True:
    print('Trata-se de uma string numérica')
    print(' ')
else:
    if alpha is True:
        print('Trata-se de uma string alfabética')
        print(' ')
    else:
        if alnum is True:
            print('Trata-se de uma string alfanuérica')
            print(' ')
if num is True and num2 is True:
    ix = int(x)
    iy = int(y)
    s = ix+iy
    sub = ix-iy
    mult = ix*iy
    div = ix/iy
    pot = ix**iy
    print('A soma entre os números {} e {} vale: {}.'.format(ix, iy, s))
    print('A subtração entre os números {} e {} vale: {}.'.format(ix, iy, sub))
    print('A multiplicação entre os números {} e {} vale: {}'.format(ix, iy, mult))
    print('A divisão entre os números {} e {} vale: {:.2f}'.format(ix, iy, div))
    print('A exponenciação entre os números {} e {} vale: {}'.format(ix, iy, pot))

