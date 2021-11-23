from modelo import Filme
from modelo import Serie
from playlist import FilmesESeries
print("TESTE - Modelo - Inicio")
vingadores = Filme("vingadores - guerra infinita", 2018, 160)
vingadores.dar_like()
print(f"Nome: {vingadores.nome} - Ano: {vingadores.ano} "
      f"- Duração: {vingadores.duracao} "
      f"- Likes: {vingadores.likes}")

atlanta = Serie("atlanta", 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
print(f"Nome: {atlanta.nome} - Ano: {atlanta.ano} "
      f"- Temporadas: {atlanta.temporadas} "
      f"- Likes: {atlanta.likes}")

lista_filmes = FilmesESeries()
lista_filmes.add_item(vingadores)
lista_filmes.add_item(atlanta)
indice = 1
for programa in lista_filmes.lista:
      #detalhes = programa.duracao + " min " if hasattr(programa, 'duracao') else programa.temporadas + "Temp"
      if hasattr(programa, 'duracao'):
            detalhes = f"{programa.duracao} min "
      else:
            detalhes = f"{programa.temporadas} Temporadas"
      print(f"{indice} -> {programa.nome} - {detalhes} - {programa.likes}")
      indice += 1