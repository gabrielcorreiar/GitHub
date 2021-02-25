

class Conta:

    def __init__(self, numero, titular, saldo, limite): ##Construtor do Python /
                                                        ##Self é a referência do objeto
                                                        ##O Ponto você acessa o objeto
        print("Construindo objeto... {}".format(self))
        self.__numero = numero         ## com os dois underlines (__) eu torno o atributo privado -  no Java seria (private numero)
        self.__titular = titular       ## com os dois underlines (__) eu torno o atributo privado
        self.__saldo = saldo           ## com os dois underlines (__) eu torno o atributo privado
        self.__limite = limite         ## com os dois underlines (__) eu torno o atributo privado

    def extrato(self):
        print("O saldo do titular {} é de {} reais".format(self.__titular,self.__saldo))

    def depositar(self,valor):
        self.__saldo += valor

    def sacar(self,valor):
        self.__saldo -= valor

    def transfere(self,valor,destino): ## EXEMPLO DE ENCAPSULAMENTO
        self.sacar(valor)
        destino.depositar(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
         self.__limite = limite #metodo SET NUNCA tem return

    ##ex: conta =  Conta(123,"Gabriel", 100, 1000)
    ##    conta = None -> Deste modo desreferenciando a varial conta do objeto Conta.
