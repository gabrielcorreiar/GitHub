

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

    def __pode_sacar(self,valor_de_saque):  # Exemplo de metodo Privado
        valor_disponivel = self.__saldo + self.__limite
        return valor_de_saque <= valor_disponivel

    def sacar(self,valor):
        if ((self.__pode_sacar(valor))):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite disponivel".format(valor))

    def transfere(self,valor,destino): ## EXEMPLO DE ENCAPSULAMENTO
        self.sacar(valor)
        destino.depositar(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    #def get_limite(self):
    #    return self.__limite

    #def set_limite(self, limite):
    #     self.__limite = limite #metodo SET NUNCA tem return

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco(): # Exemplo de um metodo estático -> executa sem criar o objeto -> Conta.codigo_banco()
        return "001"


    ##ex: conta =  Conta(123,"Gabriel", 100, 1000)
    ##    conta = None -> Deste modo desreferenciando a varial conta do objeto Conta.
