#from math import factorial
#f = factorial(n)
#print(f)

#n = int(input('Digite o número que deseja saber o fatorial: '))
#c = n
#f = 1
#print('Calculando o fatorial de {}! = '.format(n), end='')
#while c > 0:
#    print('{}'.format(c), end='')
#    print(' x ' if c > 1 else ' = ', end='')
#    f = f * c
#    c = c - 1
#print('{}'.format(f))

n = int(input('Digite o número que deseja saber o fatorial: '))
c = n
f = 1
print('Calculando o fatorial de {}! = '.format(n), end='')
for c in range(n, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
print(f)
