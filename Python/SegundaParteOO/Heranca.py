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



class Filme(Programa): ##herança - herdando o comportamento da classe list
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


##class Playlist(list):##herança - herdando o comportamento da classe list
##    def __init__(self, nome, programas):
##        self.nome = nome
##        super().__init__(programas)##inicializando o objeto list

class Playlist:##herança - herdando o comportamento da classe list
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)

vingadores = Filme('El caminho',2019,200)
todo_mundo = Filme('todo mundo em panico Bad',1999,100)
breaking = Serie('breaking Bad',2431,5)
better_call_saul = Serie('better_call_saul Bad',2018,5)

breaking.dar_like()
todo_mundo.dar_like()
todo_mundo.dar_like()
better_call_saul.dar_like()


filmes_e_series = [vingadores, breaking, todo_mundo, better_call_saul]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho do Playlist: {len(playlist_fim_de_semana.listagem)}')

for programa in playlist_fim_de_semana.listagem:
    print(programa)

print(f'Tem ou não? {better_call_saul in playlist_fim_de_semana.listagem}')##Preciso por o (f') para poder passar parâmetros