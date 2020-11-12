def mensagem(msg):
    print('~' * len(msg))
    print(f'{msg:^{len(msg)}}')
    print('~' * len(msg))


mensagem(str(input('Digite a mensagem: ')))
mensagem(' Curso de Python no Youtube ')
mensagem(' CeV ')
