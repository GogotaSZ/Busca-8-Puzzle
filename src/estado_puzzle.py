"""
Representacao do estado do 8-Puzzle.

O estado sera representado por uma tupla com 9 valores inteiros.
O numero 0 representa o espaco vazio.

Exemplo:
    (1, 2, 3, 4, 5, 6, 7, 8, 0)
"""


class EstadoPuzzle:
    """
    Representa uma configuracao do tabuleiro do 8-Puzzle.

    TODO:
    - Validar se o estado possui exatamente 9 posicoes.
    - Validar se os numeros de 0 a 8 aparecem uma unica vez.
    - Guardar custo acumulado, profundidade e referencia ao estado anterior.
    - Facilitar a reconstrucao do caminho da solucao.
    """

    def __init__(self, valores, anterior=None, movimento=None, custo=0, profundidade=0):
        self.valores = tuple(valores)
        self.anterior = anterior
        self.movimento = movimento
        self.custo = custo
        self.profundidade = profundidade

    def __eq__(self, outro):
        return isinstance(outro, EstadoPuzzle) and self.valores == outro.valores

    def __hash__(self):
        return hash(self.valores)

    def __repr__(self):
        return f"EstadoPuzzle(valores={self.valores})"

    def formatar(self):
        """
        Retorna uma representacao textual do tabuleiro em formato 3x3.

        TODO:
        - Melhorar a exibicao do espaco vazio.
        - Permitir formatos alternativos para relatorios e logs.
        """
        linhas = []
        for indice in range(0, 9, 3):
            linha = self.valores[indice:indice + 3]
            linhas.append(" ".join(str(valor) for valor in linha))
        return "\n".join(linhas)
