class Programa:
    def __init__(self, nome, ano):
        ##self.__nome = nome.title() ##Atributo privado não vai para classe filha
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()



class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        ## super() chama qualquer metodo da classe mãe
        super().__init__(nome, ano) ## Chamando o construtor da classe mãe
        self.duracao = duracao

##EXEMPLO DE POLIMORFISMO, TENHO DUAS FUNÇÕES COM O MESMO NOME EM CLASSES DIFERENTES
    def __str__(self):
        return f'{self._nome} - DURACAO {self.duracao} - {self.ano} TOTAL LIKES - {self._likes}' #retorna uma string

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        ## super() chama qualquer metodo da classe mãe
        super().__init__(nome, ano)  ## Chamando o construtor da classe mãe
        self.temporadas = temporadas

##EXEMPLO DE POLIMORFISMO, TENHO DUAS FUNÇÕES COM O MESMO NOME EM CLASSES DIFERENTES
    def __str__(self):
        return f'{self._nome} - TEMPORADAS {self.temporadas} - {self.ano} TOTAL LIKES - {self._likes}' #retorna uma string


vingadores = Filme('El caminho',2019,200)

breaking = Serie('breaking Bad',2431,5)
breaking.dar_like()



filmes_e_series = [vingadores, breaking]

for programa in filmes_e_series:
    print(programa) ##POLIMORFISMO
