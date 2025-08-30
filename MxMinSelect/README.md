# Implementação do Algoritmo de Seleção Simultânea (MaxMin Select) em Python 🔎

**Trabalho Individual 2 - Fundamentos de Projeto e Análise de Algoritmos**

Este projeto apresenta uma implementação em Python do algoritmo **MaxMin Select**, que encontra de forma simultânea o maior e o menor elemento de uma sequência de números. A abordagem utilizada é a de

**divisão e conquista**, que otimiza o número de comparações necessárias1.

----------

## 📜 Descrição do Projeto

O algoritmo de seleção simultânea, ou MaxMin Select, é uma técnica recursiva que demonstra o poder da estratégia de divisão e conquista2. Em vez de encontrar o menor e o maior elemento de forma independente (o que exigiria aproximadamente

2n−2 comparações), este método reduz o problema em subproblemas menores, resolve-os recursivamente e combina seus resultados de forma eficiente3. Essa abordagem diminui significativamente o número total de comparações em relação a um método ingênuo4.

### 🧠 Lógica do Algoritmo (linha a linha)

Para encontrar o menor (`min`) e o maior (`max`) elemento em uma lista `arr` de tamanho `n`:

1.  **Caso Base 1**: Se a lista contém apenas um elemento, ele é, ao mesmo tempo, o menor e o maior.
    
    Python
    
    ```
    if n == 1:
        return arr[0], arr[0]
    
    ```
    
2.  **Caso Base 2**: Se a lista contém dois elementos, uma única comparação é suficiente para determinar qual é o menor e qual é o maior.
    
    Python
    
    ```
    if n == 2:
        if arr[0] < arr[1]:
            return arr[0], arr[1]
        else:
            return arr[1], arr[0]
    
    ```
    
3.  **Divisão**: Se a lista tem mais de dois elementos, ela é dividida ao meio.
    
    Python
    
    ```
    meio = n // 2
    
    ```
    
4.  **Chamadas Recursivas (Conquista)**: O algoritmo é chamado recursivamente para a metade esquerda e para a metade direita da lista.
    
    Python
    
    ```
    min_esquerdo, max_esquerdo = max_min_select(arr[:meio])
    min_direito, max_direito = max_min_select(arr[meio:])
    
    ```
    
5.  **Combinação**: Os resultados das duas metades são combinados para encontrar o `min` e o `max` globais. Isso requer apenas duas comparações adicionais: uma para encontrar o menor entre `min_esquerdo` e `min_direito`, e outra para encontrar o maior entre `max_esquerdo` e `max_direito`.
    
    Python
    
    ```
    menor_final = min(min_esquerdo, min_direito)
    maior_final = max(max_esquerdo, max_direito)
    
    return menor_final, maior_final
    
    ```
    

----------

## ⚙️ Como Executar o Projeto

Para executar o código em seu ambiente local, siga as instruções abaixo:

1.  **Clone o repositório:**
    
    Bash
    
    ```
    # Exemplo de comando para clonar o repositório
    git clone https://github.com/seu-usuario/trabalho_individual_2_FPAA.git
    cd trabalho_individual_2_FPAA
    
    ```
    
2.  Execute o arquivo main.py:
    
    O script já contém exemplos fixos e aleatórios para demonstrar o funcionamento do algoritmo.
    
    Bash
    
    ```
    python main.py
    
    ```
    

O programa exibirá o resultado da busca pelo maior e menor elemento usando o algoritmo MaxMin Select e também os resultados das funções `min()` e `max()` do Python para verificação.

----------

## 📊 Relatório Técnico

### Análise de Complexidade Assintótica pelo Método de Contagem de Operações

Esta análise foca em detalhar o número de comparações que o algoritmo realiza5.

-   **Relação de Recorrência**: Seja C(n) o número de comparações para uma entrada de tamanho n.
    
    -   **Casos Base**:
        
        -   C(1)=0 (nenhuma comparação)
            
        -   C(2)=1 (uma comparação)
            
    -   **Passo Recursivo**: Para dividir o problema, o algoritmo realiza duas chamadas recursivas em subproblemas de tamanho n/2. Para combinar os resultados, são necessárias duas comparações adicionais (uma para os mínimos, outra para os máximos)6.
        
        Portanto, a recorrência é:
        
        C(n)=2⋅C(n/2)+2
        
-   Cálculo do Total de Comparações:
    
    Para n sendo uma potência de 2, n=2k, podemos expandir a recorrência:
    
    C(n)=2cdotC(n/2)+2
    
    C(n)=2cdot(2C(n/4)+2)+2=4C(n/4)+4+2
    
    C(n)=4cdot(2C(n/8)+2)+6=8C(n/8)+8+6
    
    Generalizando, para um nível i da recursão, temos 2i subproblemas e um custo de 2icdot2=2i+1 na combinação. A profundidade da recursão é k=log_2n. O total de comparações é a soma das comparações em cada nível, resultando em aproximadamente:
    
    C(n)≈23n​−2
    
    Como o número de comparações cresce linearmente com
    
    n, a complexidade temporal é **O(n)**7.
    

### Análise de Complexidade Assintótica pela Aplicação do Teorema Mestre

O Teorema Mestre oferece uma forma direta de resolver relações de recorrência no formato

T(n)=acdotT(n/b)+f(n)8888.

-   **Recorrência do MaxMin Select**:
    
    T(n)=2T(n/2)+O(1)
    
    Onde:
    
    -   2T(n/2): Representa as duas chamadas recursivas para subproblemas de metade do tamanho9.
        
    -   O(1): Representa o custo constante de combinar os resultados (duas comparações)10.
        
-   **Aplicação do Teorema**:
    
    1.  **Identificar os valores de a, b e f(n)**11:
        
        -   a=2 (número de subproblemas)
            
        -   b=2 (fator de redução do tamanho do problema)
            
        -   f(n)=O(1) (custo externo, que é constante)
            
    2.  **Calcular log_ba**12:
        
        p=log2​2=1
        
    3.  **Determinar o caso do Teorema Mestre**13:
        
        Comparamos o crescimento de f(n) com nlog_ba=n1.
        
        -   f(n)=O(1)
            
        -   nlog_ba=n1
            
            Como
            
            f(n)=O(1) cresce mais lentamente que n1, a condição do **Caso 1** do Teorema Mestre é satisfeita: f(n)=O(nlog_ba−epsilon) para um epsilon0 (neste caso, epsilon=1)14.
            
    4.  **Encontrar a solução assintótica**15:
        
        De acordo com o Caso 1, a complexidade é dominada pelo custo das chamadas recursivas16. A solução é:
        
        T(n)=Θ(nlogb​a)=Θ(n1)=Θ(n)
        

Ambas as análises confirmam que o algoritmo MaxMin Select possui uma complexidade de tempo linear, **O(n)**.