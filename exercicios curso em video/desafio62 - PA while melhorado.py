num = int(input('Digite o primeiro termo da PA: '))
pa = num
c = 0
passo = int(input('Digite o passo da PA: '))
termos = int(input('Quantidade de termos da PA: '))
while c < termos:
    print(pa, '→ ' if c < (termos - 1) else 'Fim', end='')
    pa = pa + passo
    c = c + 1
