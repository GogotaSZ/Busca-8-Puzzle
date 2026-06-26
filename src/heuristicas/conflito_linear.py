"""
Heurística: Conflito Linear (Linear Conflict)
Complementa a Distância de Manhattan adicionando o custo das peças que 
estão na linha/coluna correta, mas na ordem invertida.
"""

from heuristicas.distancia_manhattan import calcular_manhattan

def calcular_conflito_linear(estado_atual, estado_objetivo):
    """
    Calcula o Conflito Linear somado à Distância de Manhattan.
    Cada conflito direto entre duas peças na mesma linha ou coluna 
    adiciona um custo de 2 movimentos.
    """
    # Inicia com o valor base da Manhattan
    custo_h = calcular_manhattan(estado_atual, estado_objetivo)
    
    conflitos = 0
    valores = estado_atual.valores
    objetivos = estado_objetivo.valores

    # Verifica conflitos nas LINHAS
    for linha in range(3):
        pecas_linha = []
        for coluna in range(3):
            indice = linha * 3 + coluna
            peca = valores[indice]
            
            # Se a peça não é o zero e o objetivo dela também é nesta mesma linha
            if peca != 0:
                indice_obj = objetivos.index(peca)
                linha_obj = indice_obj // 3
                if linha == linha_obj:
                    pecas_linha.append(peca)
                    
        # Compara os pares na linha para ver se estão invertidos
        for i in range(len(pecas_linha)):
            for j in range(i + 1, len(pecas_linha)):
                peca_esq = pecas_linha[i]
                peca_dir = pecas_linha[j]
                
                coluna_obj_esq = objetivos.index(peca_esq) % 3
                coluna_obj_dir = objetivos.index(peca_dir) % 3
                
                # Se a peça da esquerda deveria estar à direita da outra, é um conflito!
                if coluna_obj_esq > coluna_obj_dir:
                    conflitos += 1

    # Verifica conflitos nas COLUNAS
    for coluna in range(3):
        pecas_coluna = []
        for linha in range(3):
            indice = linha * 3 + coluna
            peca = valores[indice]
            
            # Se a peça não é o zero e o objetivo dela também é nesta mesma coluna
            if peca != 0:
                indice_obj = objetivos.index(peca)
                coluna_obj = indice_obj % 3
                if coluna == coluna_obj:
                    pecas_coluna.append(peca)
                    
        # Compara os pares na coluna para ver se estão invertidos
        for i in range(len(pecas_coluna)):
            for j in range(i + 1, len(pecas_coluna)):
                peca_cima = pecas_coluna[i]
                peca_baixo = pecas_coluna[j]
                
                linha_obj_cima = objetivos.index(peca_cima) // 3
                linha_obj_baixo = objetivos.index(peca_baixo) // 3
                
                # Se a peça de cima deveria estar abaixo da outra, é um conflito!
                if linha_obj_cima > linha_obj_baixo:
                    conflitos += 1

    # Cada conflito exige 1 passo para sair do caminho e 1 para voltar (+2)
    return custo_h + (2 * conflitos)