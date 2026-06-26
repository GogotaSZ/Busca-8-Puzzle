import os, time
from utilitarios import verificar_solubilidade, ler_estado_de_texto, reconstruir_caminho
from algoritmos.busca_custo_uniforme import buscar as busca_custo_uniforme
from algoritmos.busca_gulosa import buscar as busca_gulosa
from estado_puzzle import EstadoPuzzle
from algoritmos.busca_a_estrela import busca_a_estrela

def imprimir_matriz(estado):
    """Formata e imprime a lista de 9 posições como uma matriz 3x3."""
    for i in range(0, 9, 3):
        # Pega a linha atual (fatiando a lista a cada 3 posições)
        linha = estado[i:i+3]
        # Substitui o 0 por '_' para destacar o espaço vazio
        linha_formatada = [str(x) if x != 0 else "_" for x in linha]
        print("  " + "  ".join(linha_formatada))
    print() # Linha em branco para separar



def exibir_resultados(no_final, nos_visitados, tempo_execucao, nos_gerados=None):
    """
    Formata e exibe os resultados da execução do algoritmo, 
    cumprindo todos os requisitos de saída do PDF.
    """
    print("\n" + "="*40)
    print("🏆 RESULTADOS DA BUSCA")
    print("="*40)
    
    if no_final is None:
        print("Nenhuma solução foi encontrada para este estado.")
    else:
        caminho = reconstruir_caminho(no_final)
        
        print("Passo a passo da solução:\n")
        
        for i, passo in enumerate(caminho):
            if passo['acao']:
                print(f"Passo {i}: Mover espaço vazio para {passo['acao']}")
            else:
                print("Estado Inicial:")
            
            # Aqui chamamos aquele método formatar() lindão da classe EstadoPuzzle
            print(passo['estado'].formatar())
            print("-" * 20)
            
        print("\n📊 MÉTRICAS DA EXECUÇÃO:")
        # A profundidade é exatamente o custo_g do último nó!
        print(f"- Profundidade da solução: {no_final.custo_g} movimentos")
        print(f"- Número de nós visitados: {nos_visitados}")
        if nos_gerados is not None:
            print(f"- Número de nós gerados: {nos_gerados}")
        print(f"- Tempo de execução: {tempo_execucao:.5f} segundos")
    print("="*40 + "\n")

def carregar_casos_teste(nivel_dificuldade):
    """Lê os arquivos txt da pasta exemplos baseado na dificuldade escolhida."""
    arquivos = {
        '1': 'casos_faceis.txt',
        '2': 'casos_medios.txt',
        '3': 'casos_dificeis.txt'
    }

    nome_arquivo = arquivos.get(nivel_dificuldade)
    if not nome_arquivo:
        return None

    # Resolve o caminho absoluto subindo 3 níveis (src/interface/ -> src/ -> raiz -> exemplos/)
    caminho_base = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    caminho_arquivo = os.path.join(caminho_base, 'exemplos', nome_arquivo)

    casos = []
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                # Ignora linhas vazias e comentários
                if linha and not linha.startswith('#'):
                    # Converte a string '1 2 3 5 0 6 4 7 8' em uma lista de inteiros
                    estado = [int(x) for x in linha.split()]
                    casos.append(estado)
        return casos
    except FileNotFoundError:
        print(f"\n[Erro] O arquivo {nome_arquivo} não foi encontrado na pasta 'exemplos'.")
        return None

def menu_algoritmos(estado_inicial):
    """Menu para seleção do algoritmo de busca."""
    while True:
        print("\n" + "-"*40)
        print("Estado Selecionado:\n")
        imprimir_matriz(estado_inicial)
        print("-" * 40)
        print("1. A* (A-Estrela)")
        print("2. Busca em Largura (BFS)")
        print("3. Busca em Profundidade (DFS)")
        print("4. Busca de Custo Uniforme")
        print("5. Busca Gulosa")
        print("0. Voltar")
        
        opcao = input("Selecione o algoritmo: ")
        
        if opcao == '1':
            menu_heuristicas(estado_inicial)
        elif opcao == '4':
            print("\n[Sistema] Iniciando Busca de Custo Uniforme...")
            no_final, nos_visitados, nos_gerados, tempo_execucao = busca_custo_uniforme(
                EstadoPuzzle(estado_inicial),
                EstadoPuzzle((1, 2, 3, 4, 5, 6, 7, 8, 0)),
            )
            exibir_resultados(no_final, nos_visitados, tempo_execucao, nos_gerados)
        elif opcao == '5':
            print("\n[Sistema] Iniciando Busca Gulosa com Distancia de Manhattan...")
            no_final, nos_visitados, nos_gerados, tempo_execucao = busca_gulosa(
                EstadoPuzzle(estado_inicial),
                EstadoPuzzle((1, 2, 3, 4, 5, 6, 7, 8, 0)),
            )
            exibir_resultados(no_final, nos_visitados, tempo_execucao, nos_gerados)
        elif opcao in ['2', '3']:
            print(f"\n[Sistema] O algoritmo {opcao} ainda não foi implementado.")
        elif opcao == '0':
            break
        else:
            print("\nOpção inválida.")

def menu_heuristicas(estado_inicial):
    """Submenu exclusivo para o algoritmo A*."""
    while True:
        print("\n" + "-"*40)
        print("Heurísticas disponíveis para o A*:")
        print("1. Peças fora do lugar")
        print("2. Distância de Manhattan")
        print("3. Conflito Linear")
        print("0. Voltar")
        
        opcao = input("Selecione a heurística: ")
        
        if opcao in ['1', '2', '3']:
            print(f"\n[Sistema] Iniciando A* com heurística {opcao}...")
            
            # Marca o tempo inicial
            inicio = time.time()
            
            # Chama a nossa IA
            no_final, nos_visitados = busca_a_estrela(estado_inicial, opcao)
            
            # Marca o tempo final
            fim = time.time()
            tempo_execucao = fim - inicio
            
            # Exibe o relatório na tela!
            exibir_resultados(no_final, nos_visitados, tempo_execucao)
            break
        elif opcao == '0':
            break
        else:
            print("\nOpção inválida.")

def menu_principal():
    """Ponto de entrada do programa."""
    while True:
        print("\n" + "="*40)
        print("🧩 SOLUCIONADOR 8-PUZZLE")
        print("="*40)
        print("1. Carregar caso de teste")
        print("2. Inserir estado manualmente")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '0':
            print("\nEncerrando o sistema...")
            break
            
        estado_inicial = None
        
        if opcao == '1':
            print("\nNíveis de dificuldade:")
            print("1. Fácil")
            print("2. Médio")
            print("3. Difícil")
            nivel = input("Escolha o nível: ")
            
            casos = carregar_casos_teste(nivel)
            if casos:
                print(f"\nForam carregados {len(casos)} casos:\n")
                for i, caso in enumerate(casos):
                    print(f"[{i+1}]")
                    imprimir_matriz(caso)
                
                try:
                    escolha = int(input("Qual caso deseja executar? ")) - 1
                    if 0 <= escolha < len(casos):
                        estado_inicial = casos[escolha]
                    else:
                        print("\nÍndice fora do limite.")
                except ValueError:
                    print("\nPor favor, digite um número válido.")
                    
        elif opcao == '2':
            entrada = input("\nDigite os 9 números separados por espaço (Use 0 para vazio): ")
            try:
                # Usa a nossa função utilitária que já valida tudo!
                # Se der erro, ela "grita" e o 'except' abaixo captura.
                estado_inicial = ler_estado_de_texto(entrada)
                # Converte a tupla de volta para lista, pois alguns algoritmos podem preferir
                estado_inicial = list(estado_inicial) 
            except ValueError as erro:
                # Aqui o terminal imprime exatamente a mensagem que configuramos no utilitarios.py
                print(f"\n{erro}") 
                estado_inicial = None
                
        # --- BLOCO DE VALIDAÇÃO DE SOLUBILIDADE ---
        if estado_inicial:
            # Verifica se matematicamente tem solução antes de chamar o menu de algoritmos
            if verificar_solubilidade(estado_inicial):
                menu_algoritmos(estado_inicial)
            else:
                print("\n" + "!"*50)
                print("[AVISO] CONFIGURAÇÃO SEM SOLUÇÃO!")
                print("!"*50)
                print("O programa detectou que este estado inicial não possui")
                print("solução matemática (número ímpar de inversões).")
                print("Por favor, tente outra configuração.")
                
if __name__ == "__main__":
    menu_principal()
