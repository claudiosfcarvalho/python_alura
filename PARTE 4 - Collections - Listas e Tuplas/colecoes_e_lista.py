# lista
idades = [39, 30, 27, 18]
print(idades[0])
print(len(idades))
idades.append(15)
print(idades)
idades.remove(30)
print(idades)
# idades.clear()
# print(idades)

print(15 in idades)
idades.insert(2, 10)
idades.extend([45, 56, 78])
print(idades)

idades_no_ano_que_vem = []
for idade in idades:
    idades_no_ano_que_vem.append(idade + 1)
print(idades_no_ano_que_vem)

idades_no_ano_que_vem2 = [(idade + 1) for idade in idades]
print(idades_no_ano_que_vem2)

idades_maior_que_21 = [(idade) for idade in idades if idade > 21]
print(idades_maior_que_21)


def faz_processamento_de_visualizacao(lista = None):
    if lista == None:
        lista = list()
    print(len(lista))
    lista.append(13)
    print(lista)


faz_processamento_de_visualizacao(idades)
faz_processamento_de_visualizacao(idades)
faz_processamento_de_visualizacao()
