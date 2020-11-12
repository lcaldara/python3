maior = 0
menor = 100000
for c in range(0, 5):
    peso = float(input('Digite seu peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(maior)
print(menor)

