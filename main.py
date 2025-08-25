from __future__ import annotations
import argparse

def karatsuba(x: int, y: int) -> int:
    """
    Multiplica dois inteiros x e y usando o algoritmo de Karatsuba.
    Suporta inteiros arbitrariamente grandes.
    """
    # 1) Lida com o sinal
    sign = -1 if (x < 0) ^ (y < 0) else 1
    a, b = abs(x), abs(y)

    # 2) Casos-base
    if a == 0 or b == 0:
        return 0
    if a < 10 and b < 10:
        return sign * (a * b)

    # 3) Ponto de corte
    n = max(len(str(a)), len(str(b)))
    m = n // 2

    # 4) Divide os números
    base = 10 ** m
    a_high, a_low = divmod(a, base)
    b_high, b_low = divmod(b, base)

    # 5) Recursão
    z2 = karatsuba(a_high, b_high)
    z0 = karatsuba(a_low, b_low)
    z1 = karatsuba(a_high + a_low, b_high + b_low) - z2 - z0

    # 6) Combinação
    result = (z2 * (10 ** (2 * m))) + (z1 * (10 ** m)) + z0

    return sign * result

def main() -> None:
    parser = argparse.ArgumentParser(description="Multiplicação de inteiros usando Karatsuba.")
    parser.add_argument("x", type=int, help="Primeiro inteiro")
    parser.add_argument("y", type=int, help="Segundo inteiro")
    parser.add_argument("--verify", action="store_true", help="Executa verificações contra a multiplicação nativa")
    args = parser.parse_args()

    prod = karatsuba(args.x, args.y)
    print(prod)

    if args.verify:
        pairs = [
            (0, 0), (0, 123456), (9, 8), (12, 34), (-12, 34), (1234, 5678),
            (10**20 + 12345, 10**18 + 6789),
            (args.x, args.y),
        ]
        for a, b in pairs:
            assert karatsuba(a, b) == a * b, f"Falha em {a} * {b}"
        print("[OK] Verificações rápidas passaram.")

if __name__ == "__main__":
    main()
