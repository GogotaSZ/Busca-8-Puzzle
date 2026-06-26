# 🧩 Solucionador 8-Puzzle

Este projeto é uma implementação em Python voltada ao estudo de algoritmos de busca em Inteligência Artificial, aplicado ao problema clássico do 8-Puzzle. O sistema permite a resolução de tabuleiros através de busca cega e busca informada, coletando métricas de desempenho para análise acadêmica.

## 👥 Equipe
* Bernardo Ladeira Kartabil
* Guilherme Henrique da Silva Teodoro
* Marcella Santos Belchior
* Yasmin Torres Moreira dos Santos

## 👨‍🏫 Professor Responsável
* Gabriel P. D. Oliveira

---

## 📋 Pré-requisitos
* **Python:** 3.8 ou superior
* **Git:** Opcional (para clonar o repositório)

## 🚀 Como Executar

1. **Clone o repositório ou baixe os arquivos.**
2. **Navegue até a pasta `src`:**
   ```bash
   cd src
   ```
3. **Inicie o sistema:**
   ```bash
   python principal.py
   ```

## 🎮 Funcionalidades

* **Seleção de Dificuldade:** Carregue casos de teste (Fácil, Médio, Difícil).
* **Entrada Manual:** Insira sua própria configuração (ex: `1 2 3 4 5 6 7 8 0`).

### Algoritmos Implementados:
* **A-Estrela:** Utilizando heurísticas de *Peças fora do lugar*, *Distância de Manhattan* e *Conflito Linear*.
* **Busca em Largura (BFS):** Exploração exaustiva por níveis.
* **Busca em Profundidade (DFS):** Exploração profunda com controle de estados visitados.
* **Busca de Custo Uniforme (UCS):** Expansão baseada no menor custo de caminho $g(n)$.
* **Busca Gulosa:** Expansão baseada estritamente no valor heurístico $h(n)$.

### Métricas Geradas:
O sistema calcula automaticamente e exibe ao final da execução:
* Profundidade da solução
* Número de nós expandidos (visitados)
* Número de nós gerados
* Tempo de execução (segundos)

## 📂 Estrutura do Projeto

```text
src/
├── algoritmos/        # Lógica dos algoritmos de busca e heurísticas
├── interface/         # Menus de linha de comando e exibição
├── utilitarios.py     # Funções de validação e reconstrução de caminho
└── principal.py       # Ponto de entrada
```

---
*Projeto acadêmico desenvolvido para a disciplina de Inteligência Artificial - PUC Minas.*
