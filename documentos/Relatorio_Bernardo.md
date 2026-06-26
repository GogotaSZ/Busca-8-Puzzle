# Material do relatório — Bernardo Ladeira

## Modelagem do 8-Puzzle

O 8-Puzzle é modelado como um problema de busca em espaço de estados. Um estado é uma tupla imutável de nove inteiros, em ordem de leitura do tabuleiro 3×3; os valores de 1 a 8 identificam as peças e `0` representa o espaço vazio. O estado inicial é qualquer configuração válida informada pelo usuário ou selecionada nos casos de teste. O estado objetivo adotado é `(1, 2, 3, 4, 5, 6, 7, 8, 0)`.

As ações possíveis deslocam o espaço vazio para cima, baixo, esquerda ou direita, desde que a posição permaneça dentro do tabuleiro. A função de transição troca o `0` com a peça adjacente na direção escolhida, criando um novo estado e registrando o estado anterior e o movimento realizado. O teste de objetivo compara a tupla do estado atual com a tupla objetivo. Cada movimento possui custo unitário; portanto, o custo acumulado de um nó corresponde à profundidade do caminho até ele. Antes da busca, o programa verifica a paridade de inversões: em um tabuleiro 3×3, somente configurações com número par de inversões alcançam o objetivo adotado.

## Busca em Profundidade (DFS)

A Busca em Profundidade explora primeiro o sucessor mais profundo disponível. A implementação usa uma pilha LIFO: remove o topo, verifica se é objetivo e, caso não seja, insere seus sucessores. O conjunto de estados explorados e o conjunto de estados já presentes na fronteira evitam ciclos e gerações duplicadas. Embora os sucessores sejam obtidos na ordem Cima, Baixo, Esquerda e Direita, eles são empilhados na ordem inversa para que a próxima expansão preserve essa prioridade. Cada nó guarda o ponteiro para seu pai, permitindo reconstruir o caminho ao encontrar o objetivo.

No espaço finito do 8-Puzzle, com controle de estados explorados, a DFS é completa: se houver solução alcançável, a busca termina encontrando uma delas. Caso seja fornecido um limite de profundidade, essa garantia deixa de valer para soluções além do limite. A DFS não é ótima, pois o primeiro caminho encontrado não é necessariamente o de menor número de movimentos. Na formulação em árvore, suas complexidades de pior caso são `O(b^m)` em tempo e espaço, em que `b` é o fator de ramificação e `m` é a profundidade máxima explorada. Nesta implementação em grafo, o limite prático é o número de estados e transições alcançáveis, pois cada estado é expandido no máximo uma vez.

## Busca Gulosa

A Busca Gulosa é uma busca informada que ordena a fronteira apenas pelo valor heurístico `h(n)`. A cada passo, seleciona o estado que aparenta estar mais próximo do objetivo segundo a heurística escolhida; o custo já percorrido `g(n)` não participa da prioridade. Para o 8-Puzzle, uma implementação típica usa uma fila de prioridade e calcula `h(n)` para cada sucessor antes de inseri-lo na fronteira.

Uma heurística mais informativa tende a reduzir o número de estados explorados, mas a Busca Gulosa não garante uma solução ótima porque pode preferir um estado aparentemente promissor que exige um caminho longo. Em espaços infinitos, ela não é completa em geral; no 8-Puzzle finito, o controle de estados repetidos permite que termine se houver solução alcançável. O pior caso continua exponencial em tempo e espaço, `O(b^m)`, embora seu desempenho prático dependa diretamente da qualidade da heurística. A implementação desse algoritmo é responsabilidade de outro membro; esta seção descreve apenas seu funcionamento para o relatório.

## Resultados experimentais da DFS

Medições feitas com Python 3.13 no Windows, sem impressão do caminho durante a busca. Para cada instância, o tempo apresentado é a mediana de três execuções; os demais valores são determinísticos para a ordem de sucessores adotada.

| Caso | Estado inicial | Tempo mediano (s) | Nós expandidos/visitados | Nós gerados | Profundidade da solução |
| --- | --- | ---: | ---: | ---: | ---: |
| Fácil 1 | `(1, 2, 3, 4, 5, 6, 7, 0, 8)` | 0,501919 | 181440 | 181440 | 1 |
| Fácil 2 | `(1, 2, 3, 4, 5, 6, 0, 7, 8)` | 0,260598 | 84897 | 127093 | 64328 |
| Fácil 3 | `(1, 2, 3, 4, 5, 0, 7, 8, 6)` | 0,649250 | 181439 | 181440 | 1 |
| Médio 1 | `(1, 2, 3, 5, 0, 6, 4, 7, 8)` | 0,413622 | 127975 | 165588 | 54710 |
| Médio 2 | `(1, 3, 6, 5, 2, 0, 4, 7, 8)` | 0,254954 | 58705 | 94625 | 51551 |
| Médio 3 | `(1, 3, 6, 5, 0, 2, 4, 7, 8)` | 0,533658 | 131502 | 167832 | 52270 |
| Difícil 1 | `(7, 2, 4, 5, 0, 6, 8, 3, 1)` | 0,552409 | 146987 | 175856 | 39478 |
| Difícil 2 | `(8, 6, 7, 2, 5, 4, 3, 0, 1)` | 0,138172 | 44186 | 73832 | 40757 |
| Difícil 3 | `(6, 4, 7, 8, 5, 0, 3, 2, 1)` | 0,571640 | 166721 | 180799 | 18055 |

Os resultados evidenciam que a DFS não produz, necessariamente, o caminho mais curto. Mesmo configurações a uma jogada do objetivo podem fazer a busca visitar grande parte do espaço de estados quando a solução direta aparece por último na ordem de expansão.
