from math import sqrt
# É possívem importar todo o math (import math), porém, na fórmula entraria math.sqrt
x = int(input('Digite um número: '))
print('O dobro de {} é {}, o triplo é {}, e sua raiz quadrada vale {:.2f}'.format(x, x*2, x*3, sqrt(x)))

