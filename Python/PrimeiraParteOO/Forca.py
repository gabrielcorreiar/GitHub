import random

def jogar_forca(): #criando uma função -
                   # (Lembrando que tudo em baixo deve
                   # estar sempre identado dentro dela)

    abertura()
    palavra_secreta = carrega_palavra_screta()##pegando o retorno da palavra secreta
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)##passando a palavra secreta como a parametro para ser utilizado
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1 ## erros = erros + 1
            desenha_forca(erros)

        enforcou = erros == 7 ## Se a quantidade de erros for igual a 6 a variavel muda para TRUE
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        if (enforcou is True):
            imprime_mensagem_perdedor(palavra_secreta)

        if (acertou is True):
            imprime_mensagem_sucesso()

## TUPLE - () -> Não pode ser alterado - tuple = (4,3,2,1)
## LIST  - [] -> Pode ser alterado     - lista = [4,3,2,1]

def abertura():
    print("-------------------------------------")
    print("Bem vindo no jogo da Forca!!")
    print("-------------------------------------")

def carrega_palavra_screta():
    arquivo = open("palavras.txt", "r")
    lista_palavras = []

    for linha in arquivo:
        linha = linha.strip()
        lista_palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(lista_palavras))
    palavra_secreta = lista_palavras[numero].upper()

    return palavra_secreta ##retornando a palavra secreta para ser utilizada

def inicializa_letras_acertadas(palavra_secreta): ##recebendo a palavra secreta como a parametro para ser utilizado
    return ["_" for letras in palavra_secreta]  ##crie a quantidade de "_" para cada letra dentro da palavra secreta

def pede_chute():
    chute = input("Qual letra?")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1  ## index = index + 1

def imprime_mensagem_sucesso():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"): #Verifica se este arquivo está sendo rodado direto nele ou pelo arquivo que chama sua função
    jogar_forca()
