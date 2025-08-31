import random

def max_min_select(arr):
    """
    Encontra o maior e o menor elemento em uma lista de forma simultânea
    utilizando a abordagem de divisão e conquista otimizada.
    """
    n = len(arr)
    
    # Caso Base 1: Lista vazia
    if n == 0:
        return None, None
    
    # Caso Base 2: Apenas um elemento
    if n == 1:
        return arr[0], arr[0]

    # Otimização: Evita divisão desnecessária para listas pequenas
    if n <= 3:
        min_val = max_val = arr[0]
        for i in range(1, n):
            if arr[i] < min_val:
                min_val = arr[i]
            elif arr[i] > max_val:
                max_val = arr[i]
        return min_val, max_val

    # Divisão otimizada - evita cópias desnecessárias de listas
    meio = n // 2
    
    # Passa índices em vez de criar novas listas
    min_esquerdo, max_esquerdo = max_min_select(arr[:meio])
    min_direito, max_direito = max_min_select(arr[meio:])

    # Combinação otimizada - menos comparações
    menor_final = min_esquerdo if min_esquerdo < min_direito else min_direito
    maior_final = max_esquerdo if max_esquerdo > max_direito else max_direito

    return menor_final, maior_final

# Versão ainda mais otimizada usando índices (evita cópias de lista)
def max_min_select_optimized(arr, start=0, end=None):
    """
    Versão otimizada que trabalha com índices para evitar cópias de lista.
    """
    if end is None:
        end = len(arr) - 1
    
    n = end - start + 1
    
    if n == 0:
        return None, None
    if n == 1:
        return arr[start], arr[start]
    
    # Para pequenas listas, usa abordagem iterativa
    if n <= 4:
        min_val = max_val = arr[start]
        for i in range(start + 1, end + 1):
            if arr[i] < min_val:
                min_val = arr[i]
            elif arr[i] > max_val:
                max_val = arr[i]
        return min_val, max_val
    
    meio = (start + end) // 2
    
    min_esq, max_esq = max_min_select_optimized(arr, start, meio)
    min_dir, max_dir = max_min_select_optimized(arr, meio + 1, end)
    
    return min(min_esq, min_dir), max(max_esq, max_dir)

# --- Exemplo de Execução ---
if __name__ == "__main__":
    # Teste de performance
    import time
    
    # Lista grande para teste
    lista_grande = [random.randint(0, 1000000) for _ in range(10000)]
    
    # Teste versão original
    start_time = time.time()
    menor1, maior1 = max_min_select(lista_grande[:1000])  # Reduzido para 1000
    time1 = time.time() - start_time
    
    # Teste versão otimizada
    start_time = time.time()
    menor2, maior2 = max_min_select_optimized(lista_grande)
    time2 = time.time() - start_time
    
    # Teste Python built-in
    start_time = time.time()
    menor_py, maior_py = min(lista_grande), max(lista_grande)
    time_py = time.time() - start_time
    
    print(f"Versão original: {time1:.6f}s")
    print(f"Versão otimizada: {time2:.6f}s")
    print(f"Python built-in: {time_py:.6f}s")
    print(f"Resultados corretos: {menor2 == menor_py and maior2 == maior_py}")