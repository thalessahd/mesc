# 3) Considerando este código (https://github.com/carlosbazilio/mesc/blob/main/github.py), 
# o qual imprime na tela os dados recebidos do acesso a api do github para a minha conta, 
# crie uma função para, dado o valor de um cep, exibir os dados postais referentes a este cep. Para tal,
# use a api descrita neste site (https://viacep.com.br/), a qual foi comentada brevemente em sala.

import requests
import sys

def getAddress(cep):
    cleanCep = cep.replace('-', '')
    url = 'https://viacep.com.br/ws/'+cleanCep+'/json/'
    response = requests.get(url)
    if response.status_code != 200:
        return 'Erro na consulta'
    else:
        return response.json()

address = getAddress(sys.argv[1])
print(address)
