## Lendo Arquivo gerado (Poucas linhas)
with open("MeuPrimeiroArquivo.txt","r") as arquivo:

    for linha in arquivo.readlines():
        print(linha)

## Lendo um arquivo maior (Base de dados Iris)
database = []
with open("iris.data", "r") as arquivo_iris:
    for registro in arquivo_iris:
        database.append(registro.split(","))

print(database)
print(float(database[0][0]) + float(database[0][1]))