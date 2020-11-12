u = input('Informe a unidade da temperatura (C, F ou K): ')
t = float(input('Informe a temperatura a ser convertida: '))
if u == 'C' or u == 'c':
    print('{}ºC correspondem a {}ºF.\n{}ºC correspondem a {}K.'.format(t, (t*(9/5)+32), t, (t+273.15)))
else:
    if u == 'F' or u == 'f':
        print('{}ºF correspondem a {:.2f}ºC.\n{}ºF correspondem a {:.2f}K.'.format(t, ((t-32)*(5/9)), t, (((t-32)*(5/9))+273.15)))
    else:
        if u == 'K' or u == 'k':
            print('{}K correspondem a {:.2f}ºC.\n{}K correspondem a {:.2f}ºF.'.format(t, (t-273.15), t, (((t-273.15)*(9/5))+32)))



