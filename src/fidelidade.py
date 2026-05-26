def calcular_desconto_fidelidade(pontos: int) -> float:
    if pontos < 0:
        raise ValueError("Os pontos não podem ser negativos")

    return pontos * 0.5
