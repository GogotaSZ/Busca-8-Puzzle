"""Testes unitarios das heuristicas do 8-Puzzle."""

import unittest

from estado_puzzle import EstadoPuzzle
from heuristicas.conflito_linear import calcular_conflito_linear
from heuristicas.distancia_manhattan import calcular_manhattan
from heuristicas.pecas_fora_lugar import calcular_pecas_fora_lugar


ESTADO_OBJETIVO = EstadoPuzzle((1, 2, 3, 4, 5, 6, 7, 8, 0))


class TestHeuristicas(unittest.TestCase):
    """Verifica valores conhecidos para cada heuristica implementada."""

    def test_pecas_fora_lugar(self):
        estado = EstadoPuzzle((1, 2, 3, 4, 5, 6, 7, 0, 8))

        self.assertEqual(calcular_pecas_fora_lugar(ESTADO_OBJETIVO, ESTADO_OBJETIVO), 0)
        self.assertEqual(calcular_pecas_fora_lugar(estado, ESTADO_OBJETIVO), 1)

    def test_distancia_manhattan(self):
        estado = EstadoPuzzle((1, 2, 3, 4, 5, 6, 0, 7, 8))

        self.assertEqual(calcular_manhattan(ESTADO_OBJETIVO, ESTADO_OBJETIVO), 0)
        self.assertEqual(calcular_manhattan(estado, ESTADO_OBJETIVO), 2)

    def test_conflito_linear(self):
        estado = EstadoPuzzle((2, 1, 3, 4, 5, 6, 7, 8, 0))

        self.assertEqual(calcular_conflito_linear(ESTADO_OBJETIVO, ESTADO_OBJETIVO), 0)
        self.assertEqual(calcular_conflito_linear(estado, ESTADO_OBJETIVO), 4)


if __name__ == "__main__":
    unittest.main()
