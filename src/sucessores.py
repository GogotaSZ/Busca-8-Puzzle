"""
Geracao de sucessores para o 8-Puzzle.

Este modulo sera responsavel por listar todos os movimentos validos a partir
de um estado atual.
"""

from estado_puzzle import EstadoPuzzle

MOVIMENTOS = {
    "Cima": -3,
    "Baixo": 3,
    "Esquerda": -1,
    "Direita": 1,
}

def movimento_valido(posicao_vazio, movimento):
    """
    Verifica se um movimento pode ser aplicado ao espaco vazio no grid 3x3 (1D).
    """
    if movimento == "Cima" and posicao_vazio < 3:
        return False
    if movimento == "Baixo" and posicao_vazio > 5:
        return False
    if movimento == "Esquerda" and posicao_vazio % 3 == 0:
        return False
    if movimento == "Direita" and posicao_vazio % 3 == 2:
        return False
    
    return True

def gerar_sucessores(estado_atual):
    """
    Gera os estados sucessores validos para o estado atual.
    """
    sucessores = []
    valores = estado_atual.valores
    
    # Localiza a posicao do espaco vazio (o zero)
    posicao_vazio = valores.index(0)

    for nome_movimento, delta in MOVIMENTOS.items():
        if movimento_valido(posicao_vazio, nome_movimento):
            # Calcula o indice de destino da peca que vai ser movida
            nova_posicao = posicao_vazio + delta
            
            # Transforma a tupla em lista temporariamente para fazer a troca (swap)
            novos_valores = list(valores)
            novos_valores[posicao_vazio], novos_valores[nova_posicao] = novos_valores[nova_posicao], novos_valores[posicao_vazio]
            
            # Instancia o novo objeto usando nossa classe padronizada
            novo_estado = EstadoPuzzle(
                valores=novos_valores,
                anterior=estado_atual,
                movimento=nome_movimento,
                custo_g=estado_atual.custo_g + 1
            )
            
            sucessores.append(novo_estado)

    return sucessores

