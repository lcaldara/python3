num = int(input('Digite o primeiro termo da PA: '))
passo = int(input('Digite o passo da PA: '))
decimot = num + (10-1) * passo
for c in range(num, decimot + passo, passo):
    print(c, end='→')
print('Fim')
