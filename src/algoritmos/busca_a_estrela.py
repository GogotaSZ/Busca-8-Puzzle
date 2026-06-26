"""Implementacao do algoritmo de busca A* (A-Estrela)."""

import heapq
from time import perf_counter

from estado_puzzle import EstadoPuzzle
from heuristicas.conflito_linear import calcular_conflito_linear
from heuristicas.distancia_manhattan import calcular_manhattan
from heuristicas.pecas_fora_lugar import calcular_pecas_fora_lugar
from sucessores import gerar_sucessores


OBJETIVO_VALORES = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def busca_a_estrela(estado_inicial_valores, opcao_heuristica):
    """Executa o A* para encontrar o caminho mais curto ate o objetivo.

    Returns:
        Uma tupla contendo o no objetivo (ou ``None``), nos visitados, nos
        gerados e tempo de execucao em segundos.
    """
    inicio_tempo = perf_counter()
    no_objetivo = EstadoPuzzle(valores=OBJETIVO_VALORES)
    funcoes_heuristica = {
        "1": calcular_pecas_fora_lugar,
        "2": calcular_manhattan,
        "3": calcular_conflito_linear,
    }

    heuristica_escolhida = funcoes_heuristica.get(opcao_heuristica)
    if not heuristica_escolhida:
        raise ValueError("Opcao de heuristica invalida.")

    no_inicial = EstadoPuzzle(valores=estado_inicial_valores)
    no_inicial.custo_h = heuristica_escolhida(no_inicial, no_objetivo)

    fronteira = []
    heapq.heappush(fronteira, no_inicial)
    explorados = set()
    nos_visitados = 0
    nos_gerados = 1  # inclui o no inicial

    while fronteira:
        no_atual = heapq.heappop(fronteira)

        if no_atual.valores in explorados:
            continue

        nos_visitados += 1

        if no_atual.valores == OBJETIVO_VALORES:
            return no_atual, nos_visitados, nos_gerados, perf_counter() - inicio_tempo

        explorados.add(no_atual.valores)

        for filho in gerar_sucessores(no_atual):
            if filho.valores not in explorados:
                filho.custo_h = heuristica_escolhida(filho, no_objetivo)
                heapq.heappush(fronteira, filho)
                nos_gerados += 1

    return None, nos_visitados, nos_gerados, perf_counter() - inicio_tempo
