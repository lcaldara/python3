import calendar
ano = int(input('Digite o ano: '))
x = calendar.monthlen(ano, 2)
if x == 29:
    print('Fevereiro tem {} dias, portanto, {} é um ano bissexto.'.format(x, ano))
else:
    print('Fevereiro tem {} dias, portanto, {} não é um ano bissexto.'.format(x, ano))
