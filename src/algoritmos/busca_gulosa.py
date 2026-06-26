"""Busca Gulosa (Best-First Search) para o 8-Puzzle."""

from heapq import heappop, heappush
from itertools import count
from time import perf_counter

from estado_puzzle import EstadoPuzzle
from sucessores import gerar_sucessores


def _como_estado_puzzle(estado):
    """Aceita tanto um ``EstadoPuzzle`` quanto uma lista/tupla de valores."""
    return estado if isinstance(estado, EstadoPuzzle) else EstadoPuzzle(estado)


def distancia_manhattan(valores, objetivo):
    """Calcula a distancia de Manhattan, ignorando o espaco vazio."""
    posicoes_objetivo = {peca: indice for indice, peca in enumerate(objetivo)}
    distancia = 0
    for indice, peca in enumerate(valores):
        if peca:
            indice_objetivo = posicoes_objetivo[peca]
            distancia += abs(indice // 3 - indice_objetivo // 3)
            distancia += abs(indice % 3 - indice_objetivo % 3)
    return distancia


def buscar(estado_inicial, estado_objetivo=(1, 2, 3, 4, 5, 6, 7, 8, 0), heuristica=None):
    """Executa a Busca Gulosa ordenando a fronteira apenas por ``h(n)``.

    Por padrao, usa a distancia de Manhattan. Uma funcao ``heuristica``
    alternativa pode ser informada e deve receber ``(valores, objetivo)``.
    O retorno contem: no objetivo, nos visitados, nos gerados e tempo em s.
    """
    inicio = _como_estado_puzzle(estado_inicial)
    objetivo = _como_estado_puzzle(estado_objetivo).valores
    avaliar = heuristica or distancia_manhattan
    inicio.custo_h = avaliar(inicio.valores, objetivo)

    inicio_tempo = perf_counter()
    desempate = count()
    fronteira = [(inicio.custo_h, next(desempate), inicio)]
    descobertos = {inicio.valores}
    nos_visitados = 0
    nos_gerados = 1  # inclui o no inicial

    while fronteira:
        _, _, atual = heappop(fronteira)
        nos_visitados += 1

        if atual.valores == objetivo:
            return atual, nos_visitados, nos_gerados, perf_counter() - inicio_tempo

        for sucessor in gerar_sucessores(atual):
            if sucessor.valores in descobertos:
                continue

            descobertos.add(sucessor.valores)
            sucessor.custo_h = avaliar(sucessor.valores, objetivo)
            heappush(fronteira, (sucessor.custo_h, next(desempate), sucessor))
            nos_gerados += 1

    return None, nos_visitados, nos_gerados, perf_counter() - inicio_tempo
