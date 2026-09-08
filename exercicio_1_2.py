import math
import random
import matplotlib.pyplot as plt



# CÁLCULO ANALÍTICO


def disponibilidade_analitica(n, k, p):
    """
    Calcula a disponibilidade teórica do serviço.
    """

    disponibilidade = 0

    for i in range(k, n + 1):
        disponibilidade += (
            math.comb(n, i)
            * (p ** i)
            * ((1 - p) ** (n - i))
        )

    return disponibilidade



# SIMULAÇÃO ESTOCÁSTICA


def disponibilidade_simulada(n, k, p, rodadas=100000):
    """
    Estima a disponibilidade através de simulação.
    """

    sucessos = 0

    for _ in range(rodadas):

        servidores_disponiveis = 0

        for _ in range(n):

            if random.random() <= p:
                servidores_disponiveis += 1

        if servidores_disponiveis >= k:
            sucessos += 1

    return sucessos / rodadas



# COMPARAÇÃO


n = 8
valores_k = [1, 4, 8]

valores_p = [
    0.1, 0.2, 0.3, 0.4, 0.5,
    0.6, 0.7, 0.8, 0.9, 1.0
]

for k in valores_k:

    analitico = []
    experimental = []

    print(f"\n===== n={n} | k={k} =====")

    for p in valores_p:

        a = disponibilidade_analitica(n, k, p)
        s = disponibilidade_simulada(n, k, p)

        analitico.append(a)
        experimental.append(s)

        print(
            f"p={p:.1f} | "
            f"Analítico={a:.4f} | "
            f"Experimental={s:.4f}"
        )

    # ---------------- Gráfico ----------------

    plt.figure(figsize=(8,5))

    plt.plot(
        valores_p,
        analitico,
        marker="o",
        label="Analítico"
    )

    plt.plot(
        valores_p,
        experimental,
        marker="x",
        linestyle="--",
        label="Experimental"
    )

    plt.title(f"Disponibilidade (n={n}, k={k})")
    plt.xlabel("Probabilidade p")
    plt.ylabel("Disponibilidade")
    plt.ylim(0, 1.05)
    plt.grid(True)
    plt.legend()

    plt.show()
