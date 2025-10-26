import networkx as nx
import matplotlib.pyplot as plt
import os
from main import Grafo

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
            if not orientado and (v, u) in arestas_originais:
                continue
            arestas_originais.append((u, v))
            
    G.add_edges_from(arestas_originais)

    # Definir layout
    pos = nx.spring_layout(G, seed=42)
    
    plt.figure(figsize=(12, 8))
    
    # 2. Desenhar o grafo original
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue', alpha=0.9)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
    nx.draw_networkx_edges(G, pos, edgelist=arestas_originais, width=1, alpha=0.3, 
                          edge_color='gray', style='dashed')

    # 3. Destacar o Caminho Hamiltoniano
    if caminho_encontrado:
        arestas_caminho = []
        for i in range(len(caminho_encontrado) - 1):
            u = caminho_encontrado[i]
            v = caminho_encontrado[i+1]
            arestas_caminho.append((u, v))
            
        # Desenha as arestas do caminho
        nx.draw_networkx_edges(G, pos, edgelist=arestas_caminho, 
                               width=3, alpha=0.9, edge_color='red', 
                               arrows=orientado, arrowsize=20)
        
        # Destaca os nós do caminho
        nx.draw_networkx_nodes(G, pos, nodelist=caminho_encontrado, 
                              node_color='red', node_size=800)
        
        plt.title(f"✅ Caminho Hamiltoniano Encontrado\n{caminho_encontrado}", 
                 fontsize=16, pad=20)
    else:
        plt.title("❌ Grafo (Nenhum Caminho Hamiltoniano Encontrado)", 
                 fontsize=16, pad=20)

    plt.axis('off')

    # 4. Salvar a imagem
    if not os.path.exists('assets'):
        os.makedirs('assets')
        
    caminho_salvar = 'assets/caminho_hamiltoniano.png'
    plt.savefig(caminho_salvar, bbox_inches='tight', dpi=150)
    print(f"\n📊 Visualização salva em: {caminho_salvar}")
    plt.show()

def main_visualizacao():
    """Função principal para visualização interativa"""
    print("=== Visualização do Caminho Hamiltoniano ===")
    
    # Usar o mesmo input do main.py
    from main import main as main_algoritmo
    
    # Executar o algoritmo principal
    print("Primeiro, vamos configurar o grafo:")
    V = int(input("Digite o número total de vértices: "))
    
    orientado_input = input("O grafo é orientado? (s/n): ").strip().lower()
    orientado = orientado_input in ['s', 'sim']
    
    grafo = Grafo(V, orientado)
    
    E = int(input("Digite o número total de arestas: "))
    
    print(f"Digite as {E} arestas (formato: origem destino)")
    for i in range(E):
        aresta_input = input(f"Aresta {i+1}: ").strip().split()
        u = int(aresta_input[0])
        v = int(aresta_input[1])
        grafo.adicionar_aresta(u, v)
    
    # Encontrar caminho
    print("\nExecutando algoritmo...")
    caminho = grafo.encontrar_caminho_hamiltoniano()
    
    if caminho:
        print(f"Caminho encontrado: {caminho}")
        print("Gerando visualização...")
        visualizar_caminho(grafo, caminho, orientado)
    else:
        print("Nenhum caminho Hamiltoniano encontrado.")
        print("Gerando visualização do grafo...")
        visualizar_caminho(grafo, None, orientado)

if __name__ == "__main__":
    main_visualizacao()