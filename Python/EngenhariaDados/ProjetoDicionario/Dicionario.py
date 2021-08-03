from EngenhariaDados.ProjetoDicionario.funcoesDicionario import *

usuarios = {}
opcao = perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":

    if opcao == "I":
        inserir(usuarios)

    if opcao == "P":
        pesquisar()

    if opcao == "E":

        palavra = input("Digite um valor para procurar: ").upper()
        deletar(palavra)


    if opcao == "L":
        palavra = input("Digite um valor para procurar: ").upper()
        palavra_tratata = bytes(palavra, encoding="utf-8")
        listar(palavra_tratata)

    opcao = perguntar()