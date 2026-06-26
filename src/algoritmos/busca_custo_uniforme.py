"""Busca de Custo Uniforme para o 8-Puzzle."""

from heapq import heappop, heappush
from itertools import count
from time import perf_counter

from estado_puzzle import EstadoPuzzle
from sucessores import gerar_sucessores


def _como_estado_puzzle(estado):
    """Aceita tanto um ``EstadoPuzzle`` quanto uma lista/tupla de valores."""
    return estado if isinstance(estado, EstadoPuzzle) else EstadoPuzzle(estado)


def buscar(estado_inicial, estado_objetivo=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
    """Encontra o caminho de menor custo acumulado ate ``estado_objetivo``.

    Cada movimento do puzzle tem custo 1. O retorno e uma tupla contendo o no
    objetivo (ou ``None``), nos visitados, nos gerados e tempo em segundos.
    """
    inicio = _como_estado_puzzle(estado_inicial)
    objetivo = _como_estado_puzzle(estado_objetivo).valores
    inicio_tempo = perf_counter()
    desempate = count()
    fronteira = []
    heappush(fronteira, (inicio.custo_g, next(desempate), inicio))

    # Menor custo conhecido para cada configuracao. Evita ciclos e permite
    # reabrir um estado caso apareca um caminho estritamente mais barato.
    melhor_custo = {inicio.valores: inicio.custo_g}
    nos_visitados = 0
    nos_gerados = 1  # inclui o no inicial

    while fronteira:
        custo_atual, _, atual = heappop(fronteira)
        if custo_atual != melhor_custo.get(atual.valores):
            continue

        nos_visitados += 1
        if atual.valores == objetivo:
            return atual, nos_visitados, nos_gerados, perf_counter() - inicio_tempo

        for sucessor in gerar_sucessores(atual):
            custo_sucessor = sucessor.custo_g
            if custo_sucessor < melhor_custo.get(sucessor.valores, float("inf")):
                melhor_custo[sucessor.valores] = custo_sucessor
                heappush(fronteira, (custo_sucessor, next(desempate), sucessor))
                nos_gerados += 1

    return None, nos_visitados, nos_gerados, perf_counter() - inicio_tempo
