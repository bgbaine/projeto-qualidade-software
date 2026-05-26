def calcular_desconto(valor_pedido, percentual_desconto):
    if percentual_desconto < 0 or percentual_desconto > 100:
        raise ValueError("Percentual inválido")

    desconto = valor_pedido * (percentual_desconto / 100)
    return valor_pedido - desconto
