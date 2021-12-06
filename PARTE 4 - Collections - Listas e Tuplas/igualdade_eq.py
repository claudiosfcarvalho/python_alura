from abc import ABCMeta, abstractmethod

'''
    a classe conta virou uma classe abstrata por conta de usar o metaclass e o abstractmethod
    forçando que todos os filhos são forçado a implementar  os metodos marcado como abstractmethod
    caso contrario dará erro ao instanciar
'''


class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return f"[>>Codigo {self.codigo} Saldo {self.saldo}<<]"


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self.saldo -= 2


class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self.saldo *= 1.01
        self.saldo -= 3


class ContaInvestimento(Conta):
    pass

class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False

        return self._codigo == other._codigo and self._saldo == other._saldo


conta1 = ContaSalario(37)
conta2 = ContaSalario(37)
print(conta1 == conta2)

conta3 = ContaCorrente(37)
print(conta1 == conta3)
print(isinstance(conta1, ContaCorrente))

