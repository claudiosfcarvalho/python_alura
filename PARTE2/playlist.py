
class FilmesESeries:
    __lista = []

    def add_item(self, programa):
        self.__lista.append(programa)

    @property
    def lista(self):
        return self.__lista
