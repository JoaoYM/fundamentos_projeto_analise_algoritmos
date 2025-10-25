# main.py
# Implementação do Algoritmo para Caminho Hamiltoniano usando Backtracking

class Grafo:
    """
    Classe para representar um grafo usando lista de adjacência.
    O grafo pode ser orientado ou não orientado.
    """
    def __init__(self, vertices):
        """
        Inicializa o grafo.
        :param vertices: Número de vértices (V)
        """
        self.V = vertices
        # Inicializa a lista de adjacência para V vértices (0 a V-1)
        self.adj = [[] for _ in range(vertices)]
        self.path = [] # Armazena o caminho hamiltoniano encontrado

    def adicionar_aresta(self, u, v, orientado=False):
        """
        Adiciona uma aresta ao grafo.
        :param u: Vértice de origem
        :param v: Vértice de destino
        :param orientado: Define se o grafo é orientado
        """
        # Adiciona aresta de u para v
        if 0 <= u < self.V and 0 <= v < self.V:
            self.adj[u].append(v)
            # Se não for orientado, adiciona a aresta de v para u também
            if not orientado:
                self.adj[v].append(u)
        else:
            print(f"Aviso: Vértices {u} ou {v} fora do intervalo [0, {self.V-1}]")

    def _backtrack_util(self, v, visitado):
        """
        Função utilitária recursiva (backtracking) para encontrar o caminho.
        """
        # 1. Adiciona o vértice atual 'v' ao caminho e marca como visitado
        self.path.append(v)
        visitado[v] = True

        # 2. Caso base: Se todos os vértices estão no caminho (comprimento == V),
        #    encontramos um Caminho Hamiltoniano.
        if len(self.path) == self.V:
            return True

        # 3. Tenta todos os vizinhos do vértice atual 'v'
        for vizinho in self.adj[v]:
            # 4. Verifica se o vizinho ainda não foi visitado
            if not visitado[vizinho]:
                # 5. Chamada recursiva: explora a partir do vizinho
                if self._backtrack_util(vizinho, visitado):
                    return True # Propaga o sucesso

        # 6. Backtrack: Se nenhum vizinho levou a uma solução,
        #    este caminho a partir de 'v' falhou.
        self.path.pop() # Remove 'v' do caminho
        visitado[v] = False # Desmarca 'v'
        return False

    def encontrar_caminho_hamiltoniano(self):
        """
        Função principal que tenta encontrar um Caminho Hamiltoniano.
        Tenta iniciar o caminho a partir de cada vértice, pois o
        caminho pode começar em qualquer lugar.
        """
        for inicio in range(self.V):
            # Reseta o caminho e o array de visitados para cada nova tentativa
            self.path = []
            visitado = [False] * self.V

            # Tenta encontrar o caminho a partir do vértice 'inicio'
            if self._backtrack_util(inicio, visitado):
                print(f"Caminho Hamiltoniano encontrado (iniciando em {inicio}):")
                return self.path

        print("Nenhum Caminho Hamiltoniano encontrado.")
        return None

# --- Exemplo de Uso ---
if __name__ == "__main__":
    
    # Exemplo 1: Grafo com Caminho Hamiltoniano
    print("--- Teste 1 (Grafo com caminho) ---")
    g1 = Grafo(5)
    g1.adicionar_aresta(0, 1)
    g1.adicionar_aresta(1, 2)
    g1.adicionar_aresta(2, 3)
    g1.adicionar_aresta(3, 4)
    g1.adicionar_aresta(1, 3) # Adicionando mais arestas
    g1.adicionar_aresta(1, 4)
    # Grafo: 0-1, 1-2, 1-3, 1-4, 2-3, 3-4

    caminho1 = g1.encontrar_caminho_hamiltoniano()
    if caminho1:
        print(caminho1) # Saída esperada: [0, 1, 2, 3, 4] ou similar

    print("\n--- Teste 2 (Grafo sem caminho) ---")
    # Exemplo 2: Grafo sem Caminho Hamiltoniano (desconexo)
    g2 = Grafo(5)
    g2.adicionar_aresta(0, 1)
    g2.adicionar_aresta(1, 2)
    g2.adicionar_aresta(3, 4) # Componente desconexo

    caminho2 = g2.encontrar_caminho_hamiltoniano()
    if caminho2:
        print(caminho2) # Saída esperada: Nenhum Caminho...

    print("\n--- Teste 3 (Grafo completo) ---")
    # Exemplo 3: Grafo completo (sempre tem caminho)
    g3 = Grafo(4)
    g3.adicionar_aresta(0, 1)
    g3.adicionar_aresta(0, 2)
    g3.adicionar_aresta(0, 3)
    g3.adicionar_aresta(1, 2)
    g3.adicionar_aresta(1, 3)
    g3.adicionar_aresta(2, 3)

    caminho3 = g3.encontrar_caminho_hamiltoniano()
    if caminho3:
        print(caminho3) # Saída esperada: [0, 1, 2, 3] ou qualquer permutação