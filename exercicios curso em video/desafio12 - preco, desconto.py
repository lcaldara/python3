x = float(input('Qual o valor total da venda? '))
desc = input('O pagamento será em dinheiro (desconto de 20%)? (S/N) ')
if desc == 's' or desc == 'S':
    print('O cliente pagará {}. O desconto total foi de {}.'.format(x*0.8, x*0.2))
else:
    print('O cliente pagará {}.'.format(x))
