grupo = []
mulheres = []
acima = []
pessoa = dict()
while True:
    pessoa = {'Nome': str(input('Digite o nome: ')),
              'Sexo': str(input('Informe o sexo: ')).upper().strip(),
              'Idade': int(input('Informe a idade: '))}
    grupo.append(pessoa.copy())
    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa.copy())
    pessoa.clear()
    cont = str(input('Deseja continuar? [S/N] '))
    if cont in 'Nn':
        break
print('-='*30)
print(f'- O grupo tem {len(grupo)} pessoa(s).')
c = total = 0
for p in grupo:
    total += grupo[c]['Idade']
    c += 1
media = total/(len(grupo))
print(f'- A média de idade é de {media} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
c = 0
for m in mulheres:
    print(mulheres[c]['Nome'], end=' ')
    c += 1
print()
c = 0
for p in grupo:
    if grupo[c]['Idade'] > media:
        acima.append(grupo[c].copy())
    c += 1
print(f'- Lista das pessoas acima da média de idade: ')
c = 0
for p in acima:
    print(p)
    c += 1
