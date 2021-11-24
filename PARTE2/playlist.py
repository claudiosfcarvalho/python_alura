
class Playlist(list):

    def __init__(self, nome, programas):
        self.__nome = nome
        super().__init__(programas)

    @property
    def nome(self):
        return self.nome

