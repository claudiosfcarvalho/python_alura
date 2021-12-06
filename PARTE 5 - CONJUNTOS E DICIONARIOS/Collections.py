usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]
assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(assistiram)
#usando o conjunto remove os duplicados // nao pode acessar o indice pois nao existe
print(set(assistiram))
for a in set(assistiram):
    print(a)

# o set pode usar o {}
usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}
print(usuarios_data_science | usuarios_machine_learning)