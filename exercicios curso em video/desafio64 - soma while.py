c = 0
s = 0
n = 0
flag = 999
n = int(input('Digite o número a ser somado: '))
while n != flag:
    s = s + n
    c = c + 1
    n = int(input('Digite o número a ser somado: '))
print('A soma dos {} termos foi de {}.'.format(c, s))
