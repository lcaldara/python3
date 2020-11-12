jogador = {'Nome': str(input('Nome do jogador: ')), 'Partidas': int(input('Número de partidas: '))}
gols = []
total = 0
for g in range(1, jogador['Partidas']+1):
    gols.append(int(input(f'Gols na partida {g}: ')))
    total += gols[g-1]
jogador['Gols'] = gols[:]
jogador['Total'] = total
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas.')
for p, g in enumerate(gols):
    print(f'    => Na partida {p+1} fez {g} gols.')
print(f'O total foi de {jogador["Total"]} gols.')
