#num = int(input('Digite o número: '))
#for c in range(1, num+1):
#    if num / c == 1 and num / 1 == c and num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
#        print('Número primo')
num = int(input('Digite o número: '))
div = 0
for c in range(1, num+1):
    if num % c == 0 and num % num == 0:
        div += 1
if div == 2:
    print('O número {} só tem {} divisores, e portanto é primo.'.format(num, div))
else:
    print('O número {} possui {} divisores, e portanto não é primo.'.format(num, div))
print('Acabou')
