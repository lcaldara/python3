from random import randint
tupla = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print(f'Os valores sorteados foram {tupla}')
print(f'O menor valor sorteado foi o {sorted(tupla)[0]}')
print(f'O maior valor sorteado foi o {sorted(tupla)[4]}')
#print(f'O maior valor sorteado foi o {max(tupla)}')
#print(f'O menor valor sorteado foi o {min(tupla)}')
