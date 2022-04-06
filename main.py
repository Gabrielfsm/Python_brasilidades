import requests
from acesso_cep import BuscaEndereco

cep = 58432532
objeto_cep = BuscaEndereco(cep)
# print(objeto_cep)

# r = requests.get("https://viacep.com.br/ws/58432532/json/")
# print(r.text)

bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)
