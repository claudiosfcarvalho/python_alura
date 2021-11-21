from modelo import Filme
from modelo import Serie

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