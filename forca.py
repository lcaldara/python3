from random import randint

def mensagem_abertura():
    print(f'{"*" * 50:^50}')
    print(f'{"Bem vindo ao jogo da forca!":^50}')
    print(f'{"*" * 50:^50}')


def escolher_palavra():
    lista = []
    listacorrigida = []
    with open("palavras.txt") as arquivo:
        for palavra in arquivo:
            lista.append(palavra)
    for pos, palavra in enumerate(lista):
        lista[pos] = palavra.lower().strip()
    for palavra in lista:
        if ";" in palavra:
            palavra2 = palavra[:len(palavra) - 1]
            listacorrigida.append(palavra2)
    palavra_secreta = listacorrigida[randint(0, len(listacorrigida))]
    return palavra_secreta


def jogar():
    mensagem_abertura()
    palavra_secreta = escolher_palavra()

    palavralista = []
    letras_acertadas = []
    listachutes = []
    listaerros = []
    tentativa = 0
    erro = 0

    for c in range(0, len(palavra_secreta)):
        palavralista.append(palavra_secreta[c])
    for c in range(0, len(palavra_secreta)):
        letras_acertadas.append('_')
        #letras_acertadas = ["_" for letras in palavra_secreta]

    acertou = False
    enforcou = False

    print('')
    print(f'Palavra: {letras_acertadas}')
    print('')

    while not acertou and not enforcou:
        try:
            chute = str(input('Tente uma letra: ')).lower().strip()[0]
            listachutes.append(chute)
            tentativa += 1
            if chute not in palavralista:
                erro += 1
                print(f'Você errou! A palavra secreta não tem a letra "{chute}".')
                print(f'Este foi seu erro número {erro}. Você tem {6-erro} tentativas.')
                listaerros.append(chute)
                print(f'Lista de erros: {sorted(listaerros)}\n')
                print(f'Palavra: {letras_acertadas}.\n')
                if erro == 6:
                    print(f'Você não conseguiu acertar a palavra "{palavra_secreta}".')
                    enforcou = True
            if chute in palavralista:
                print(f'Você acertou! A palavra secreta tem a letra "{chute}".')
                for pos, letra in enumerate(palavra_secreta):
                    if chute == letra:
                        letras_acertadas[pos] = chute
                print(f'Palavra: {letras_acertadas}.\n')
                if letras_acertadas == palavralista:
                    print(f'Parabéns! Você acertou a palavra "{palavra_secreta}"')
                    acertou = True
        except IndexError:
            print("Digite um valor válido.\n")

    print(f'Tentativas: {tentativa}')
    print(f'Erros: {erro}\n')

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
