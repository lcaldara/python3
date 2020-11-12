from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
       'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
ranking = {}
for k, v in jogo.items():
    print(f'{k} tirou {v}.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*15)
print(f'{"RANKING":^30}')
print('-='*15)
for p, n in enumerate(ranking):
    print(f'{p+1}º lugar: {n[0]} com {n[1]}.')
