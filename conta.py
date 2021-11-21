class Conta:

    # Construtor
    def __init__(self, numero, titular, saldo, limite):
        print(f"Contruindo objeto ...{self}")
        # os dois underscore antes do campo indica campo 'privado'
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo {self.__saldo} do titular {self.__titular}")

    def deposita(self, valor):
        print(f"Depósito de R${valor} na conta {self.__numero}")
        self.__saldo += valor

    def saca(self, valor):
        print(f"Saque de R${valor} da conta {self.__numero}")
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        print("chamando @property saldo()")
        return self.__saldo

    @property
    def titular(self):
        print("chamando @property titular()")
        return self.__titular

    @property
    def limite(self):
        print("chamando @property limite()")
        return self.__limite

    @limite.setter
    def limite(self, valor):
        print("chamando setter limite()")
        self.__limite = valor