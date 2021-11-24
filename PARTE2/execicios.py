from modelo import Filme
from modelo import Serie
from playlist import Playlist
print("TESTE - Modelo - Inicio")
vingadores = Filme("vingadores - guerra infinita", 2018, 160)
vingadores.dar_like()
# print(f"Nome: {vingadores.nome} - Ano: {vingadores.ano} "
#       f"- Duração: {vingadores.duracao} "
#       f"- Likes: {vingadores.likes}")

atlanta = Serie("atlanta", 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
# print(f"Nome: {atlanta.nome} - Ano: {atlanta.ano} "
#       f"- Temporadas: {atlanta.temporadas} "
#       f"- Likes: {atlanta.likes}")

lista_filmes = Playlist("Fim de Semana",[vingadores, atlanta])
lista_filmes.add_item(Filme("Batman", 2018, 160))
lista_filmes.add_item(Filme("Era do gelo", 2018, 160))

indice = 1
print("Vingadores está na lista? ",vingadores in lista_filmes.listagem)
for programa in lista_filmes.listagem:
      print(f"{indice} -> {programa}")
      indice += 1