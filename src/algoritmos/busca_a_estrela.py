"""
Implementação do algoritmo de busca A* (A-Estrela).
"""

import heapq
from interface.sucessores import gerar_sucessores
from interface.estado_puzzle import EstadoPuzzle
from heuristicas.pecas_fora_lugar import calcular_pecas_fora_lugar
from heuristicas.distancia_manhattan import calcular_manhattan
from heuristicas.conflito_linear import calcular_conflito_linear

def busca_a_estrela(estado_inicial_valores, opcao_heuristica):
    """
    Executa o algoritmo A* para encontrar o caminho mais curto até o objetivo.
    
    Retorna:
        - no_final: O objeto EstadoPuzzle que atingiu o objetivo (ou None se falhar)
        - nos_visitados: Inteiro com a quantidade de nós tirados da fronteira
    """
    # 1. Definir o estado objetivo oficial do PDF
    OBJETIVO_VALORES = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    no_objetivo = EstadoPuzzle(valores=OBJETIVO_VALORES)
    
    # 2. Mapeamento das heurísticas escolhidas no menu
    funcoes_heuristica = {
        '1': calcular_pecas_fora_lugar,
        '2': calcular_manhattan,
        '3': calcular_conflito_linear
    }
    
    heuristica_escolhida = funcoes_heuristica.get(opcao_heuristica)
    if not heuristica_escolhida:
        raise ValueError("Opção de heurística inválida.")

    # 3. Configurar o nó inicial
    no_inicial = EstadoPuzzle(valores=estado_inicial_valores)
    no_inicial.custo_h = heuristica_escolhida(no_inicial, no_objetivo)
    
    # 4. Estruturas de controle do algoritmo
    fronteira = []
    heapq.heappush(fronteira, no_inicial)
    
    # Usamos um 'set' (conjunto) para o conjunto de explorados. 
    # É O(1) para buscar, absurdamente mais rápido que uma lista.
    explorados = set()
    nos_visitados = 0
    
    # 5. O Laço Principal de Busca
    while fronteira:
        # Remove sempre o nó com o menor f(n)
        no_atual = heapq.heappop(fronteira)
        nos_visitados += 1
        
        # Teste de Objetivo: Achamos a solução?
        if no_atual.valores == OBJETIVO_VALORES:
            return no_atual, nos_visitados
            
        # Para evitar processar o mesmo estado duas vezes e entrar em loop
        if no_atual.valores in explorados:
            continue
            
        # Adiciona a tupla de valores na lista de explorados
        explorados.add(no_atual.valores)
        
        # Pede ao motor do jogo as próximas jogadas válidas
        filhos = gerar_sucessores(no_atual)
        
        for filho in filhos:
            # Se ainda não visitamos esse estado, ele entra na fila
            if filho.valores not in explorados:
                # Calcula o h(n) do filho
                filho.custo_h = heuristica_escolhida(filho, no_objetivo)
                
                # Joga na fila de prioridade
                heapq.heappush(fronteira, filho)
                
    # Se a fronteira esvaziar e não acharmos o objetivo (o que nossa trava matemática evita)
    return None, nos_visitados