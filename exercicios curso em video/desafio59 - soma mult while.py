n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
op = 0
maior = 0
while op != 5:
    op = int(input('''\nInfome a operação desejada:
[1] Soma
[2] Multiplicação
[3] Maior
[4] Novos números
[5] Sair
Escolha: '''))
    if op == 1:
        print('\n{} + {} = {}'.format(n1, n2, n1+n2))
    elif op == 2:
        print('\n{} x {} = {}'.format(n1, n2, n1*n2))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('\nO maior número é o {}.'.format(maior))
    elif op == 4:
        n1 = int(input('\nDigite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    else:
        print('Opção inválida.')
print('\nFim')
