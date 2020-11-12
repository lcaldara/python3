cores = {}
print('\033[7;37;40mCALCULADORA DE TRIANGULOS\033[m')
r1 = int(input('Digite o comprimento do primeiro segmento de reta: '))
r2 = int(input('Digite o comprimento do segundo segmento de reta: '))
r3 = int(input('Digite o comprimento do terceiro segmento de reta: '))
if abs(r2 - r3) < r1 < (r2 + r3) and abs(r1 - r3) < r2 < (r1 + r3) and abs(r1 - r2) < r3 < (r1 + r2):
    print('É possível construir um triângulo.')
    if r1 == r2 == r3:
        print('Trata-se de um triângulo equilátero.')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('Trata-se de um triângulo isósceles.')
    elif r1 != r2 != r3:
        print('Trata-se de um triângulo escaleno.')
else:
    print('Não é possível construir um triângulo.')

