import random
import time
num = random.randint(0, 5)
print('Vou pensar em um número.')
escolha = int(input('Adivinhe o número que escolhi entre 0 e 5: '))
print('PROCESSANDO...')
time.sleep(3)
if num == escolha:
    print('Nós pensamos o mesmo número. Eu também escolhi o número {}.'.format(num))
else:
    print('Nós não escolhemos o mesmo número. Eu escolhi o número {}.'.format(num))
