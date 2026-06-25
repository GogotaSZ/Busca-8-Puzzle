"""
Funcoes utilitarias compartilhadas pelo projeto.
"""

def reconstruir_caminho(estado_final):
    """
    Reconstrui o caminho da solucao a partir do estado final.

    Considera que 'estado_final' e um objeto da classe No (Node),
    que contem referencias para o 'pai', 'acao' e 'estado'.
    """
    caminho = []
    no_atual = estado_final
    
    # Percorre os ponteiros de pai ate chegar ao no raiz (onde pai e None)
    while no_atual is not None:
        # Extraimos os atributos com getattr para evitar erros caso os nomes mudem,
        # mas idealmente seu objeto 'No' tera atributos diretos como no.acao e no.estado
        acao = getattr(no_atual, 'acao', None)
        estado = getattr(no_atual, 'estado', None)
        
        caminho.append({
            'acao': acao,
            'estado': estado
        })
        
        no_atual = getattr(no_atual, 'pai', None)
        
    # Inverte a lista para que a ordem seja do Inicio -> Objetivo
    caminho.reverse()
    
    return caminho


def verificar_solubilidade(valores):
    """
    Verifica se uma configuracao do 8-Puzzle pode chegar ao estado objetivo.
    
    Retorna True se for soluvel (inversoes pares), False caso contrario.
    """
    inversoes = 0
    # Extrai apenas as pecas, ignorando o espaco vazio (0)
    valores_sem_zero = [v for v in valores if v != 0]
    tamanho = len(valores_sem_zero)
    
    # Compara cada numero com todos os numeros a sua direita
    for i in range(tamanho):
        for j in range(i + 1, tamanho):
            if valores_sem_zero[i] > valores_sem_zero[j]:
                inversoes += 1
                
    # No tabuleiro 3x3, estados soluveis possuem numero par de inversoes
    return inversoes % 2 == 0


def ler_estado_de_texto(texto):
    """
    Converte uma linha de texto em uma tupla de inteiros.

    Exemplo esperado:
        "1 2 3 4 5 6 7 8 0"
    """
    try:
        # Tenta separar a string por espacos e converter para inteiros
        valores = [int(x) for x in texto.split()]
    except ValueError:
        raise ValueError("Erro: O texto deve conter apenas numeros inteiros.")
        
    # Valida quantidade de valores
    if len(valores) != 9:
        raise ValueError(f"Erro: Quantidade invalida. Esperado 9 valores, recebido {len(valores)}.")
        
    # Valida repeticoes verificando se todos os numeros de 0 a 8 estao presentes
    # Convertendo para set (conjunto), eliminamos duplicatas automaticamente
    if set(valores) != set(range(9)):
        raise ValueError("Erro: Valores invalidos ou repetidos. O estado deve conter os numeros de 0 a 8 exatamente uma vez.")
        
    # Retorna como tupla para garantir a imutabilidade na passagem de parametros
    return tuple(valores)