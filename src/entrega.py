def calcular_taxa_entrega(distancia):
    if distancia < 0:
        raise ValueError("Distância inválida")

    if distancia <= 3:
        return 5.0

    quilometros_extras = distancia - 3
    return 5.0 + (quilometros_extras * 2.0)
