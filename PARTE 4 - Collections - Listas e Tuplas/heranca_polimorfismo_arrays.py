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


print(Conta(88))

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)

contas = [conta16, conta17]
for conta in contas:
    conta.passa_o_mes()
    print(conta)

# array - usar apenas para trabalhar com numeros, pois otimiza o armazenamento
#       quando necessita alto desempenho usar o NumPy
import array as arr

arr.array('d', [1, 3.5])

import numpy as np

np.array([1, 3.5])

conta_investimento = ContaInvestimento(1234)
