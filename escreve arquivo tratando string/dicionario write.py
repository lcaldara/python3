arquivo = open("palavras.txt", "r")
dicionario = open("dicionario.txt", "w")
lista = []
lista2 = []
for palavra in arquivo:
    lista.append(palavra)
arquivo.close()
for pos, palavra in enumerate(lista):
    lista[pos] = palavra.lower().strip()
for palavra in lista:
    if ";" in palavra:
        palavra2 = palavra[:len(palavra)-1]
        lista2.append(palavra2)
        dicionario.write(palavra2)
        dicionario.write("\n")
dicionario.close()
print(lista2)
