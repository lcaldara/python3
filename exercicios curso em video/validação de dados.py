valido = False
novo = 0
while not valido:
    entrada = str(input('Valor: ')).replace(',', '.').strip()
    if entrada.isalpha() or entrada == '':
        print(f'\033[0;31mERRO: {entrada} não é um valor válido.\033[m')
    else:
        valido = True
        novo = float(entrada)
print(f'{novo:.2f}')
