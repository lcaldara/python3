lista = []
for c in range(0, 5):
    x = int(input('Digite um valor: '))
    if c == 0:
        lista.append(x)
    elif x > lista[len(lista)-1]:
        lista.append(x)
    else:
        pos = 0
        while pos < len(lista):
            if x <= lista[pos]:
                lista.insert(pos, x)
                break
            pos += 1
print(lista)
