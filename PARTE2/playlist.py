
class Playlist:

    def __init__(self, nome, programas):
        self.__nome = nome
        self._programas = programas

    #Torna a classa iterable
    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

    @property
    def nome(self):
        return self.nome

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)

    def add_item(self, programa):
        self._programas.append(programa)

