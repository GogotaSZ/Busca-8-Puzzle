"""
Geracao de sucessores para o 8-Puzzle.

Este modulo sera responsavel por listar todos os movimentos validos a partir
de um estado atual.
"""


MOVIMENTOS = {
    "cima": -3,
    "baixo": 3,
    "esquerda": -1,
    "direita": 1,
}


def gerar_sucessores(estado_atual):
    """
    Gera os estados sucessores validos para o estado atual.

    TODO:
    - Localizar a posicao do espaco vazio.
    - Verificar quais movimentos sao validos.
    - Criar novos objetos EstadoPuzzle para cada movimento.
    - Registrar o movimento realizado em cada sucessor.
    - Incrementar custo e profundidade.
    """
    pass


def movimento_valido(posicao_vazio, movimento):
    """
    Verifica se um movimento pode ser aplicado ao espaco vazio.

    TODO:
    - Impedir movimentos para fora do tabuleiro.
    - Tratar corretamente as bordas esquerda e direita.
    """
    pass
