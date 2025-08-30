import random

def max_min_select(arr):
    """
    Encontra o maior e o menor elemento em uma lista de forma simultânea
    utilizando a abordagem de divisão e conquista.

    Parâmetros:
    arr (list): A lista de números para análise.

    Retorna:
    tuple: Uma tupla contendo (menor_elemento, maior_elemento).
    """
    n = len(arr)

    # Caso Base 1: Se a lista tiver apenas um elemento.
    if n == 1:
        return arr[0], arr[0]

    # Caso Base 2: Se a lista tiver dois elementos, faz uma única comparação.
    if n == 2:
        if arr[0] < arr[1]:
            return arr[0], arr[1]
        else:
            return arr[1], arr[0]

    # Etapa de Divisão: Divide a lista em duas metades.
    meio = n // 2
    
    # Chamadas Recursivas para resolver os subproblemas.
    min_esquerdo, max_esquerdo = max_min_select(arr[:meio])
    min_direito, max_direito = max_min_select(arr[meio:])

    # Etapa de Combinação: Combina os resultados dos subproblemas.
    # Compara os menores das duas metades para encontrar o menor geral.
    menor_final = min(min_esquerdo, min_direito)
    
    # Compara os maiores das duas metades para encontrar o maior geral.
    maior_final = max(max_esquerdo, max_direito)

    return menor_final, maior_final

# --- Exemplo de Execução ---
if __name__ == "__main__":
    # Exemplo com uma lista fixa
    lista_exemplo = [10, 5, 25, 3, 42, 1, 88, 7]
    menor, maior = max_min_select(lista_exemplo)
    print(f"Lista de Exemplo: {lista_exemplo}")
    print(f"Resultado (MaxMin Select): Menor = {menor}, Maior = {maior}")
    print(f"Resultado (Padrão Python): Menor = {min(lista_exemplo)}, Maior = {max(lista_exemplo)}")
    print("-" * 30)

    # Exemplo com uma lista aleatória
    lista_aleatoria = [random.randint(0, 1000) for _ in range(20)]
    menor_aleatorio, maior_aleatorio = max_min_select(lista_aleatoria)
    print(f"Lista Aleatória: {lista_aleatoria}")
    print(f"Resultado (MaxMin Select): Menor = {menor_aleatorio}, Maior = {maior_aleatorio}")
    print(f"Resultado (Padrão Python): Menor = {min(lista_aleatoria)}, Maior = {max(lista_aleatoria)}")
    print("-" * 30)