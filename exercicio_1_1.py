import math


def disponibilidade(n, k, p):
    """
    Calcula a disponibilidade de um serviço replicado.

    n = número total de servidores
    k = número mínimo de servidores disponíveis
    p = probabilidade de cada servidor estar disponível
    """

    resultado = 0

    for i in range(k, n + 1):
        resultado += (
            math.comb(n, i)
            * (p ** i)
            * ((1 - p) ** (n - i))
        )

    return resultado


# Exemplos para testar a fórmula
n = 4
p = 0.8

# Caso k = 1
print("k = 1:", disponibilidade(n, 1, p))

# Caso k = n/2
print("k = n/2:", disponibilidade(n, n // 2, p))

# Caso k = n
print("k = n:", disponibilidade(n, n, p))
