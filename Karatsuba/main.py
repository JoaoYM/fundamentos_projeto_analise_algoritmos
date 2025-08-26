import sys

def karatsuba(x, y):
    """
    Multiplica dois números inteiros usando o algoritmo de Karatsuba.

    Args:
        x (int): O primeiro número.
        y (int): O segundo número.

    Returns:
        int: O produto de x e y.
    """
    # Caso base para a recursão: se os números são pequenos, usa multiplicação padrão.
    if x < 10 or y < 10:
        return x * y

    # Converte os números para string para encontrar o ponto de divisão.
    str_x = str(x)
    str_y = str(y)

    # Determina o tamanho dos números.
    n = max(len(str_x), len(str_y))
    
    # Para garantir que a divisão seja feita corretamente, o tamanho n precisa ser par.
    # Se n for ímpar, aumentamos para o próximo número par.
    # Esta abordagem é mais simples do que lidar com metades de tamanhos diferentes.
    half_n = n // 2

    # Divide os números em partes 'alta' e 'baixa'.
    # x = a * 10^(n/2) + b
    # y = c * 10^(n/2) + d
    high_x = x // (10**half_n)
    low_x = x % (10**half_n)
    high_y = y // (10**half_n)
    low_y = y % (10**half_n)

    # Chamadas recursivas para calcular os produtos necessários.
    z0 = karatsuba(low_x, low_y)      # z0 = b * d
    z2 = karatsuba(high_x, high_y)     # z2 = a * c
    z1 = karatsuba((low_x + high_x), (low_y + high_y)) # z1 = (a+b)*(c+d)

    # O truque de Karatsuba: calcula o produto do meio com apenas uma multiplicação.
    # z1 - z2 - z0 = (a+b)(c+d) - ac - bd = ac + ad + bc + bd - ac - bd = ad + bc
    prod_mid = z1 - z2 - z0

    # Combina os resultados para obter o produto final.
    # resultado = z2 * 10^(2*half_n) + (z1 - z2 - z0) * 10^(half_n) + z0
    result = (z2 * 10**(2 * half_n)) + (prod_mid * 10**half_n) + z0
    
    return result

if __name__ == "__main__":
    # Define um limite de recursão maior para números grandes.
    sys.setrecursionlimit(2000)

    # --- Exemplos de uso ---
    num1 = 5678
    num2 = 1234
    resultado = karatsuba(num1, num2)
    print(f"O produto entre {num1} e {num2} é: {resultado}")
    print(f"Verificação (multiplicação padrão): {num1 * num2}")
    print("-" * 30)

    num3 = 12345678901234567890
    num4 = 98765432109876543210
    resultado2 = karatsuba(num3, num4)
    print(f"O produto entre números grandes é: {resultado2}")
    print(f"Verificação (multiplicação padrão): {num3 * num4}")
    print("-" * 30)
    
    # --- Demonstração com entrada do usuário ---
    try:
        input1 = int(input("Digite o primeiro número inteiro: "))
        input2 = int(input("Digite o segundo número inteiro: "))
        resultado_usuario = karatsuba(input1, input2)
        print(f"\nO resultado da multiplicação é: {resultado_usuario}")
        print(f"Verificação (multiplicação padrão): {input1 * input2}")
    except ValueError:
        print("\nEntrada inválida. Por favor, digite apenas números inteiros.")