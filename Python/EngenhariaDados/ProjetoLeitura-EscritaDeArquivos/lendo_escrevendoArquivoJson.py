import json
# #Lendo um arquivo Json
# dicionario = []
# with open("bd.json", "r") as arquivo_json:
#     dicionario = json.load(arquivo_json)
#     for chave, dados in dicionario.items():
#         print(chave + " | " + str(dados))
#
#
# #Escrevendo um arquivo Json
# with open("bd2.json", "w") as arquivo_json2:
#     json.dump(dicionario,arquivo_json2)

# import requests
# link = "https://87dyrojjxk.execute-api.us-east-1.amazonaws.com/dev/fiap/ranking?skip=1&take=20"
# teste = requests.get(link)
# a = teste.text
# print(a)
#
# for linha in a.split(','):
#     print(linha)


import requests
link = "https://87dyrojjxk.execute-api.us-east-1.amazonaws.com/dev/fiap/raw"
teste = requests.get(link)
a = teste.text
print(a)

for linha in a.split(','):
    print(linha)
