"""Implementação da busca em profundidade (DFS) para o 8-Puzzle."""

from time import perf_counter

from estado_puzzle import EstadoPuzzle
from sucessores import gerar_sucessores


def _normalizar_estado(estado):
    """Cria um nó inicial independente a partir de valores ou de um EstadoPuzzle."""
    if isinstance(estado, EstadoPuzzle):
        return EstadoPuzzle(estado.valores)
    return EstadoPuzzle(estado)


def buscar(estado_inicial, estado_objetivo, limite_profundidade=None):
    """Resolve o 8-Puzzle com busca em profundidade (DFS) iterativa.

    Args:
        estado_inicial: Sequência de nove valores ou ``EstadoPuzzle`` inicial.
        estado_objetivo: Sequência de nove valores ou ``EstadoPuzzle`` objetivo.
        limite_profundidade: Profundidade máxima opcional. Quando ``None``, a
            busca percorre todo o espaço de estados alcançável, se necessário.

    Returns:
        Uma tupla ``(no_final, metricas)``. ``no_final`` é o ``EstadoPuzzle``
        objetivo, com ponteiros para reconstruir o caminho, ou ``None``. O
        dicionário ``metricas`` contém ``nos_visitados``, ``nos_gerados``,
        ``profundidade`` e ``tempo_execucao``.

    Raises:
        ValueError: Se ``limite_profundidade`` não for ``None`` ou um inteiro
            não negativo.
    """
    if (
        limite_profundidade is not None
        and (
            isinstance(limite_profundidade, bool)
            or not isinstance(limite_profundidade, int)
            or limite_profundidade < 0
        )
    ):
        raise ValueError("O limite de profundidade deve ser um inteiro não negativo ou None.")

    no_inicial = _normalizar_estado(estado_inicial)
    valores_objetivo = (
        estado_objetivo.valores
        if isinstance(estado_objetivo, EstadoPuzzle)
        else tuple(estado_objetivo)
    )

    inicio = perf_counter()
    pilha = [no_inicial]
    explorados = set()
    na_fronteira = {no_inicial.valores}
    nos_visitados = 0
    nos_gerados = 1

    while pilha:
        no_atual = pilha.pop()
        na_fronteira.discard(no_atual.valores)

        # A proteção é mantida mesmo com o conjunto da fronteira para garantir
        # que um estado nunca seja expandido mais de uma vez.
        if no_atual.valores in explorados:
            continue

        explorados.add(no_atual.valores)
        nos_visitados += 1

        if no_atual.valores == valores_objetivo:
            return no_atual, {
                "nos_visitados": nos_visitados,
                "nos_gerados": nos_gerados,
                "profundidade": no_atual.custo_g,
                "tempo_execucao": perf_counter() - inicio,
            }

        # O nó no limite ainda é visitado, mas não gera descendentes.
        if limite_profundidade is not None and no_atual.custo_g >= limite_profundidade:
            continue

        # A função de sucessores produz Cima, Baixo, Esquerda e Direita.
        # A inversão preserva essa prioridade ao retirar itens de uma pilha LIFO.
        for filho in reversed(gerar_sucessores(no_atual)):
            if filho.valores not in explorados and filho.valores not in na_fronteira:
                pilha.append(filho)
                na_fronteira.add(filho.valores)
                nos_gerados += 1

    return None, {
        "nos_visitados": nos_visitados,
        "nos_gerados": nos_gerados,
        "profundidade": None,
        "tempo_execucao": perf_counter() - inicio,
    }
