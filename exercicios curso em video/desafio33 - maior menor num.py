a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
if a > b > c:
    print('O maior número é o {}.'.format(a))
    print('O menor número é o {}.'.format(c))
elif b > a > c:
    print('O maior número é o {}.'.format(b))
    print('O menor número é o {}.'.format(c))
elif c > a > b:
    print('O maior número é o {}.'.format(c))
    print('O menor número é o {}.'.format(b))
elif c > b > a:
    print('O maior número é o {}.'.format(c))
    print('O menor número é o {}.'.format(a))
elif a > b == c:
    print('O maior número é o {}.'.format(a))
    print('O menor número é o {}.'.format(b))
elif b > a == c:
    print('O maior número é o {}.'.format(b))
    print('O menor número é o {}.'.format(a))
elif c > a == b:
    print('O maior número é o {}.'.format(c))
    print('O menor número é o {}.'.format(a))
elif a < b == c:
    print('O maior número é o {}.'.format(b))
    print('O menor número é o {}.'.format(a))
elif b < a == c:
    print('O maior número é o {}.'.format(a))
    print('O menor número é o {}.'.format(b))
elif c < a == b:
    print('O maior número é o {}.'.format(a))
    print('O menor número é o {}.'.format(c))
