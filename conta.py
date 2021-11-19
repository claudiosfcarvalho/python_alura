

class Conta:

    #Construtor
    def __init__(self, numero, titular, saldo, limite):
        print(f"Contruindo objeto ...{self}")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
