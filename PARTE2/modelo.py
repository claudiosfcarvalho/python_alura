from programa import Programa

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano, 0)
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano, 0)
        self.temporadas = temporadas

    def __str__(self):
        return f"Nome: {self.nome} - Ano: {self.ano} - Temporadas: {self.temporadas}"
