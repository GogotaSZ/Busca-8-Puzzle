"""Testes unitarios da Busca A* para o 8-Puzzle."""

import unittest

from algoritmos.busca_a_estrela import busca_a_estrela
from utilitarios import reconstruir_caminho


ESTADO_OBJETIVO = (1, 2, 3, 4, 5, 6, 7, 8, 0)
ESTADO_A_UMA_JOGADA = (1, 2, 3, 4, 5, 6, 7, 0, 8)


class TestBuscaAEstrela(unittest.TestCase):
    """Cobre o retorno com metricas completas do A*."""

    def test_estado_inicial_ja_e_objetivo(self):
        no_final, nos_visitados, nos_gerados, tempo_execucao = busca_a_estrela(
            ESTADO_OBJETIVO,
            "2",
        )

        self.assertEqual(no_final.valores, ESTADO_OBJETIVO)
        self.assertEqual(no_final.custo_g, 0)
        self.assertEqual(nos_visitados, 1)
        self.assertEqual(nos_gerados, 1)
        self.assertGreaterEqual(tempo_execucao, 0)

    def test_solucao_de_uma_jogada_retorna_metricas_completas(self):
        no_final, nos_visitados, nos_gerados, tempo_execucao = busca_a_estrela(
            ESTADO_A_UMA_JOGADA,
            "2",
        )
        caminho = reconstruir_caminho(no_final)

        self.assertEqual(no_final.valores, ESTADO_OBJETIVO)
        self.assertEqual([passo["acao"] for passo in caminho], [None, "Direita"])
        self.assertEqual(no_final.custo_g, 1)
        self.assertGreaterEqual(nos_visitados, 1)
        self.assertGreaterEqual(nos_gerados, nos_visitados)
        self.assertGreaterEqual(tempo_execucao, 0)

    def test_heuristica_invalida_lanca_erro(self):
        with self.assertRaises(ValueError):
            busca_a_estrela(ESTADO_OBJETIVO, "9")


if __name__ == "__main__":
    unittest.main()
