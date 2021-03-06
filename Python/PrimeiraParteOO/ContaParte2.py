
def carregarConta():

    Conta = cria_conta(10,"gabriel",9999,10000)
    print("Criei minha conta com {} reias".format(Conta["saldo"]))

    depositar = deposita(Conta,5000)
    print("Depositei: {}".format(Conta["saldo"]))

    Sacar = sacar(Conta,7000)
    print("Saquei: {}".format(Conta["saldo"]))

    Extrato = extrato(Conta)


def cria_conta(numero,titular,saldo,limite):
    conta = {"número":numero,"titular":titular,"saldo":saldo,"limite":limite}
    return conta

def deposita(conta,valor):
  conta["saldo"] += valor

def sacar(conta,valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("O saldo da conta é de: {}".format(conta["saldo"]))


if(__name__ == "__main__"): #Verifica se este arquivo está sendo rodado direto nele ou pelo arquivo que chama sua função
    carregarConta()

