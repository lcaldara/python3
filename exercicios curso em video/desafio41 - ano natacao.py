from datetime import datetime
now = datetime.now()
nasc = int(input('Digite seu ano de nascimento: '))
idade = now.year - nasc
if idade < 9:
    print('O atleta tem {} anos e se encaixa na categoria MIRIM.'.format(idade))
elif 9 <= idade < 14:
    print('O atleta tem {} anos e se encaixa na categoria INFANTIL.'.format(idade))
elif 14 <= idade < 19:
    print('O atleta tem {} anos e se encaixa na categoria JÚNIOR.'.format(idade))
elif 19 <= idade < 20:
    print('O atleta tem {} anos e se encaixa na categoria SÊNIOR.'.format(idade))
elif idade >= 20:
    print('O atleta tem {} anos e se encaixa na categoria MASTER.'.format(idade))
