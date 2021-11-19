class Conta:

    # Construtor
    def __init__(self, numero, titular, saldo, limite):
        print(f"Contruindo objeto ...{self}")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"Saldo {self.saldo} do titular {self.titular}")

    def deposita(self, valor):
        print(f"Depósito de R${valor} na conta {self.numero}")
        self.saldo += valor

    def saca(self, valor):
        print(f"Saque de R${valor} da conta {self.numero}")
        self.saldo -= valor