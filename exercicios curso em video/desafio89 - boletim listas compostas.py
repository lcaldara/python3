lista = []
dados = []
while True:
    dados.append(str(input('Digite o nome do aluno: ')))
    dados.append(float(input('Digite a 1ª nota: ')))
    dados.append(float(input('Digite a 2ª nota: ')))
    lista.append(dados[:])
    dados.clear()
    cont = str(input('Deseja continuar? [S/N]')).upper().strip()
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N]')).upper().strip()
    if cont == 'N':
        break
print('-=-'*20)
print(f'{"Nº":4}{"NOME":<10}{"MÉDIA":>8}')
print('---'*10)
for pos, p in enumerate(lista):
    print(f'{pos:<4}{p[0]:<10}{((p[1]+p[2])/2):>7}')
print('---'*10)
print()
while True:
    op = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if op == 999:
        break
    print('---'*10)
    print(f'{"Aluno : ":<7}{lista[op][0]}'
          f'\n{"Nota 1: ":<7}{lista[op][1]}'
          f'\n{"Nota 2: ":<7}{lista[op][2]}')
    print('---'*10)
