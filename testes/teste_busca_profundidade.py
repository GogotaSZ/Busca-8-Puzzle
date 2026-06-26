"""Testes unitários da Busca em Profundidade para o 8-Puzzle."""

import unittest

from algoritmos.busca_profundidade import buscar
from utilitarios import reconstruir_caminho


ESTADO_OBJETIVO = (1, 2, 3, 4, 5, 6, 7, 8, 0)
ESTADO_A_UMA_JOGADA = (1, 2, 3, 4, 5, 6, 7, 0, 8)


class TestBuscaProfundidade(unittest.TestCase):
    """Cobre o contrato público e as métricas da DFS."""

    def test_estado_inicial_ja_e_objetivo(self):
        no_final, metricas = buscar(ESTADO_OBJETIVO, ESTADO_OBJETIVO)

        self.assertEqual(no_final.valores, ESTADO_OBJETIVO)
        self.assertEqual(metricas['profundidade'], 0)
        self.assertEqual(metricas['nos_visitados'], 1)
        self.assertEqual(metricas['nos_gerados'], 1)

    def test_solucao_de_uma_jogada_com_caminho_e_metricas(self):
        no_final, metricas = buscar(
            ESTADO_A_UMA_JOGADA,
            ESTADO_OBJETIVO,
            limite_profundidade=1,
        )
        caminho = reconstruir_caminho(no_final)

        self.assertEqual(no_final.valores, ESTADO_OBJETIVO)
        self.assertEqual(no_final.custo_g, 1)
        self.assertEqual([passo['acao'] for passo in caminho], [None, 'Direita'])
        self.assertEqual(metricas['profundidade'], 1)
        self.assertEqual(metricas['nos_visitados'], 4)
        self.assertEqual(metricas['nos_gerados'], 4)
        self.assertGreaterEqual(metricas['tempo_execucao'], 0)

    def test_limite_de_profundidade_impede_solucao_mais_profunda(self):
        no_final, metricas = buscar(
            ESTADO_A_UMA_JOGADA,
            ESTADO_OBJETIVO,
            limite_profundidade=0,
        )

        self.assertIsNone(no_final)
        self.assertIsNone(metricas['profundidade'])
        self.assertEqual(metricas['nos_visitados'], 1)
        self.assertEqual(metricas['nos_gerados'], 1)

    def test_limite_invalido_lanca_erro(self):
        for limite in (-1, True, '1'):
            with self.subTest(limite=limite):
                with self.assertRaises(ValueError):
                    buscar(ESTADO_OBJETIVO, ESTADO_OBJETIVO, limite)


if __name__ == '__main__':
    unittest.main()
