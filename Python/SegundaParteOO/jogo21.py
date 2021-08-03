print("-------------------------------------")
print("BEM VINDO AO JOGO DO 21!!")
print("-------------------------------------")
print("                                      ")
print("--- RESPONDA COM AS ALTERNATIVAS ABAIXO ---")
print("SIM == S")
print("NÃO == N")
print("                                      ")

def jogar_21():

    cartas_de_valor_fixo = input("Você recebeu apenas cartas de valor fixo (não recebeu Ás) ?")
    cartas_de_valor_fixo = cartas_de_valor_fixo.strip().upper()

     ##SE A PRIMEIRA RESPOSTA FOR NEGATIVA ELE NAO ENTRA NESTE PASSO
    if cartas_de_valor_fixo == 'N':
        cartas_com_as = input("Entre as duas cartas que você recebeu, há um Ás ?")
        cartas_com_as = cartas_com_as.strip().upper()
    else:
        cartas_com_as = 'N'

    cartas_com_mesmo_valor = input("Você recebeu 2 cartas de mesmo valor (pares) ?")
    cartas_com_mesmo_valor = cartas_com_mesmo_valor.strip().upper()

    print(cartas_de_valor_fixo, cartas_com_as, cartas_com_mesmo_valor)

    valor_carta_1 = int(input("Digite o valor da sua primeira carta!?"))
    valor_carta_2 = int(input("Digite o valor da sua segunda carta!?"))
    soma_das_cartas = int(valor_carta_1 + valor_carta_2)
    carta_da_casa = int(input("Digite o valor da carta da CASA!?"))


    print(valor_carta_1, valor_carta_2, soma_das_cartas, carta_da_casa)



    if (cartas_de_valor_fixo == 'S'):
        decisao = maos_de_valor_fixo(soma_das_cartas, carta_da_casa)
        print(decisao)
"""
    if (cartas_com_as == 'S'):
        decisao = maos_de_As(valor_carta_1, valor_carta_2, carta_da_casa)
        print(decisao)


def maos_de_As(valor_carta_1, valor_carta_2, carta_da_casa):

    qual_decisao_tomar = None

    carta_da_casa_valor_As_e_2 = [1, 2]
    carta_da_casa_valor_As_e_3 = [1, 3]
    carta_da_casa_valor_As_e_4 = [1, 4]
    carta_da_casa_valor_As_e_5 = [1, 5]
    carta_da_casa_valor_As_e_6 = [1, 6]
    carta_da_casa_valor_As_e_7 = [1, 7]
    carta_da_casa_valor_As_e_8 = [1, 8]
    carta_da_casa_valor_As_e_9 = [1, 9]
    carta_da_casa_valor_As_e_10 = [1, 10]

    carta_da_casa_valor_5_ou_6 = [5, 6]
    carta_da_casa_valor_entre_4_e_6 = [4, 5, 6]
    carta_da_casa_valor_entre_3_e_6 = [3, 4, 5, 6]
    carta_da_casa_valor_entre_2_e_8 = [2, 7, 8]

    cartas_na_minha_mao = [valor_carta_1, valor_carta_2]


    if (((valor_carta_1 == 1) or (valor_carta_2 == 2)) or ((valor_carta_1 == 1) or (valor_carta_2 == 3)) and (carta_da_casa in carta_da_casa_valor_5_ou_6)):
        qual_decisao_tomar = "Peça outra carta DOBRANDO a aposta!!"
        print("IF 1")
    elif (((valor_carta_1 in carta_da_casa_valor_As_e_2) or (valor_carta_2 in carta_da_casa_valor_As_e_2)) or ((valor_carta_1 in carta_da_casa_valor_As_e_3) or (valor_carta_2 in carta_da_casa_valor_As_e_3)) and (carta_da_casa not in  carta_da_casa_valor_5_ou_6)):
        qual_decisao_tomar = "Peça outra carta!!"
        print("IF 1")

    if (((valor_carta_1 in carta_da_casa_valor_As_e_4) or (valor_carta_2 in carta_da_casa_valor_As_e_4)) or ((valor_carta_1 in carta_da_casa_valor_As_e_5) or (valor_carta_2 in carta_da_casa_valor_As_e_5)) and (carta_da_casa in carta_da_casa_valor_entre_4_e_6)):
        qual_decisao_tomar = "Peça outra carta DOBRANDO a aposta!!"
        print("IF 2")
    elif (((valor_carta_1 in carta_da_casa_valor_As_e_4) or (valor_carta_2 in carta_da_casa_valor_As_e_4)) or ((valor_carta_1 in carta_da_casa_valor_As_e_5) or (valor_carta_2 in carta_da_casa_valor_As_e_5)) and (carta_da_casa not in carta_da_casa_valor_entre_4_e_6)):
        qual_decisao_tomar = "Peça outra carta!!"
        print("IF 2")

    if (((valor_carta_1 in carta_da_casa_valor_As_e_6) or (valor_carta_2 in carta_da_casa_valor_As_e_6)) and (carta_da_casa in carta_da_casa_valor_entre_3_e_6)):
        qual_decisao_tomar = "Peça outra carta DOBRANDO a aposta!!"
        print("IF 3")
    elif (((valor_carta_1 in carta_da_casa_valor_As_e_6) or (valor_carta_2 in carta_da_casa_valor_As_e_6)) and (carta_da_casa not in carta_da_casa_valor_entre_3_e_6)):
        qual_decisao_tomar = "Peça outra carta!!"
        print("IF 3")

    if (((valor_carta_1 in carta_da_casa_valor_As_e_7) or (valor_carta_2 in carta_da_casa_valor_As_e_7)) and (carta_da_casa in carta_da_casa_valor_entre_3_e_6)):
        qual_decisao_tomar = "Peça outra carta DOBRANDO a aposta!!"
        print("IF 4")
    elif (((valor_carta_1 in carta_da_casa_valor_As_e_7) or (valor_carta_2 in carta_da_casa_valor_As_e_7)) and (carta_da_casa in  carta_da_casa_valor_entre_2_e_8)):
        qual_decisao_tomar = "PARE!!"
        print("IF 4")
    elif (((valor_carta_1 in carta_da_casa_valor_As_e_7) or (valor_carta_2 in carta_da_casa_valor_As_e_7)) and (carta_da_casa in  carta_da_casa_valor_As_e_9)):
        qual_decisao_tomar = "Peça outra carta!!"
        print("IF 4")

    if (((valor_carta_1 in carta_da_casa_valor_As_e_8) or (valor_carta_2 in carta_da_casa_valor_As_e_8)) or (cartas_na_minha_mao in carta_da_casa_valor_As_e_9)):
        qual_decisao_tomar = "PARE!!"
        print("IF 5")

    if ((valor_carta_1 in carta_da_casa_valor_As_e_10) or (valor_carta_2 in carta_da_casa_valor_As_e_10)):
        qual_decisao_tomar = "Parabéns! Você fez blackjack e receberá 1,5 vezes o valor da sua aposta!!"
        print("IF 6")

    return qual_decisao_tomar
"""

def maos_de_valor_fixo(soma_das_cartas, carta_da_casa):

    qual_decisao_tomar = None

    carta_da_casa_valor_entre_3_e_6 = [3, 4, 5, 6]
    carta_da_casa_valor_entre_2_e_9 = [2, 3, 4, 5, 6, 7, 8, 9]
    carta_da_casa_valor_entre_As_e_10 = [1, 2, 7, 8, 9, 10]
    carta_da_casa_valor_de_As_ou_10 = [1, 10]
    carta_da_casa_valor_As = [1]
    carta_da_casa_valor_entre_4_e_6 = [4, 5, 6]
    cartas_da_casa_valor_de_As_a_10 = [1, 2, 3, 7, 8, 9, 10]
    soma_das_minhas_cartas = [13, 14, 15, 16]

    if (soma_das_cartas <= 8):
        qual_decisao_tomar = "Peça outra carta!!"
        print("IF 1")

    if ((soma_das_cartas == 9) and (carta_da_casa in carta_da_casa_valor_entre_3_e_6)):
        qual_decisao_tomar = "Peça outra carta DOBRANDO a aposta!!"
        print("IF 2")
    elif ((soma_das_cartas == 9) and carta_da_casa in carta_da_casa_valor_entre_As_e_10):
        qual_decisao_tomar = "Peça outra carta!!"
        print("IF 2")

    if ((soma_das_cartas == 10) and (carta_da_casa in carta_da_casa_valor_entre_2_e_9)):
        qual_decisao_tomar = "Peça outra carta DOBRANDO a aposta!!"
        print("IF 3")
    elif ((soma_das_cartas == 10) and carta_da_casa in carta_da_casa_valor_de_As_ou_10):
        qual_decisao_tomar = "Peça outra carta!!"
        print("IF 3")

    if ((soma_das_cartas == 11) and (carta_da_casa not in carta_da_casa_valor_As)):
        qual_decisao_tomar = "Peça outra carta DOBRANDO a aposta!!"
        print("IF 4")
    elif ((soma_das_cartas == 11) and (carta_da_casa in carta_da_casa_valor_As)):
        qual_decisao_tomar = "Peça outra carta!!"
        print("IF 4")

    if ((soma_das_cartas == 12) and (carta_da_casa in carta_da_casa_valor_entre_4_e_6)):
        qual_decisao_tomar = "PARE - a chance da casa passar de 21 nesse caso é muito grande!!"
        print("IF 5")
    elif ((soma_das_cartas == 12) and (carta_da_casa not in  carta_da_casa_valor_entre_4_e_6)):
        qual_decisao_tomar = "Peça outra carta!!"
        print("IF 5")

    if ((soma_das_cartas in soma_das_minhas_cartas) and (carta_da_casa in carta_da_casa_valor_entre_4_e_6)):
        qual_decisao_tomar = "PARE - você tem uma boa chance de estourar se pedir outras cartas!!"
        print("IF 6")
    elif ((soma_das_cartas in soma_das_minhas_cartas) and (carta_da_casa in  cartas_da_casa_valor_de_As_a_10)):
        qual_decisao_tomar = "Peça outra carta!!"
        print("IF 6")

    if ((soma_das_cartas == 17) or (soma_das_cartas == 21)):
        qual_decisao_tomar = "PARE!!"
        print("IF 7")

    return qual_decisao_tomar


if(__name__ == "__main__"): #Verifica se este arquivo está sendo rodado direto nele ou pelo arquivo que chama sua função
    jogar_21()