n = int(input('Digite um número para a tabuada: '))
print('='*15)
i = 0
f = 11
for c in range(i, f):
    print('{:2} x {:2} = {:3}'.format(n, c, n*c))
print('='*15)
print('Fim')
