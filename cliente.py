
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    # properties - define acesso direto a função sem a necessidade de colocar ()
    @property
    def nome(self):
        print("chamando @property nome()")
        # retorna primeira letra em maiuscula
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome