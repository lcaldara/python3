vel = int(input('Informe a velocidade do automóvel: '))
if vel > 80:
    valor = (vel - 80) * 7
    print('Sua velocidade foi de {}km/h.\nVocê foi multado!\nO valor da multa será de R${:.2f}'.format(vel, valor))
else:
    print('Sua velocidade foi de {}km/h.'.format(vel))
