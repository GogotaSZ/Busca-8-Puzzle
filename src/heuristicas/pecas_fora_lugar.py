"""
Heurística: Peças Fora do Lugar (Hamming Distance)
"""

def calcular_pecas_fora_lugar(estado_atual, estado_objetivo):
    """
    Conta o número de peças que estão em posições diferentes do estado objetivo.
    O espaço vazio (0) é ignorado na contagem.
    """
    custo_h = 0
    valores_atuais = estado_atual.valores
    valores_objetivo = estado_objetivo.valores

    for i in range(9):
        peca = valores_atuais[i]
        # Ignora o 0 e verifica se a peça está no lugar errado
        if peca != 0 and peca != valores_objetivo[i]:
            custo_h += 1
            
    return custo_h