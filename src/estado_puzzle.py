"""
Representacao do estado do 8-Puzzle.

O estado sera representado por uma tupla com 9 valores inteiros.
O numero 0 representa o espaco vazio.

Exemplo:
    (1, 2, 3, 4, 5, 6, 7, 8, 0)
"""

class EstadoPuzzle:
    """
    Representa uma configuracao do tabuleiro do 8-Puzzle dentro da árvore de busca.
    Encapsula o estado atual, histórico de movimentos e custos para os algoritmos.
    """

    def __init__(self, valores, anterior=None, movimento=None, custo_g=0, custo_h=0):
        # Transforma em tupla para garantir a imutabilidade exigida pela propriedade __hash__
        self.valores = tuple(valores) 
        self.anterior = anterior
        self.movimento = movimento
        
        # custo_g: Profundidade do nó (quantos passos desde o início)
        self.custo_g = custo_g 
        
        # custo_h: Valor da heurística (palpite até o final). Algoritmos cegos deixam como 0
        self.custo_h = custo_h 

    @property
    def custo_f(self):
        """O custo total f(n) = g(n) + h(n), usado apenas pelo A* e Busca Gulosa."""
        return self.custo_g + self.custo_h

    def __eq__(self, outro):
        """Permite comparar se dois nós têm o mesmo estado (tabuleiro)."""
        return isinstance(outro, EstadoPuzzle) and self.valores == outro.valores

    def __hash__(self):
        """Permite usar o objeto em conjuntos (sets) para a lista de Explorados."""
        return hash(self.valores)

    def __lt__(self, outro):
        """Ensina a fila de prioridade do A* a desempatar nós pelo menor custo F."""
        return self.custo_f < outro.custo_f

    def __repr__(self):
        """Representação limpa para logs e debug."""
        return f"EstadoPuzzle(valores={self.valores}, f={self.custo_f})"

    def formatar(self):
        """
        Retorna uma representacao textual do tabuleiro em formato 3x3.
        O espaco vazio (0) e substituido por '_' para melhor visualizacao.
        """
        linhas = []
        for indice in range(0, 9, 3):
            linha = self.valores[indice:indice + 3]
            linha_formatada = " ".join(str(valor) if valor != 0 else "_" for valor in linha)
            linhas.append(linha_formatada)
        return "\n".join(linhas)