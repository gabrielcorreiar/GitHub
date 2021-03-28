import Forca
import Advinhacao

def escolher_jogo():
    print("-------------------------------------")
    print("Escolha o seu jogo!!")
    print("-------------------------------------")


    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual Jogo quer jogar?"))

    if(jogo == 1):
        print("Jogando Forca")
        Forca.jogar_forca() #chamando a função
    elif(jogo ==2):
        print("Jogando Adivinhação")
        Advinhacao.jogar_adivinhacao() #chamando a função

if(__name__ == "__main__"): #Verifica se este arquivo está sendo rodado direto nele ou pelo arquivo que chama sua função
    escolher_jogo()