#import random
#import time
#itens = ('Pedra', 'Papel', 'Tesoura')
#computador = randint(0, 2)
#print('O computador escolheu {}'.format(itens[computador]))
#emp = vit = der = 0
#while True:
#    lista = ['Pedra', 'Papel', 'Tesoura']
#    random.shuffle(lista)
#    x = int(input('''[1] Pedra
#[2] Papel
#[3] Tesoura
#Escolha do usuário: '''))
#    while x not in [1, 2, 3]:
#        x = int(input('Digite uma opção válida [1/2/3] '))
#    time.sleep(0.5)
#    print('JO')
#    time.sleep(0.5)
#    print('KEN')
#    time.sleep(0.5)
#    print('PO!!!')
#    if lista[0] == 'Pedra' and x == 1:
#        print('O computador também escolheu {} e o jogo empatou.'.format(lista[0]))
#        emp += 1
#    elif lista[0] == 'Pedra' and x == 2:
#        print('O computador escolheu {} e foi derrotado.'.format(lista[0]))
#        vit += 1
#    elif lista[0] == 'Pedra' and x == 3:
#        print('O computador escolheu {} e venceu o jogo.'.format(lista[0]))
#        der += 1
#    elif lista[0] == 'Papel' and x == 2:
#        print('O computador também escolheu {} e o jogo empatou.'.format(lista[0]))
#        emp += 1
#    elif lista[0] == 'Papel' and x == 3:
#        print('O computador escolheu {} e foi derrotado.'.format(lista[0]))
#        vit += 1
#    elif lista[0] == 'Papel' and x == 1:
#        print('O computador escolheu {} e venceu o jogo.'.format(lista[0]))
#        der += 1
#    elif lista[0] == 'Tesoura' and x == 3:
#        print('O computador também escolheu {} e o jogo empatou.'.format(lista[0]))
#        emp += 1
#    elif lista[0] == 'Tesoura' and x == 1:
#        print('O computador escolheu {} e foi derrotado.'.format(lista[0]))
#        vit += 1
#    elif lista[0] == 'Tesoura' and x == 2:
#        print('O computador escolheu {} e venceu o jogo.'.format(lista[0]))
#        der += 1
#    cont = str(input('Vamos jogar de novo? [S/N] ')).upper().strip()[0]
#    while cont not in 'NS':
#        cont = str(input('Digite uma opção válida [S/N] ')).upper().strip()[0]
#    if cont == 'N':
#        break
#print('-='*20)
#print('              SCORE FINAL              ')
#print('-='*20)
#print(f'Vitórias: {vit}')
#print(f'Empates : {emp}')
#print(f'Derrotas: {der}')

import random
import time
emp = vit = der = 0
while True:
    lista = ['Pedra', 'Papel', 'Tesoura']
    random.shuffle(lista)
    x = str(input('''[1] Pedra
[2] Papel
[3] Tesoura
Escolha do usuário: '''))
    while x not in '123':
        x = str(input('Digite uma opção válida [1/2/3]: '))
    time.sleep(0.5)
    print('JO')
    time.sleep(0.5)
    print('KEN')
    time.sleep(0.5)
    print('PO!!!')
    if lista[0] == 'Pedra' and x == '1':
        print(f'O computador também escolheu {lista[0]} e o jogo empatou.')
        emp += 1
    elif lista[0] == 'Pedra' and x == '2':
        print(f'O computador escolheu {lista[0]} e foi derrotado.')
        vit += 1
    elif lista[0] == 'Pedra' and x == '3':
        print(f'O computador escolheu {lista[0]} e venceu o jogo.')
        der += 1
    elif lista[0] == 'Papel' and x == '2':
        print(f'O computador também escolheu {lista[0]} e o jogo empatou.')
        emp += 1
    elif lista[0] == 'Papel' and x == '3':
        print(f'O computador escolheu {lista[0]} e foi derrotado.')
        vit += 1
    elif lista[0] == 'Papel' and x == '1':
        print(f'O computador escolheu {lista[0]} e venceu o jogo.')
        der += 1
    elif lista[0] == 'Tesoura' and x == '3':
        print(f'O computador também escolheu {lista[0]} e o jogo empatou.')
        emp += 1
    elif lista[0] == 'Tesoura' and x == '1':
        print(f'O computador escolheu {lista[0]} e foi derrotado.')
        vit += 1
    elif lista[0] == 'Tesoura' and x == '2':
        print(f'O computador escolheu {lista[0]} e venceu o jogo.')
        der += 1
    cont = str(input('Vamos jogar de novo? [S/N] ')).upper().strip()[0]
    while cont not in 'NS':
        cont = str(input('Digite uma opção válida [S/N]: ')).upper().strip()[0]
    if cont == 'N':
        break
print('-='*20)
print(' '*14+'SCORE FINAL'+' '*14)
print('-='*20)
print(f'Vitórias: {vit}')
print(f'Empates : {emp}')
print(f'Derrotas: {der}')
