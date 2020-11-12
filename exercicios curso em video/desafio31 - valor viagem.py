inicio = int(input('Escolha o inicio de sua viagem\n[1] RJ\n[2] SP\n[3] CF\n[4] SJC\nEscolha: '))
fim = int(input('Escolha fim de sua viagem: \n[1] RJ\n[2] SP\n[3] CF\n[4] SJC\nEscolha: '))
strinicio = str(inicio)
strfim = str(fim)
conc = strinicio+strfim
longas = ['12', '21', '14', '41']
curtas = ['13', '31', '34', '43']
if conc in longas:
    print('Sua viagem será interestadual.')
else:
    print('Sua viagem será intermunicipal.')
#dist = int(input('Digite a distância de sua viagem: '))
#if dist < 200:
#   vlr = dist * 0.50
#lse:
#    vlr = dist * 0.45
#print('O valor de sua passagem será de R${:.2f}.'.format(vlr))
