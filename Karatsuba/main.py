import sys
import math

def karatsuba(x, y):
    """Multiplica dois números inteiros usando o algoritmo de Karatsuba."""

    # Caso base: usa multiplicação padrão quando os números são pequenos
    if x < 1000 or y < 1000:
        return x * y

    # Determina o tamanho em dígitos decimais
    n = max(len(str(x)), len(str(y)))
    half_n = n // 2

    pow_half = 10 ** half_n

    # Divide os números
    high_x, low_x = divmod(x, pow_half)
    high_y, low_y = divmod(y, pow_half)

    # Recursão
    z0 = karatsuba(low_x, low_y)                      # b * d
    z2 = karatsuba(high_x, high_y)                    # a * c
    z1 = karatsuba(low_x + high_x, low_y + high_y)    # (a+b)(c+d)

    # Combinação
    return (z2 * 10**(2 * half_n)) + ((z1 - z2 - z0) * pow_half) + z0


if __name__ == "__main__":
    sys.setrecursionlimit(2000)

    num1, num2 = 5678, 1234
    print(f"O produto entre {num1} e {num2} é: {karatsuba(num1, num2)}")
    print(f"Verificação: {num1 * num2}")

    num3 = 1866666
    num4 = 158791
    print(f"O produto entre números grandes é: {karatsuba(num3, num4)}")
    print(f"Verificação: {num3 * num4}")
