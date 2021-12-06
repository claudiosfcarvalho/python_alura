idades = [15, 87, 32, 65, 56, 32, 49, 37]

for idade in idades:
    print(idade)


for i in range(len(idades)):
    print("range -", i, idades[i])


print(enumerate(idades))

print(list(enumerate(idades)))

for i in enumerate(idades):
    print(i)

for indice, idade in enumerate(idades):
    print(indice, "x", idade)

usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]

for usuario in usuarios:
    print(usuario)

#desempacotando a tupla
for nome, idade, nascimento in usuarios:
    print(nome)

#Ignorando a segunda e terceira posição
for nome, _, _ in usuarios:
    print(nome)