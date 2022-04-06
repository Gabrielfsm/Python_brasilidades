import requests

class BuscaEndereco:

    def __init__(self, cep):
        if self.cep_eh_valido(str(cep)):
            self.cep = str(cep)
        else:
            raise ValueError("CEP inválido!")

    def __str__(self):
        return self.format_cep()

    def cep_eh_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return (f"{self.cep[:5]}-{self.cep[5:]}")

    def acessa_via_cep(self):
        url = (f"https://viacep.com.br/ws/{self.cep}/json/")
        r = requests.get(url)
        dados = r.json()
        return (
            dados["bairro"],
            dados["localidade"],
            dados["uf"]
        )
