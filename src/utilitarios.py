"""
Funcoes utilitarias compartilhadas pelo projeto.
"""


def reconstruir_caminho(estado_final):
    """
    Reconstrui o caminho da solucao a partir do estado final.

    TODO:
    - Percorrer os ponteiros para estados anteriores.
    - Inverter a ordem do caminho.
    - Retornar a lista de estados desde o inicial ate o objetivo.
    """
    pass


def verificar_solubilidade(valores):
    """
    Verifica se uma configuracao do 8-Puzzle pode chegar ao estado objetivo.

    TODO:
    - Contar o numero de inversoes.
    - Considerar que, no tabuleiro 3x3, estados soluveis possuem numero par de inversoes.
    - Ignorar o espaco vazio na contagem.
    """
    pass


def ler_estado_de_texto(texto):
    """
    Converte uma linha de texto em uma tupla de inteiros.

    Exemplo esperado:
        "1 2 3 4 5 6 7 8 0"

    TODO:
    - Validar quantidade de valores.
    - Validar repeticoes.
    - Retornar mensagens de erro amigaveis.
    """
    pass
