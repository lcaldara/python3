import random
a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o nome do segundo aluno: ')
c = input('Digite o nome do terceiro aluno: ')
d = input('Digite o nome do quarto aluno: ')
lista = [a, b, c, d]
aluno = random.choice(lista)
print('O aluno escolhido foi o(a) {}.'.format(aluno))

random.shuffle(lista)
print(lista)

'''import random
a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o nome do segundo aluno: ')
c = input('Digite o nome do terceiro aluno: ')
d = input('Digite o nome do quarto aluno: ')
r = random.randint(1, 4)
if r == 1:
    print('O aluno {} foi escolhido.'.format(a))
else:
    if r == 2:
        print('O aluno {} foi escolhido.'.format(b))
    else:
        if r == 3:
            print('O aluno {} foi escolhido.'.format(c))
        else:
            if r == 4:
                print('O aluno {} foi escolhido.'.format(d))'''
