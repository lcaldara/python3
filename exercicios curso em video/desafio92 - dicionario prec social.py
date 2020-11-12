from datetime import date
atual = date.today().year
pessoa = dict()
grupo = []
while True:
    pessoa = {'Nome': str(input('Digite o nome: ')),
              'Idade': atual-(int(input('Ano de nascimento: '))),
              'CTPS': int(input('Nº da CTPS (0 para não informar): '))}
    if pessoa['CTPS'] != 0:
        pessoa['Ano'] = int(input('Ano de contratação: '))
        pessoa['Salário'] = float(input('Salário: '))
        pessoa['Aposentadoria'] = pessoa["Idade"]+(pessoa["Ano"]+35)-atual
    grupo.append(pessoa.copy())
    pessoa.clear()
    cont = str(input('Deseja continuar? [S/N] '))
    if cont in 'Nn':
        break
print('-='*30)
print(grupo)
c = 0
for p in grupo:
    for k, v in grupo[c].items():
        print(f'{k} tem o valor {v} e está na posição {c}.')
    c += 1
