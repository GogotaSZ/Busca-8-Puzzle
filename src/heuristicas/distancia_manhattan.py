"""
Heurística: Distância de Manhattan (City Block Distance)
"""

def calcular_manhattan(estado_atual, estado_objetivo):
    """
    Calcula a soma das distâncias horizontais e verticais de cada peça
    até a sua posição objetivo.
    """
    custo_h = 0
    valores_atuais = estado_atual.valores
    valores_objetivo = estado_objetivo.valores

    for i in range(9):
        peca = valores_atuais[i]
        if peca != 0:
            # Encontra onde a peça deveria estar no objetivo
            indice_objetivo = valores_objetivo.index(peca)
            
            # Calcula a linha e coluna atual (usando divisão inteira e resto)
            linha_atual = i // 3
            coluna_atual = i % 3
            
            # Calcula a linha e coluna objetivo
            linha_objetivo = indice_objetivo // 3
            coluna_objetivo = indice_objetivo % 3
            
            # Soma a diferença absoluta das linhas e colunas
            distancia = abs(linha_atual - linha_objetivo) + abs(coluna_atual - coluna_objetivo)
            custo_h += distancia

    return custo_h