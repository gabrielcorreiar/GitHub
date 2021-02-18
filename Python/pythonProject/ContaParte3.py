

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
<<<<<<< HEAD
        self.saldo -= valor

    ##ex: conta =  Conta(123,"Gabriel", 100, 1000)
    ##    conta = None -> Deste modo desreferenciando a varial conta do objeto Conta.
=======
        self.__saldo -= valor

    def transfere(self,valor,destino): ## EXEMPLO DE ENCAPSULAMENTO
        self.sacar(valor)
        destino.depositar(valor)
>>>>>>> 2d47fc7fe43c6afd05f057b11bed474993ee2f82
