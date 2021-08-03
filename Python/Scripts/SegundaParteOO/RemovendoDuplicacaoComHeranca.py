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




class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        ## super() chama qualquer metodo da classe mãe
        super().__init__(nome, ano)  ## Chamando o construtor da classe mãe
        self.temporadas = temporadas




vingadores = Filme('El caminho',2019,200)
print(vingadores.nome)

breaking = Serie('breaking Bad',2431,5)
breaking.dar_like()
print(f'{breaking.nome} - {breaking.ano} - {breaking.temporadas} - {breaking.likes}')