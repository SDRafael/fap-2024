
import requests

def consultarRua(numeroCep):
    url2 = 'https://viacep.com.br/ws/{}/json/'.format(numeroCep)
    req2 = requests.get(url2, timeout=3)
    endere2 = req2.json()

    endereco = {
        "CEP": endere2["cep"],
        "Rua": endere2["logradouro"],
        "Bairro": endere2["bairro"],
        "Cidade": endere2["localidade"]
    }

    return endereco


numeroCep = input('Digite o cep: ')
while numeroCep.lower() != 'sair':
    con = consultarRua(numeroCep)
    print(con)
    numeroCep = input('Digite o cep: ')
