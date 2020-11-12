alunos = dict()
alunos['Nome'] = str(input('Qual o nome do aluno? '))
alunos['Nota 1'] = float(input('Digite a 1ª nota: '))
alunos['Nota 2'] = float(input('Digite a 2ª nota: '))
alunos['Media'] = (alunos['Nota 1']+alunos['Nota 2'])/2
for k, v in alunos.items():
    print(f'{k} é igual a {v}')
if alunos['Media'] < 5:
    print(f'A situação é REPROVADO, com a média {alunos["Media"]:.2f}.')
if alunos['Media'] >= 5:
    print(f'A situação é APROVADO, com a média {alunos["Media"]:.2f}.')
