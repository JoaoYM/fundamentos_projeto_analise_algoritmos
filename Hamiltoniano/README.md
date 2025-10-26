# Implementação do Algoritmo de Caminho Hamiltoniano (Backtracking) em Python 🛤️

**Trabalho Individual 3 - Fundamentos de Projeto e Análise de Algoritmos**

Este projeto apresenta uma implementação em Python do algoritmo de **Backtracking** para encontrar um **Caminho Hamiltoniano** em um grafo. Um Caminho Hamiltoniano é um caminho que visita cada vértice do grafo exatamente uma vez.

Encontrar tal caminho é um problema NP-Completo clássico, intimamente relacionado ao Problema do Caixeiro Viajante (TSP). A abordagem de backtracking implementada explora sistematicamente todas as possibilidades de caminhos, "retrocedendo" assim que um caminho se mostra inviável.

O script `main.py` é interativo, solicitando a definição do grafo ao usuário, e inclui a funcionalidade de **visualização opcional (ponto extra)**, que é ativada automaticamente caso as bibliotecas `networkx` e `matplotlib` estejam instaladas.

-----

## 1\. Descrição do Projeto

O algoritmo implementado utiliza uma classe `Grafo` que armazena os vértices e arestas usando uma lista de adjacência. A lógica principal de busca é encapsulada em uma função recursiva de backtracking (`_backtrack_util`) que tenta construir um caminho passo a passo.

### 🧠 Lógica do Algoritmo (main.py)

O script é estruturado da seguinte forma:

1.  **Imports Opcionais**:
    O script primeiro tenta importar `networkx` e `matplotlib`. Se a importação falhar, ele define `VISUALIZACAO_DISPONIVEL = False` e continua a execução normalmente, apenas desativando o recurso de visualização.

    ```python
    try:
        import networkx as nx
        import matplotlib.pyplot as plt
        VISUALIZACAO_DISPONIVEL = True
    except ImportError:
        VISUALIZACAO_DISPONIVEL = False
    ```

2.  **Função Principal (`encontrar_caminho_hamiltoniano`)**:
    Como o caminho pode começar em qualquer vértice, esta função itera por todos os vértices (de `0` a `V-1`), usando cada um como um ponto de partida potencial.

    ```python
    def encontrar_caminho_hamiltoniano(self):
        for inicio in range(self.V):
            # Prepara estruturas para uma nova busca
            self.path = []
            visitado = [False] * self.V
            
            # Chama a função recursiva de backtracking
            if self._backtrack_util(inicio, visitado):
                return self.path # Sucesso
        
        return None # Falha
    ```

3.  **Função Recursiva (`_backtrack_util`) - O Backtracking**:
    Esta é a função central que constrói o caminho:

      * **Escolha**: Adiciona o vértice `v` ao `self.path` e o marca como `visitado`.
      * **Caso Base (Sucesso)**: Se `len(self.path) == self.V`, todos os vértices foram visitados. Retorna `True`.
      * **Exploração**: Itera por todos os `vizinhos` de `v`. Se um vizinho não foi visitado, chama a si mesma recursivamente para esse vizinho.
      * **Backtrack (Falha)**: Se o loop de vizinhos termina sem sucesso, a escolha de `v` foi um beco sem saída. Remove `v` do `self.path`, desmarca `visitado` e retorna `False`.

    <!-- end list -->

    ```python
    def _backtrack_util(self, v, visitado):
        self.path.append(v)
        visitado[v] = True

        if len(self.path) == self.V:
            return True

        for vizinho in self.adj[v]:
            if not visitado[vizinho]:
                if self._backtrack_util(vizinho, visitado):
                    return True
        
        # Backtrack
        self.path.pop()
        visitado[v] = False
        return False
    ```

4.  **Função `main()` - Fluxo Principal**:
    A função `main()` gerencia a interação com o usuário (coleta de vértices e arestas) e, ao final, chama `encontrar_caminho_hamiltoniano()`.

      * Se um caminho for encontrado, ele é impresso.
      * Em seguida, se `VISUALIZACAO_DISPONIVEL` for `True`, a função `visualizar_caminho_encontrado()` é chamada para gerar o gráfico.

-----

## 2\. Como Executar o Projeto

O script `main.py` foi refatorado para aceitar entradas interativas e incluir a visualização opcional.

1.  **Clone o repositório (exemplo):**

    ```bash
    git clone https://github.com/JoaoYM/fundamentos_projeto_analise_algoritmos.git
    cd seu-repositorio
    ```

2.  **(Opcional) Habilitando a Visualização (Ponto Extra):**
    Para que o script possa desenhar o grafo, você deve instalar as bibliotecas `networkx` e `matplotlib`. Se você não as instalar, o script funcionará normalmente, mas pulará a etapa de visualização.

    ```bash
    pip install networkx matplotlib
    ```

    *Nota: Se você estiver no Windows e encontrar erros relacionados ao `pip` ou `tkinter`, consulte os prompts anteriores para obter soluções sobre como usar `py -m pip` ou reparar sua instalação do Python para incluir o Tcl/Tk.*

3.  **Execute o arquivo principal:**

    ```bash
    python main.py
    ```

4.  **Forneça as entradas interativas:**
    O programa solicitará, em ordem:

      * `Digite o número total de vértices:` (ex: `5`)
      * `O grafo é orientado? (s/n):` (ex: `n`)
      * `Digite o número total de arestas:` (ex: `6`)
      * `Digite as 6 arestas (formato: origem destino):`
          * `Aresta 1: 0 1`
          * `Aresta 2: 1 2`
          * ...

    Após a inserção da última aresta, o script executará a busca. Se um caminho for encontrado, ele será impresso e, se as bibliotecas estiverem instaladas, uma janela com o grafo será exibida.

-----

## 3\. Exemplos de Teste e Casos de Uso

Abaixo estão 12 cenários de teste para validar o `main.py` interativo.

**1. Grafo Linha (Não Orientado)**

  * **Input:**
      * Vértices: `4`
      * Orientado: `n`
      * Arestas: `3`
      * `0 1`, `1 2`, `2 3`
  * **Resultado Esperado:** `[0, 1, 2, 3]` (ou `[3, 2, 1, 0]`)

**2. Grafo Linha (Orientado, com caminho)**

  * **Input:**
      * Vértices: `4`
      * Orientado: `s`
      * Arestas: `3`
      * `0 1`, `1 2`, `2 3`
  * **Resultado Esperado:** `[0, 1, 2, 3]`

**3. Grafo Linha (Orientado, sem caminho)**

  * **Input:**
      * Vértices: `4`
      * Orientado: `s`
      * Arestas: `3`
      * `3 2`, `2 1`, `0 1`
  * **Resultado Esperado:** `Nenhum Caminho Hamiltoniano foi encontrado.`

**4. Grafo Desconexo (Não Orientado)**

  * **Input:**
      * Vértices: `5`
      * Orientado: `n`
      * Arestas: `3`
      * `0 1`, `1 2`, `3 4`
  * **Resultado Esperado:** `Nenhum Caminho Hamiltoniano foi encontrado.`

**5. Grafo Completo K4 (Não Orientado)**

  * **Input:**
      * Vértices: `4`
      * Orientado: `n`
      * Arestas: `6`
      * `0 1`, `0 2`, `0 3`, `1 2`, `1 3`, `2 3`
  * **Resultado Esperado:** `[0, 1, 2, 3]` (Qualquer permutação é válida, ex: `[0, 2, 1, 3]`)

**6. Grafo Ciclo C5 (Não Orientado)**

  * **Input:**
      * Vértices: `5`
      * Orientado: `n`
      * Arestas: `5`
      * `0 1`, `1 2`, `2 3`, `3 4`, `4 0`
  * **Resultado Esperado:** `[0, 1, 2, 3, 4]` (ou `[0, 4, 3, 2, 1]`)

**7. Grafo "Casa" (Substituto do "Estrela")**

  * **Input:**
      * Vértices: `5`
      * Orientado: `n`
      * Arestas: `6`
      * `0 1`, `1 2`, `2 3`, `3 0`, `0 4`, `1 4`
  * **Resultado Esperado:** `[2, 1, 4, 0, 3]` (ou `[3, 0, 4, 1, 2]`)

**8. Grafo Estrela (Teste Negativo Válido)**

  * **Input:**
      * Vértices: `5`
      * Orientado: `n`
      * Arestas: `4`
      * `0 1`, `0 2`, `0 3`, `0 4`
  * **Resultado Esperado:** `Nenhum Caminho Hamiltoniano foi encontrado.` (Correto, pois o vértice '0' precisaria ser revisitado).

**9. Grafo "Haltere" (Dois K3 com ponte)**

  * **Input:**
      * Vértices: `6`
      * Orientado: `n`
      * Arestas: `7`
      * `0 1`, `1 2`, `2 0` (K3 esquerdo)
      * `2 3` (Ponte)
      * `3 4`, `4 5`, `5 3` (K3 direito)
  * **Resultado Esperado:** `[0, 1, 2, 3, 4, 5]` (ou `[1, 0, 2, 3, 5, 4]`)

**10. Grafo "Gargalo" (Teste Negativo Válido)**

  * **Input:**
      * Vértices: `5`
      * Orientado: `n`
      * Arestas: `4`
      * `0 1`, `1 2`, `2 3`, `2 4`
  * **Resultado Esperado:** `Nenhum Caminho Hamiltoniano foi encontrado.` (O vértice '2' é um ponto de articulação que precisaria ser revisitado).

**11. Vértice Único**

  * **Input:**
      * Vértices: `1`
      * Orientado: `n`
      * Arestas: `0`
  * **Resultado Esperado:** `[0]`

**12. Dois Vértices, Sem Aresta**

  * **Input:**
      * Vértices: `2`
      * Orientado: `n`
      * Arestas: `0`
  * **Resultado Esperado:** `Nenhum Caminho Hamiltoniano foi encontrado.`

-----

## 4\. Relatório Técnico

### 4.1. Análise da Complexidade Computacional (Classes P, NP, NP-Completo e NP-Difícil)

**Referência:** AULA 02\_Introdução à teoria da complexidade.pdf - Páginas 69-95

O Problema do Caminho Hamiltoniano (HPP) é um problema de decisão fundamental na teoria da computação. Sua classificação é a seguinte:

  * **Classe P (Polinomial)**:

      * [cite\_start]**Definição:** Problemas que podem ser *resolvidos* por um algoritmo determinístico em tempo polinomial ($O(n^k)$) [cite: 843-848].
      * **Classificação HPP:** O HPP **não pertence** à classe P (assumindo a crença geral de que $P \ne NP$). Não existe um algoritmo conhecido que resolva o HPP em tempo polinomial.

  * **Classe NP (Não-Determinístico Polinomial)**:

      * [cite\_start]**Definição:** Problemas cujas soluções ("certificados") podem ser *verificadas* em tempo polinomial por um algoritmo determinístico [cite: 857-861, 873].
      * **Classificação HPP:** O HPP **pertence** à classe NP. [cite\_start]Se recebermos um caminho candidato (uma sequência de $V$ vértices), podemos verificá-lo em tempo polinomial[cite: 1003, 1015]:
        1.  Checar se o caminho contém $V$ vértices únicos ($O(V)$).
        2.  Checar se existe uma aresta entre cada vértice $v_i$ e $v_{i+1}$ no caminho ( $O(V)$ ).
      * Como a verificação é polinomial, o problema está em NP.

  * **Classe NP-Difícil (NP-Hard)**:

      * **Definição:** Problemas que são *pelo menos tão difíceis* quanto qualquer problema em NP. [cite\_start]Todo problema NP pode ser reduzido a um problema NP-Difícil em tempo polinomial [cite: 896-900, 929].
      * **Classificação HPP:** O HPP **é NP-Difícil**.

  * **Classe NP-Completo (NP-Complete)**:

      * [cite\_start]**Definição:** Problemas que atendem a duas condições: 1) Pertencem a NP e 2) São NP-Difíceis [cite: 880-886, 926].
      * [cite\_start]**Classificação HPP:** O HPP **é NP-Completo**[cite: 940, 1015]. Ele está em NP (é verificável) e é NP-Difícil (tão difícil quanto qualquer problema NP).

**Justificativa (Relação com o TSP):**
[cite\_start]O Problema do Caixeiro Viajante (TSP), em sua versão de decisão ("existe um ciclo de custo $\le k$?"), é NP-Completo[cite: 865, 1016]. O Problema do Caminho Hamiltoniano pode ser reduzido ao TSP. Se pudéssemos resolver o HPP em tempo polinomial, poderíamos também resolver o TSP e, por extensão, todos os problemas NP-Completos. Isso solidifica sua classificação como NP-Completo.

### 4.2. Análise da Complexidade Assintótica de Tempo

  * [cite\_start]**Método Utilizado:** A complexidade é determinada pela **análise da árvore de recursão (contagem de operações)**, similar à análise de força bruta do TSP [cite: 1098-1101]. O Teorema Mestre não se aplica, como detalhado abaixo.
  * **Análise:** No pior caso, o algoritmo `_backtrack_util` será chamado para cada caminho possível.
      * O primeiro vértice (escolhido na função principal) tem $V$ opções.
      * O segundo vértice (primeira chamada recursiva) tem até $(V-1)$ vizinhos para explorar.
      * O terceiro vértice tem até $(V-2)$ vizinhos, e assim por diante.
  * **Relação de Recorrência (informal):** $T(n) = n \cdot T(n-1)$, onde $n$ é o número de vértices a visitar.
  * **Complexidade:** O número total de caminhos explorados na árvore de recursão é da ordem de $V!$ (V fatorial). Como a função principal pode iniciar a busca de $V$ vértices diferentes, a complexidade de tempo total do algoritmo é **$O(V \cdot V!)$**. Esta é uma complexidade fatorial, que cresce mais rápido que a exponencial (ex: $O(2^n)$) e é considerada intratável para grafos que não sejam muito pequenos.

### 4.3. Aplicação do Teorema Mestre

**Referência:** AULA 02\_Introdução à teoria da complexidade.pdf - Páginas 199-212, 414-416, 1124

**Não é possível aplicar o Teorema Mestre** ao algoritmo de backtracking implementado.

**Justificativa:**
O Teorema Mestre é uma ferramenta para resolver recorrências de **divisão e conquista**, que seguem o formato estrito:
[cite\_start]$T(n) = a \cdot T(n/b) + f(n)$ [cite: 203-205].

[cite\_start]O Teorema Mestre exige que o problema seja dividido em subproblemas de tamanho *proporcional* (ex: $n/b$)[cite: 212, 415, 541].

Nosso algoritmo de backtracking usa uma abordagem *subtrativa*. A cada chamada recursiva, o "tamanho" do problema (o número de vértices restantes a visitar) é reduzido em 1. A recorrência se assemelha a $T(n) \approx n \cdot T(n-1)$, que não se encaixa no formato $T(n/b)$.

[cite\_start]Conforme visto na aula, algoritmos com recorrências baseadas em decrementos lineares (como $T(n-1)$) não podem ser analisados pelo Teorema Mestre e exigem outros métodos, como a **expansão de recorrência**[cite: 199, 214, 224, 260, 416].

### 4.4. Análise dos Casos de Complexidade (Pior, Médio, Melhor)

**Referência:** AULA 02\_Introdução à teoria da complexidade.pdf - Páginas 406-410, 532-536, 1132-1135

  * **Pior Caso:**

      * **Descrição:** Ocorre quando o algoritmo precisa explorar o maior número possível de caminhos parciais. Isso acontece se:
        1.  O grafo **não** possui Caminho Hamiltoniano. [cite\_start]O algoritmo deve explorar todas as $V!$ permutações (a partir de todas as $V$ origens) para provar que nenhuma funciona[cite: 407].
        2.  O grafo possui um caminho, mas ele é o último a ser encontrado (ex: começa no último vértice `inicio` testado, e os vizinhos corretos são sempre os últimos na lista de adjacência).
      * [cite\_start]**Complexidade:** $O(V \cdot V!)$ [cite: 1133-1134].

  * **Melhor Caso:**

      * [cite\_start]**Descrição:** Ocorre quando o algoritmo encontra o caminho na primeira tentativa, sem retroceder (backtracking)[cite: 410, 536].
      * **Exemplo:** O algoritmo inicia a busca no vértice `0` (primeira iteração da função principal). O primeiro vizinho de `0` é `1`, o primeiro vizinho de `1` (não visitado) é `2`, e assim por diante, formando um caminho `0-1-2-...-(V-1)` que é Hamiltoniano.
      * **Complexidade:** $O(V)$. O algoritmo faz apenas $V$ chamadas recursivas (uma para cada vértice no caminho) e termina.

  * **Caso Médio:**

      * **Descrição:** O desempenho médio depende muito da estrutura (densidade) do grafo. Em grafos esparsos, os caminhos são "podados" (backtrack) rapidamente, pois os vértices têm poucos vizinhos. [cite\_start]Em grafos densos, mais caminhos precisam ser explorados[cite: 409, 535].
      * **Complexidade:** Apesar de "podar" a árvore de busca, o número de caminhos a explorar em um grafo aleatório médio ainda é exponencial/fatorial. A complexidade do caso médio ainda é intratável e muito mais próxima do Pior Caso do que do Melhor Caso.

-----

## 5\. Visualização (Ponto Extra Opcional)

A funcionalidade de visualização está agora **integrada** ao `main.py`. Se um caminho Hamiltoniano for encontrado e as bibliotecas `networkx` e `matplotlib` estiverem instaladas, o script irá automaticamente:

1.  Gerar uma visualização do grafo.
2.  Destacar o caminho encontrado em vermelho.
3.  Salvar a imagem como `assets/caminho_hamiltoniano.png`.
4.  Exibir a imagem em uma nova janela.

*(Esta imagem é um placeholder. Execute o script com as bibliotecas instaladas para gerar a sua.)*

-----

## 6\. Conclusões Técnicas

1.  [cite\_start]**Classificação Comprovada**: O Problema do Caminho Hamiltoniano é um exemplo clássico de um problema **NP-Completo**[cite: 1015]. [cite\_start]Embora sua solução seja *difícil de encontrar* (requer tempo fatorial $O(V!)$ com backtracking), ela é *fácil de verificar* (em tempo linear $O(V)$), colocando-o firmemente na classe NP[cite: 1003].
2.  **Limites do Teorema Mestre**: A análise deste algoritmo demonstra um limite chave do Teorema Mestre. [cite\_start]Ele não é aplicável a algoritmos recursivos que reduzem o problema de forma subtrativa (ex: $T(n-1)$) [cite: 223, 415, 541][cite\_start], sendo necessário usar métodos como expansão de recorrência[cite: 224].
3.  **O Custo do Backtracking**: A implementação demonstra o poder e o custo do backtracking. [cite\_start]Embora encontre a solução correta, seu desempenho no pior caso ($O(V!)$) [cite: 408] [cite\_start]o torna inviável para grafos de tamanho moderado[cite: 17, 196], justificando por que problemas NP-Completos são considerados "intratáveis" na prática.
4.  [cite\_start]**Variação de Desempenho**: O algoritmo tem uma diferença drástica entre o melhor caso ($O(V)$) [cite: 410, 536] [cite\_start]e o pior caso ($O(V!)$)[cite: 408, 534], destacando como a estrutura específica da entrada pode impactar drasticamente o tempo de execução.

-----

## 7\. Referências

  * **AULA 02\_Introdução à teoria da complexidade.pdf** (Material da disciplina)
  * CORMEN, T. H. et al. *Algoritmos: Teoria e Prática*. 3.ed. [cite\_start]São Paulo: GEN LTC, 2012[cite: 1139].
  * ZIVIANI, Nivio. *Projeto de algoritmos: com implementações em Java e C++*. [cite\_start]São Paulo: Cengage Learning, c2007[cite: 1144].
  * [cite\_start]Repositório do Professor: `https://github.com/joaopauloaramuni/fundamentos-de-projeto-e-analise-de-algoritmos` [cite: 137, 546, 557, 1109, 1200, 1230]