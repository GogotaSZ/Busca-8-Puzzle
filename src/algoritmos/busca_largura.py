"""Busca em Largura (BFS) para o 8-Puzzle."""

from collections import deque
from time import perf_counter

from estado_puzzle import EstadoPuzzle
from sucessores import gerar_sucessores


def _normalizar_estado(estado):
    """Cria um no independente a partir de valores ou de um EstadoPuzzle."""
    if isinstance(estado, EstadoPuzzle):
        return EstadoPuzzle(estado.valores)
    return EstadoPuzzle(estado)


def buscar(estado_inicial, estado_objetivo):
    """Resolve o 8-Puzzle usando Busca em Largura (BFS).

    A BFS expande os nos por nivel, garantindo a menor quantidade de movimentos
    quando todos os movimentos possuem custo 1.

    Returns:
        Uma tupla ``(no_final, metricas)``. ``no_final`` e o ``EstadoPuzzle``
        objetivo, com ponteiros para reconstruir o caminho, ou ``None``. O
        dicionario ``metricas`` contem ``nos_visitados``, ``nos_gerados``,
        ``profundidade`` e ``tempo_execucao``.
    """
    no_inicial = _normalizar_estado(estado_inicial)
    valores_objetivo = (
        estado_objetivo.valores
        if isinstance(estado_objetivo, EstadoPuzzle)
        else tuple(estado_objetivo)
    )

    inicio = perf_counter()
    fila = deque([no_inicial])
    descobertos = {no_inicial.valores}
    nos_visitados = 0
    nos_gerados = 1

    while fila:
        no_atual = fila.popleft()
        nos_visitados += 1

        if no_atual.valores == valores_objetivo:
            return no_atual, {
                "nos_visitados": nos_visitados,
                "nos_gerados": nos_gerados,
                "profundidade": no_atual.custo_g,
                "tempo_execucao": perf_counter() - inicio,
            }

        for filho in gerar_sucessores(no_atual):
            if filho.valores not in descobertos:
                descobertos.add(filho.valores)
                fila.append(filho)
                nos_gerados += 1

    return None, {
        "nos_visitados": nos_visitados,
        "nos_gerados": nos_gerados,
        "profundidade": None,
        "tempo_execucao": perf_counter() - inicio,
    }
