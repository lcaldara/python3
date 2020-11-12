from random import randint
c = 0
while True:
    n = int(input('Diga um valor: '))
    parimp = str(input('Par ou impar? [P/I]')).upper().strip()[0]
    while parimp not in 'PI':
        parimp = str(input('Escolha uma opção válida: [P/I] ')).upper().strip()[0]
    comp = randint(1, 10)
    res = n + comp
    if res % 2 == 0 and parimp == 'P':
        print(f'Você jogou {n} e o computador {comp}. Total de {res} e deu PAR.\nVocê GANHOU!')
        c = c + 1
    if res % 2 != 0 and parimp == 'P':
        print(f'Você jogou {n} e o computador {comp}. Total de {res} e deu IMPAR.\nVocê PERDEU!')
        break
    if res % 2 == 0 and parimp == 'I':
        print(f'Você jogou {n} e o computador {comp}. Total de {res} e deu PAR.\nVocê PERDEU!')
        break
    if res % 2 != 0 and parimp == 'I':
        print(f'Você jogou {n} e o computador {comp}. Total de {res} e deu IMPAR.\nVocê GANHOU!')
        c = c + 1
print(f'Você ganhou {c} rodada(s) consecutiva(s).')
