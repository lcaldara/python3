from random import randint
from time import sleep
lista = []
rep = []
tot = int(input('Quantos jogos? '))
for t in range(0, tot):
    for c in range(0, 6):
        rand = randint(1, 60)
        for r in rep:
            if rand in rep:
                rand = randint(1, 60)
        rep.append(rand)
    lista.append(rep[:])
    rep.clear()
c = 1
print('-='*5+' SORTEANDO OS JOGOS '+'=-'*5)
for j in lista:
    print(f'Jogo {c}: {sorted(j)}')
    c += 1
    sleep(1)
print('-='*7+' BOA SORTE '+'=-'*7)
