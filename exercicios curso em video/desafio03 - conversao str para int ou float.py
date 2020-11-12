x = int(input('Digite o primeiro numero (x): '))
y = int(input('Digite o segundo numero (y): '))
soma = x+y
sub = x-y
mult = x*y
div = x/y
pw = pow(x, y)  #ou x**y
print('O resultado da soma entre {} e {} é: {}'.format(x, y, soma))
print('O resultado da subtração é: {}'.format(sub))
print('O resultado da multiplicação é: {}'.format(mult))
print('O resultado da divisão é: {:.2f}'.format(div))
print('O resultado de x elevado a y é: {}'.format(pw))

#n = input('Digite o primeiro número a ser somado: ')
#m = input('Digite o segundo número a ser somado: ')
#if ((n.isnumeric()) & (m.isnumeric())) is True:
#    n1 = int(n)
#    m1 = int(m)
#    s = n1 + m1
#    print(s)
#else:
#    print('Não se trata de números reais')

