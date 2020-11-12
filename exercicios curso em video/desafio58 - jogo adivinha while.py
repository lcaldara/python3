import time
import random
num = 0
tent = 0
num = random.randint(0, 10)
print(num)
print('Vou pensar em um número.')
escolha = int(input('Adivinhe o número que escolhi entre 0 e 10: '))
print('PROCESSANDO...')
time.sleep(1)
if num == escolha:
    tent = tent + 1
    print('''Eu também pensei no número {}. Parabéns.
Você precisou de {} tentativa.'''.format(num, tent))
while num != escolha:
    tent = tent + 1
    print('Nós não pensamos no mesmo número. ')
    if escolha < num:
        print('Tente um número MAIOR...')
    else:
        print('Tente um número MENOR...')
    escolha = int(input('Tente novamente: '))
    time.sleep(1)
    if num == escolha:
        print('''Eu também pensei no número {}. Parabéns.
Você acertou na {}ª tentativa.'''.format(num, tent+1))
