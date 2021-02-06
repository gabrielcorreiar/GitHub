def cria_conta(numero,titular,saldo,limite):
    conta = {"número":numero,"titular":titular,"saldo":saldo,"limite":limite}
    return conta

exibir = cria_conta(10,"gabriel",6000,1000)

print(exibir["saldo"])