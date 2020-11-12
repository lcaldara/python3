tabela = ('Palmeiras', 'Santos', 'Flamego', 'Inter', 'Atlético', 'Goiás', 'Botafogo',
          'Bahia', 'São Paulo', 'Corinthians', 'Grêmio', 'Athetico', 'Ceará', 'Fortaleza',
          'Vasco', 'Fluminense', 'Chapecoense', 'Cruzeiro', 'CSA', 'Avaí')
x = 'Chapecoense'
print(f'Lista de times em ordem de colocação: {tabela}')
print('-='*50)
print(f'Os cinco primeiros colocados são: {tabela[0:5]}')
print('-='*50)
print(f'Os quatro últimos times são: {tabela[-4:]}')
print('-='*50)
print(f'os times em ordem alfabética: {sorted(tabela)}')
print('-='*50)
print(f'A Chapecoense está na {tabela.index(x)+1}ª posição')
