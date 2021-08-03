import requests
link = "https://87dyrojjxk.execute-api.us-east-1.amazonaws.com/dev/fiap/raw"
teste = requests.get(link)
a = teste.text
print(a)

for linha in a.split('}]}]}]},'):
    print(linha + "\n\n\n\n\n")