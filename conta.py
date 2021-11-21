class Conta:

    # Construtor
    def __init__(self, numero, titular, saldo, limite):
        print(f"Contruindo objeto ...{self}")
        # os dois underscore antes do campo indica campo privado
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
