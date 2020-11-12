while True:
    n = int(input('Digite um número para a tabuada: '))
    print('='*15)
    i = 0
    f = 11
    for c in range(i, f):
        print(f'{n:2} x {c:2} = {n*c:3}')
    print('='*15)
    cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
print('Programa encerrado.')
