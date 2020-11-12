import random
frase = 'Curso em Vídeo Python'

#fatiamento

fat = frase[9:21:2]
#[9:13] fatia do 9 ao 13
#[9:21:2] fatia do 9 ao 21 pulando 2
#[:5] fatia do inicio ao 5
#[15:] fatia do 15 ao final
#[9::3] fatia do 9 ao fim pulando 3
print(frase[9:21:2])
print(len(frase))
print(len(fat))
#comprimento da frase
print(frase.count('o'))
#conta a quantidade e 'os' da frase
print(frase.count('o', 0, 13))
#conta os 'os' do 0 ao 13
print(frase.find('deo'))
#acha na frase
print('Curso' in frase)
#retorna boleano caso haja a string na frase
print(frase.replace('Python', 'Android'))
#substitui todas as palavras Python por Android
print(frase.upper())
#coloca todas as strings em maiúsculo
print(frase.lower())
print(frase.capitalize())
#coloca só a primeira letra da primeira palavra em maiúsculo
print(frase.title())
#coloca toda primeira letra de cada palavra em maiúsculo
print(frase.split())
#divide nos espaços
print(len(frase.split()))
#conta as palavras
print(frase.upper().count('O'))
#passa pra maiusculo e conta os 'os'
dividido = frase.split()
print(dividido[0])
#imprime a primeira palavra da lista dividido
print(dividido[2][3])
#imprime a terceira letra (começa na letra zero) dentro da palavra 2 começa na palavra zero
