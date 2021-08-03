import pandas as pd

dataset = pd.read_csv('db.csv', sep =';')

#Comandos Básicos do pandas
#----------------------------------------------------------------------
'''
   #tipo de dados do dataset
print(dataset.dtypes)

    #lista mais detalhadamente o tipo de dados do dataset
print(dataset.info())

    #Gera um conjunto de estatisticas do dado analisado
print(dataset[['Quilometragem', 'Valor']].describe())
'''
#----------------------------------------------------------------------



#Trabalhando com Tuplas -> Tuplas são imutáveis e listas são mutáveis (Uma Tupla é sempre entre parenteses)
#----------------------------------------------------------------------
'''
tuplaNumeros = (1, 2, 3, 4)
tuplaNomes = ('Gabriel', 'Rafael', 'Laura',('Alacir', 'Luiz', 'Ana Paula'))
print(tuplaNumeros,tuplaNomes)
print(type(tuplaNumeros))#Vejo o tipo da variavel
print(tuplaNomes[0])#Pega o nome na primeira posição
print(tuplaNomes[1:3])
print(tuplaNomes[-1][2])#Pego o ultimo registro da tupla, e como esse
                        #registro é uma tupla também, eu navego nas
                        #posições dentro dele

#zip -> unifica duas tuplas
for nome, numero in zip(tuplaNomes,tuplaNumeros):
    print(nome, numero)

#zip -> unifica duas tuplas
for nome, numero in zip(tuplaNomes,tuplaNumeros):
    if (numero > 2):
        print(nome, numero)
'''
#----------------------------------------------------------------------



#Trabalhando com Dicionários
#----------------------------------------------------------------------
'''
carros = ['Mercedes', 'BMW', 'Audi']
valores = [100000, 120000, 90000]

dados = dict(zip(carros, valores))# junta as duas listas em um dicionário
print(dados)
print(type(dados))#exibe o tipo da variavel
print(dados['BMW'])
print('Audi' in dados)#verifica se existe (Audi) dentro da variavel dados
print(len(dados))#verifica quantas chave/valor existe no dicionario
dados['Hyundai'] = 555555#insere o registro dentro do dicionario
print(dados)
del dados['Audi']#delete o registardo audi
print(dados)
dados.update({'Volks': 99999, 'Ford': 33333})#atualizando o dicionario com o registro do Volks
print(dados)
dadosCopy = dados.copy()#estou copiando os dados do dicionario (dados) para outra variavel
print(dadosCopy)
del dadosCopy['Ford']
print(dadosCopy)
print(dadosCopy.pop('Ford', 'Chave não encontrada'))#essa função deleta o registro e caso esse não tenha sido encontrado ele retorna uma msg
print(dadosCopy.pop('Volks', 'Chave não encontrada'))
print(dadosCopy.clear())#ele remove todos os itens do dicionário


#iteração de dicionarios
print(dados.keys())#exibe todas as chaves do dicionario

for valorCarro in dados.keys():#exibe os valores de cada chave
    print(dados[valorCarro])

print(dados.values())#exibe apenas os valores de cada chave
print(dados.items())#retorna uma lista contendo uma tupla para cada chave e valor

for carro, valor in dados.items():
    print(carro, valor)

for carro, valor in dados.items():
    if (valor > 100000):
        print('Entrei na Verificação')
        print(carro, valor)
'''
#----------------------------------------------------------------------



#Built-in Functions + Funções criadas
#----------------------------------------------------------------------
'''
carros = ['Mercedes', 'BMW', 'Audi']
valores = [10, 10, 10]
dados = dict(zip(carros, valores))# junta as duas listas em um dicionário

print(sum(dados.values()))#somando apenas os valores de um dicionario

def media():#Funçao sem parametro
    valor = (1 + 2 + 3)/3
    print(valor)

media()

def mediaTeste(soma):#Função com parametro
    valor = (soma)/3
    print(valor)

soma = sum(dados.values())
mediaTeste(soma)


def mediaLista(lista):#Função passando uma lista como parametro
    valor = sum(lista) / len(lista)
    print(valor)

mediaLista(dados.values())


def mediaListaRetornandoValor(lista):#Função passando uma lista como parametro e retornando algo
    valor = sum(lista) / len(lista)
    return valor

resultado = mediaListaRetornandoValor(dados.values())
print(resultado)


def mediaListaRetornandoDoisValores(lista):#Função passando uma lista como parametro e retornando dois registros
    valor = sum(lista) / len(lista)
    return (valor, len(lista))

resultado = mediaListaRetornandoDoisValores(dados.values())#posso atribuir tudo em uma variavel
print(resultado)

resultado, tamanho = mediaListaRetornandoDoisValores(dados.values())#ou posso atribuir a duas variaveis
print(resultado, tamanho)
'''
#----------------------------------------------------------------------


#Trabalhando com Pandas
#----------------------------------------------------------------------
'''
#Criando dataframe a partir de uma lista de dicionarios
marcas = [{'Mercedes': 'A20', 'BMW': 'i360', 'Audi': 'A4'}]
datasetMarcas = pd.DataFrame(marcas)
print(datasetMarcas)

#Criando dataframe a partir de uma list
carros = ['Mercedes', 'BMW', 'Audi']
valores = [10, 10, 10]
dados = list(zip(carros, valores))# junta as duas listas em um dicionário
d = pd.DataFrame(dados)
print(d)

#Criando um dataframe a partir de dados externos
import pandas as pd

dataset = pd.read_csv('db.csv', sep = ';', index_col = 0)

print(dataset['Valor'])#Selecionando a coluna Valor -> retorna um series
print(dataset[['Valor']])#Selecionando a coluna Valor -> retorna um dataframe


#Loc -> Baseado em linhas e colunas
print(dataset.loc['Passat'])#Seleciona um grupo de linhas do filtro passado
print(dataset.loc[['Passat', 'DS5']])#Retorna um dataframe com esses dois registros
print(dataset.loc[['Passat', 'DS5'],['Motor', 'Valor']])#Filtra os dois Registros ('Passat', 'DS5') e exibe somente as colunas Motor e Valor
print(dataset.loc[:,['Motor', 'Valor']])#não passa nenhum filtro e exibe somente as colunas Motor e Valor


#Iterando com Pandas
for indice, linha in dataset.iterrows():#iterrows() cria uma lista com tuplas
    if(2019 - linha['Ano'] != 0):#Se 2019 menos a Ano que retorna da linha for diferente de 0 ele entra
        dataset.loc[indice, 'km_media'] = linha['Quilometragem'] / (2019 - linha['Ano'])#Estou criando uma coluna calculada chamada km_media
    else:
        dataset.loc[indice, 'km_media'] = 0# se não entrar no If eu crio essa coluna com o valor 0
print(dataset)


#Tratamento de dados
print(dataset.info())#Exibe os detalhes do dataframe
print(dataset[dataset.Quilometragem.isna()])#Retorna os registros em que a Quilometragem está com valor (NaN)
dataset.fillna(0, inplace = True)#Substitui o valor (NAN) para 0
print(dataset.query("Zero_km == True"))#Usa o metodo Query para selecionar

import pandas as pd
datasetTeste = pd.read_csv('db.csv', sep = ';', index_col = 0)
datasetTeste.dropna(subset = ['Quilometragem'], inplace = True)#Elimina todos os registros que a Quilometragem é NaN
print(datasetTeste)
'''
#----------------------------------------------------------------------