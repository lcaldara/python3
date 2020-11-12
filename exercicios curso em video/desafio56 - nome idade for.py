media = 0
maioridade = 0
nomemaior = ' '
mulhermenor = 0
for c in range(1, 5):
    print('===== {}ª pessoa ====='.format(c))
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite o sexo: '))
    media = media + idade
    if sexo in 'Mm' and idade > maioridade:
        nomemaior = nome
    if sexo in 'Ff' and idade < 20:
        mulhermenor = mulhermenor + 1
mediafim = media/4
print(mediafim)
print(nomemaior)
print(mulhermenor)

