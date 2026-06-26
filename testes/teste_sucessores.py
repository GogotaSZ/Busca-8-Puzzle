"""Testes unitarios da geracao de sucessores do 8-Puzzle."""

import unittest

from estado_puzzle import EstadoPuzzle
from sucessores import gerar_sucessores


class TestSucessores(unittest.TestCase):
    """Cobre movimentos validos em posicoes representativas do tabuleiro."""

    def test_sucessores_com_vazio_no_centro(self):
        estado = EstadoPuzzle((1, 2, 3, 4, 0, 5, 6, 7, 8))

        sucessores = gerar_sucessores(estado)

        self.assertEqual(len(sucessores), 4)
        self.assertEqual(
            [sucessor.movimento for sucessor in sucessores],
            ["Cima", "Baixo", "Esquerda", "Direita"],
        )
        self.assertEqual(
            [sucessor.valores for sucessor in sucessores],
            [
                (1, 0, 3, 4, 2, 5, 6, 7, 8),
                (1, 2, 3, 4, 7, 5, 6, 0, 8),
                (1, 2, 3, 0, 4, 5, 6, 7, 8),
                (1, 2, 3, 4, 5, 0, 6, 7, 8),
            ],
        )
        self.assertTrue(all(sucessor.anterior is estado for sucessor in sucessores))
        self.assertTrue(all(sucessor.custo_g == 1 for sucessor in sucessores))

    def test_sucessores_com_vazio_no_canto(self):
        estado = EstadoPuzzle((1, 2, 3, 4, 5, 6, 7, 8, 0))

        sucessores = gerar_sucessores(estado)

        self.assertEqual(len(sucessores), 2)
        self.assertEqual(
            [sucessor.movimento for sucessor in sucessores],
            ["Cima", "Esquerda"],
        )
        self.assertEqual(
            [sucessor.valores for sucessor in sucessores],
            [
                (1, 2, 3, 4, 5, 0, 7, 8, 6),
                (1, 2, 3, 4, 5, 6, 7, 0, 8),
            ],
        )


if __name__ == "__main__":
    unittest.main()
