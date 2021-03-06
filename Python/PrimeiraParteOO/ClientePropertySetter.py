

class Cliente:

    def __init__(self, nome):
        self.__nome = nome


    #def get_nome(self):
    #    return self.nome.title()

    @property
    ##metodo com o mesmo nome do atributo
    ##este metodo representa uma propriedade -> nao precisa por os () para executar
    ##Para ser executado com sucesso necessita que o atributo seja PRIVADO (__nome)

    ##Ex de execução: cliente.nome
    def nome(self):
        print("chamando @property nome()")
        return self.__nome.title()

    @nome.setter
    ##metodo com o mesmo nome do atributo
    ##este metodo representa uma propriedade -> nao precisa por os () para executar
    ##Para ser executado com sucesso necessita que o atributo seja PRIVADO

    ##Ex de execução: cliente.nome = "Gabriel"
    def nome(self, nome):
        print("chamando @nome.setter nome()")
        self.__nome = nome