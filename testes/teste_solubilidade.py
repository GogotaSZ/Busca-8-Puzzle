"""Testes unitarios da verificacao de solubilidade do 8-Puzzle."""

import unittest

from utilitarios import verificar_solubilidade


class TestSolubilidade(unittest.TestCase):
    """Cobre configuracoes com paridade par e impar de inversoes."""

    def test_estados_soluveis(self):
        casos = [
            (1, 2, 3, 4, 5, 6, 7, 8, 0),
            (1, 2, 3, 4, 5, 6, 7, 0, 8),
            (1, 2, 3, 4, 5, 6, 0, 7, 8),
        ]

        for estado in casos:
            with self.subTest(estado=estado):
                self.assertTrue(verificar_solubilidade(estado))

    def test_estado_insoluvel(self):
        estado = (1, 2, 3, 4, 5, 6, 8, 7, 0)

        self.assertFalse(verificar_solubilidade(estado))


if __name__ == "__main__":
    unittest.main()
