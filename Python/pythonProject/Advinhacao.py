import random

def jogar_adivinhacao(): #criando uma função -
                         # (Lembrando que tudo em baixo deve
                         # estar sempre identado dentro dela)

    print("-------------------------------------")
    print("Bem vindo!!")
    print("-------------------------------------")

    total_tentativas = 0
    pontos = 1000

    print("Escolha o nivel do jogo!!")
    print("1 - Fácil   2 - Médio  3 - Difícil")
    nivel = int(input("Digite o nivel escolhido:"))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5


    valor_fixo = random.randrange(1,101)
    valor_secreto = round(valor_fixo)



    for rodada in range(1,total_tentativas +1):
        print("Tentaiva {} de {}".format(rodada,total_tentativas))
        valor_digitado = input("Digite um valor:")
        print("você digitou", valor_digitado)
        valor = int(valor_digitado)


        if(valor < 1 or valor > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue


        acertou = valor == valor_secreto
        maior = valor > valor_secreto
        menor = valor < valor_secreto


        if(acertou):
            print("Acertou o número secreto !!")
            break
        else:
            if(maior):
                print("Errou, chutou um número maior que o valor secreto, tente outra vez !!")
            elif(menor):
                print("Errou, chutou um número menor que o valor secreto, tente outra vez !!")
            pontos_perdidos = abs(valor_secreto - valor)
            pontos = pontos - pontos_perdidos

    print("FIM DE JOGO !! Você fez {} pontos".format(pontos))

if(__name__ == "__main__"): #Verifica se este arquivo está sendo rodado direto nele ou pelo arquivo que chama sua função
    jogar_adivinhacao()