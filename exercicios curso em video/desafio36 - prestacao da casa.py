vlr = float(input('Qual o valor da casa? '))
sal = float(input('Qual o valor do seu salário? '))
nPrest = int(input('Em quantos anos você quer pagar? '))
totPrest = nPrest * 12
parcela = vlr / totPrest
if parcela > (sal*0.3):
    print('Seu empréstimo não foi aprovado.')
elif parcela <= (sal*0.3):
    print('Seu empréstimo foi aprovado.')
    print('A parcela mensal será de R$ {:.2f}.'.format(parcela))
