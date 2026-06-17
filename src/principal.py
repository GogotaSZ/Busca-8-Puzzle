"""
Ponto de entrada da aplicacao do projeto 8-Puzzle.

Este arquivo deve concentrar apenas a inicializacao do programa e delegar
a interacao com o usuario para o modulo de interface.
"""

from interface.linha_comando import executar_linha_comando


def principal():
    """
    Inicia a aplicacao pela interface de linha de comando.

    TODO:
    - Ler argumentos informados pelo usuario.
    - Permitir escolha do algoritmo de busca.
    - Permitir escolha da heuristica quando o algoritmo exigir.
    - Exibir o caminho da solucao e as metricas da execucao.
    """
    executar_linha_comando()


if __name__ == "__main__":
    principal()
