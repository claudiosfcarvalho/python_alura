from programa import Programa


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano, 0)
        self.duracao = duracao

    def imprime(self):
        return f"{self.nome} - Ano {self.ano} - {self.duracao} min - {self.likes} Likes"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano, 0)
        self.temporadas = temporadas

    def imprime(self):
        return f"{self.nome} - Ano {self.ano} - {self.temporadas} temporadas - {self.likes} Likes"
