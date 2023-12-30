import requests

class Pessoa:
    def __init__(self, nome: str, sobrenome: str) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos = False

    def obterTodosOsDados(self):
        resposta = requests.get('')

        if resposta.ok:
            self.dados_obtidos = True
            return 'conectado'
        
        self.dados_obtidos = False
        return 'falha'