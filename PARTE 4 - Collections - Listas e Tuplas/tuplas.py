class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f"[>>Codigo {self.codigo} Saldo {self.saldo}<<]"


conta_do_gui = ContaCorrente(15)
print(conta_do_gui)
conta_do_gui.deposita(500)
print(conta_do_gui)

conta_da_dani = ContaCorrente(47685)
print(conta_da_dani)
conta_da_dani.deposita(1000)
print(conta_da_dani)

contas = [conta_do_gui, conta_da_dani]
print(contas)

for conta in contas:
    print(conta)

print(contas[1])


def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)


print(contas[0], contas[1])
deposita_para_todas(contas)
print(contas[0], contas[1])

# tupla - lista imutável, nao pode adicionar ou remover itens
('Guilherme', 37, 1981)  # tupla


def deposita(conta):  # programacao funcinal separando o comportamento dos dados
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return codigo, novo_saldo


conta_do_gui_tupla = (15, 1000)
print(conta_do_gui_tupla)
conta_do_gui_tupla = deposita(conta_do_gui_tupla)
print(conta_do_gui_tupla)

guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 31, 1987)
usuarios = [guilherme, daniela]
usuarios.append(('Paulo', 39, 1979))

conta_do_gui = ContaCorrente(500)
conta_do_gui.deposita(500)
conta_da_dani = ContaCorrente(234876)
conta_da_dani.deposita(1000)
contas = (conta_do_gui, conta_da_dani)



