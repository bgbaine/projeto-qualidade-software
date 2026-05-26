def calcular_total_pedido(itens, taxa_entrega, desconto):
    if not itens:
        raise ValueError("Pedido deve ter pelo menos um item")

    total = sum(itens) + taxa_entrega - desconto
    return max(0.0, total)
