from modelo import Filme
from modelo import Serie
print("TESTE - Modelo - Inicio")
vingadores = Filme("vingadores - guerra infinita", 2018, 160)
print(f"Nome: {vingadores.nome} - Ano: {vingadores.ano} "
      f"- Duração: {vingadores.duracao}")

atlanta = Serie("atlanta", 2018, 2)
print(f"Nome: {atlanta.nome} - Ano: {atlanta.ano} "
      f"- Temporadas: {atlanta.temporadas}")