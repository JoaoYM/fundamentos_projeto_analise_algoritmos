# view.py
# Função para visualizar o grafo e o Caminho Hamiltoniano (Ponto Extra)

import networkx as nx
import matplotlib.pyplot as plt
import os
from main import Grafo # Importa a classe do arquivo principal

def visualizar_caminho(grafo_obj, caminho_encontrado, orientado=False):
    """
    Desenha o grafo e destaca o Caminho Hamiltoniano, se encontrado.
    Salva a imagem em 'assets/caminho_hamiltoniano.png'
    """
    
    # 1. Criar o objeto de grafo do NetworkX
    if orientado:
        G = nx.DiGraph()
    else:
        G = nx.Graph()
    
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
    if caminho_encontrado:
        arestas_caminho = []
        for i in range(len(caminho_encontrado) - 1):
            u = caminho_encontrado[i]
            v = caminho_encontrado[i+1]
            arestas_caminho.append((u, v))
            
        # Desenha as arestas do caminho
        nx.draw_networkx_edges(G, pos, edgelist=arestas_caminho, 
                               width=2.5, alpha=0.8, edge_color='red')
        
        # Destaca os nós do caminho
        nx.draw_networkx_nodes(G, pos, nodelist=caminho_encontrado, node_color='red', node_size=700)
        
        plt.title(f"Caminho Hamiltoniano Encontrado (Vermelho)\n{caminho_encontrado}", fontsize=16)
    else:
        plt.title("Grafo (Nenhum Caminho Hamiltoniano Encontrado)", fontsize=16)

    plt.axis('off') # Remove os eixos

    # 4. Salvar a imagem em /assets
    # Garante que o diretório 'assets' exista
    if not os.path.exists('assets'):
        os.makedirs('assets')
        
    caminho_salvar = 'assets/caminho_hamiltoniano.png'
    plt.savefig(caminho_salvar, bbox_inches='tight', dpi=150)
    print(f"\nVisualização salva em: {caminho_salvar}")
    plt.show()

# --- Exemplo de Uso ---
if __name__ == "__main__":
    # Reutiliza o Exemplo 1 do main.py
    g_vis = Grafo(5)
    g_vis.adicionar_aresta(0, 1)
    g_vis.adicionar_aresta(1, 2)
    g_vis.adicionar_aresta(2, 3)
    g_vis.adicionar_aresta(3, 4)
    g_vis.adicionar_aresta(1, 3)
    g_vis.adicionar_aresta(1, 4)

    # Encontra o caminho
    print("Executando 'encontrar_caminho_hamiltoniano' para visualização...")
    caminho = g_vis.encontrar_caminho_hamiltoniano()
    
    # Visualiza
    if caminho:
        print(f"Visualizando caminho: {caminho}")
        visualizar_caminho(g_vis, caminho, orientado=False)
    else:
        print("Visualizando grafo (sem caminho encontrado).")
        visualizar_caminho(g_vis, None, orientado=False)