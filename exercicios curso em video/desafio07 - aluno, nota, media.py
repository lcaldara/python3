nome = input('Digite o nome do aluno: ')
provas = int(input('Digite a quantidade de provas feitas (máximo de 3): '))
if provas == 1:
    n1 = float(input('Digite a nota da primeira prova: '))
    media = n1/2
elif provas == 2:
        n1 = float(input('Digite a nota da primeira prova: '))
        n2 = float(input('Digite a nota da segunda prova: '))
        media = (n1+n2)/provas
elif provas == 3:
            n1 = float(input('Digite a nota da primeira prova: '))
            n2 = float(input('Digite a nota da segunda prova: '))
            n3 = float(input('Digite a nota da terceira prova: '))
            media = (n1+n2+n3)/provas
if media >= 7:
    print('O aluno {} foi aprovado com a media {:.2f}'.format(nome, media))
elif 5 <= media <= 6.9:
    print('O aluno {} está em recuperação. Sua média foi {}.'.format(nome, media))
elif media < 5:
    print('O aluno {} foi reprovado com a media {:.2f}'.format(nome, media))

