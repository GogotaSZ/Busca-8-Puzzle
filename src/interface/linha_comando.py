import os

def imprimir_matriz(estado):
    """Formata e imprime a lista de 9 posições como uma matriz 3x3."""
    for i in range(0, 9, 3):
        # Pega a linha atual (fatiando a lista a cada 3 posições)
        linha = estado[i:i+3]
        # Substitui o 0 por '_' para destacar o espaço vazio
        linha_formatada = [str(x) if x != 0 else "_" for x in linha]
        print("  " + "  ".join(linha_formatada))
    print() # Linha em branco para separar

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
        elif opcao in ['2', '3', '4', '5']:
            print(f"\n[Sistema] Iniciando execução do algoritmo {opcao}...")
            # Aqui no futuro vamos chamar a função correspondente da pasta src/algoritmos/
            # Ex: resultados = busca_largura(estado_inicial)
            # exibir_resultados(resultados)
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
            # Chamada futura: resultados = busca_a_estrela(estado_inicial, heuristica=opcao)
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
                estado_inicial = [int(x) for x in entrada.split()]
                if len(estado_inicial) != 9:
                    print("\n[Erro] Você deve inserir exatamente 9 números.")
                    estado_inicial = None
            except ValueError:
                print("\n[Erro] Insira apenas números.")
                
        if estado_inicial:
            menu_algoritmos(estado_inicial)

if __name__ == "__main__":
    menu_principal()