idades = [15, 87, 32, 65, 56, 32, 49, 37]

usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]

print(sorted(idades))
print(reversed(idades))
print(list(reversed(idades)))
print(sorted(idades, reverse=True))

print(idades.sort())
print(idades)

#ordenação customizada
nomes = ["Guilherme", "Daniela", "Paulo"]
print(sorted(nomes))
nomes = ["guilherme", "Daniela", "Paulo"]
print(sorted(nomes))


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

    def __lt__(self, other):
        return self._saldo < other._saldo


conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

for conta in contas:
    print(conta)

def extrai_saldo(conta):
    return conta._saldo

print(sorted(contas, key=extrai_saldo))
for conta in sorted(contas, key=extrai_saldo):
    print(conta)

from operator import attrgetter
for conta in sorted(contas, key=attrgetter("_saldo")):
    print("operator -",conta)

print(conta_do_guilherme < conta_da_daniela)

for conta in sorted(contas):
    print("ordenado depois de implementar __lt__", conta)



conta_do_guilherme1 = ContaSalario(17)
conta_do_guilherme1.deposita(500)

conta_da_daniela1 = ContaSalario(3)
conta_da_daniela1.deposita(1000)

conta_do_paulo1 = ContaSalario(133)
conta_do_paulo1.deposita(500)

contas1 = [conta_do_guilherme1, conta_da_daniela1, conta_do_paulo1]
for conta in sorted(contas1, key=attrgetter("_saldo", "_codigo")):
    print("operator2 -",conta)


class ContaSalario1:
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

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo

        return self._codigo < other._codigo

conta_do_guilherme2 = ContaSalario1(17)
conta_do_guilherme2.deposita(500)

conta_da_daniela2 = ContaSalario1(3)
conta_da_daniela2.deposita(500)

conta_do_paulo2 = ContaSalario1(133)
conta_do_paulo2.deposita(500)
contas2 = [conta_do_guilherme2, conta_da_daniela2, conta_do_paulo2]
for conta in sorted(contas2):
    print("ordenacao lt chave dupla: ", conta)


#total ordering para definir equal e maior e do restante faz sozinho
from functools import total_ordering
@total_ordering
class ContaSalario2:
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

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo

        return self._codigo < other._codigo

conta_do_guilherme3 = ContaSalario2(17)
conta_do_guilherme3.deposita(500)

conta_da_daniela3 = ContaSalario2(3)
conta_da_daniela3.deposita(1000)

conta_do_paulo3 = ContaSalario2(133)
conta_do_paulo3.deposita(500)
contas3 = [conta_do_guilherme3, conta_da_daniela3, conta_do_paulo3]
for conta in sorted(contas3):
    print("ordenacao total ordering: ", conta)

print(conta_do_guilherme3 <= conta_da_daniela3)