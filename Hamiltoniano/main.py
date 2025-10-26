# main.py
# Implementação do Algoritmo para Caminho Hamiltoniano usando Backtracking
# (Com visualização opcional integrada)

import os
try:
    # Tenta importar as bibliotecas opcionais de visualização
    import networkx as nx
    import matplotlib.pyplot as plt
    VISUALIZACAO_DISPONIVEL = True
except ImportError:
    # Se falhar, desativa a visualização e avisa o usuário
    VISUALIZACAO_DISPONIVEL = False
    print("\nAviso: Bibliotecas 'networkx' e 'matplotlib' não encontradas.")
    print("A visualização do grafo será desativada.")
    print("Para ativar, instale com: pip install networkx matplotlib\n")


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
            # Informa o usuário sobre a aresta inválida, mas continua
            print(f"Aviso: Vértices {u} ou {v} fora do intervalo [0, {self.V-1}]. Aresta ignorada.")

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

        # Se o loop terminar sem sucesso
        return None

def visualizar_caminho_encontrado(grafo_obj, caminho, orientado=False):
    """
    (Função Opcional)
    Desenha o grafo e destaca o Caminho Hamiltoniano encontrado.
    Salva a imagem em 'assets/caminho_hamiltoniano.png'
    """
    
    # 1. Criar o objeto de grafo do NetworkX
    G = nx.DiGraph() if orientado else nx.Graph()
    
    # Adicionar nós
    for i in range(grafo_obj.V):
        G.add_node(i)
        
    # Adicionar arestas originais
    arestas_originais = []
    for u in range(grafo_obj.V):
        for v in grafo_obj.adj[u]:
            # Evitar duplicatas em grafos não orientados se nx.Graph
            if not orientado and (v, u) in arestas_originais:
                continue
            arestas_originais.append((u, v))
    G.add_edges_from(arestas_originais)

    # Definir layout
    pos = nx.spring_layout(G, seed=42) # Layout consistente
    
    plt.figure(figsize=(10, 7))
    
    # 2. Desenhar o grafo original (nós e arestas)
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue', alpha=0.9)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
    nx.draw_networkx_edges(G, pos, edgelist=arestas_originais, width=1, alpha=0.3, edge_color='gray', style='dashed')

    # 3. Destacar o Caminho Hamiltoniano
    arestas_caminho = []
    for i in range(len(caminho) - 1):
        arestas_caminho.append((caminho[i], caminho[i+1]))
        
    # Desenha as arestas do caminho
    nx.draw_networkx_edges(G, pos, edgelist=arestas_caminho, 
                           width=2.5, alpha=0.8, edge_color='red')
    
    # Destaca os nós do caminho
    nx.draw_networkx_nodes(G, pos, nodelist=caminho, node_color='red', node_size=700)
    
    plt.title(f"Caminho Hamiltoniano Encontrado (Vermelho)\n{caminho}", fontsize=16)
    plt.axis('off') # Remove os eixos

    # 4. Salvar a imagem em /assets
    # Garante que o diretório 'assets' exista
    if not os.path.exists('assets'):
        os.makedirs('assets')
        
    caminho_salvar = 'assets/caminho_hamiltoniano.png'
    plt.savefig(caminho_salvar, bbox_inches='tight', dpi=150)
    print(f"\nVisualização salva em: {caminho_salvar}")
    
    # Mostra o gráfico na tela
    plt.show()

def main():
    """
    Função principal para capturar a entrada do usuário e executar o algoritmo.
    """
    try:
        # --- 1. Obter Número de Vértices ---
        while True:
            num_vertices_input = input("Digite o número total de vértices: ")
            try:
                num_vertices = int(num_vertices_input)
                if num_vertices <= 0:
                    print("O número de vértices deve ser positivo.")
                    continue
                break
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

        # --- 2. Obter Orientação do Grafo ---
        orientado_input = input("O grafo é orientado? (s/n): ").strip().lower()
        orientado = (orientado_input == 's')
        
        # --- 3. Inicializar o Grafo ---
        g = Grafo(num_vertices)
        
        # --- 4. Obter Número de Arestas ---
        while True:
            num_arestas_input = input("Digite o número total de arestas: ")
            try:
                num_arestas = int(num_arestas_input)
                if num_arestas < 0:
                    print("O número de arestas não pode ser negativo.")
                    continue
                break
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

        # --- 5. Obter Arestas ---
        if num_arestas > 0:
            print(f"\nDigite as {num_arestas} arestas (formato: origem destino):")
            for i in range(num_arestas):
                while True:
                    aresta_input = input(f"Aresta {i+1}: ")
                    try:
                        u, v = map(int, aresta_input.split())
                        # Validação para garantir que os vértices estão no range
                        if not (0 <= u < num_vertices and 0 <= v < num_vertices):
                            print(f"Erro: Vértices devem estar no intervalo [0, {num_vertices-1}]. Tente novamente.")
                            continue
                        
                        g.adicionar_aresta(u, v, orientado)
                        break # Input da aresta foi válido
                    
                    except ValueError:
                        print("Formato inválido. Digite dois números inteiros separados por espaço.")
                    except IndexError:
                        print("Formato inválido. Digite dois números inteiros separados por espaço.")

        # --- 6. Executar e Imprimir Resultado ---
        print("\n--- Buscando Caminho Hamiltoniano ---")
        caminho = g.encontrar_caminho_hamiltoniano()
        
        if caminho:
            print("Resultado:", caminho)
            
            # --- 7. Tentar Visualização (Opcional) ---
            if VISUALIZACAO_DISPONIVEL:
                print("Gerando visualização do grafo...")
                try:
                    visualizar_caminho_encontrado(g, caminho, orientado)
                except Exception as e:
                    print(f"\nOcorreu um erro durante a visualização: {e}")
                    print("Isso pode ser um problema com o backend do Matplotlib ou Tkinter.")
            else:
                 print("(Visualização desativada. Instale 'networkx' e 'matplotlib' para habilitar.)")

        else:
            print("Resultado: Nenhum Caminho Hamiltoniano foi encontrado.")

    except KeyboardInterrupt:
        print("\nOperação interrompida pelo usuário.")
    except EOFError:
        print("\nEntrada finalizada.")

if __name__ == "__main__":
    main()