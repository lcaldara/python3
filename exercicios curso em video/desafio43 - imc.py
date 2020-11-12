alt = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (pow(alt, 2))
if imc <= 18.5:
    print('Seu IMC é {:.2f} e você está abaixo do peso.'.format(imc))
elif 18.5 < imc <= 25:
    print('Seu IMC é {:.2f} e você está dentro da sua faixa de peso.'.format(imc))
elif 25 < imc <= 30:
    print('Seu IMC é {:.2f} e você está com sobrepeso.'.format(imc))
elif 30 < imc <= 40:
    print('Seu IMC é {:.2f} e você está obeso.'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.2f} e você está com obesidade mórbida.'.format(imc))
