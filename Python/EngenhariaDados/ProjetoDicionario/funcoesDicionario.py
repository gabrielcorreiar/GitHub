import mmap

def perguntar():

        return input("O que deseja realizar?\n" +
                     "<I> - Para inserir um usuário\n" +
                     "<P> - Para pesquisar um usuário\n" +
                     "<E> - Para Excluir um usuário\n" +
                     "<L> - Para listar um usuário:").upper()


def inserir(dicionario):

    dicionario[input("Digite um login: ").upper()] = [input("Digite o nome: ").upper(),
                                                      input("Digite a última data de acesso: "),
                                                      input("Qual a última estação acessada: ").upper()]
    salvar(dicionario)


def salvar(dicionario):

    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write("\n" + chave + ":" + str(valor))

def pesquisar():
    with open("bd.txt", "r") as arquivo:

        for linha in arquivo.readlines():
            print(linha)

def listar(chave):

    with open('bd.txt', 'rb', 0) as file:
        for linha in file.readlines():
            if linha.find(chave) != -1:
                print('true')
                print(linha)

def deletar(chave):

    a = []
    with open('bd.txt', 'r+') as file:
        for linha in file.readlines():
            if linha.find(chave) == -1:
                a.append(linha)

    with open('bd.txt', 'w') as file:
        for linha in a:
            print(linha)
            file.write(linha)

