from conta import Conta
from cliente import Cliente

# Teste Conta
print("TESTE - Conta - Inicio")
conta = Conta(123, "Nico", 55.5, 1000.0)
print(conta.titular)
print(conta.codigo_banco)
print(conta.numero)
print(conta.saldo)
print("limite padrão", conta.limite)
conta.limite = 1200.0
print("limite após o set", conta.limite)
conta.saca(1000)
conta.saca(1500)

print("TESTE - Conta - Fim\n\n-----------------\n")

# Teste cliente

print("TESTE - Cliente - Inicio")
cliente = Cliente("marco")
print(cliente.nome)
cliente.nome = "jose"
print(cliente.nome)


print("TESTE - Cliente - Fim\n\n-----------------\n")