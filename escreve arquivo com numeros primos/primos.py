arquivo = open("primos.txt", "r")
lista = []
numeros = []
for num in arquivo:
    lista.append(num)
arquivo.close()
for num in lista[0].split():
    numeros.append(num)
print(numeros)
