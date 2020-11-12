from datetime import datetime
now = datetime.now()
nasc = int(input('Digite seu ano de nascimento: '))
idade = now.year - nasc
if idade < 18:
    print('Ainda não está na hora de se alistar.')
    print('Faltam {} anos para o seu alistamento.'.format(18-idade))
elif idade == 18:
    print('Está na hora de você se alistar.')
elif idade > 18:
    print('Passou da hora de você se alistar.')
    print('Você está {} ano(s) atrasado com as forças armadas.'.format(idade - 18))
