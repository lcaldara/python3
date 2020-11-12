frase = str(input('Digite a frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = (junto[::-1])
if junto == inverso:
    print('Temos um palíndromo')
else:
    print('Não temos um palíndromo')
