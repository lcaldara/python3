#num = int(input('Digite o primeiro termo da PA: '))
#passo = int(input('Digite o passo da PA: '))
#decimot = num + (10-1) * passo
#for c in range(num, decimot + passo, passo):
#    print(c, end='→')
#print('Fim')

num = int(input('Digite o primeiro termo da PA: '))
pa = num
c = 0
passo = int(input('Digite o passo da PA: '))
while c < 10:
    print(pa, '→ ' if c < 9 else 'Fim', end='')
    pa = pa + passo
    c = c + 1
