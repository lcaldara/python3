final = int(input('Número final da lista: '))
arquivo = open("primos.txt", "w")
arquivo.write("2 3 5 7 ")
for c in range(8, final):
    if c/c == 1 and c/1 == c and c % 2 != 0 and c % 3 != 0 and c % 5 != 0 and c % 7 != 0:
        arquivo.write(f'{c} ')
