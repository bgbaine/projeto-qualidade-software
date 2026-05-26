import pytest
from src.pedido import calcular_total_pedido


def test_deve_calcular_total_do_pedido_com_itens_e_taxa():
    # Arrange
    itens = [20.0, 30.0]  # Total itens: 50.0
    taxa_entrega = 5.0
    desconto = 10.0

    # Act
    resultado = calcular_total_pedido(itens, taxa_entrega, desconto)

    # Assert
    assert resultado == 45.0


def test_deve_retornar_zero_quando_desconto_for_maior_que_o_total():
    # Arrange
    itens = [10.0]
    taxa_entrega = 5.0
    desconto = 50.0  # Desconto muito alto

    # Act
    resultado = calcular_total_pedido(itens, taxa_entrega, desconto)

    # Assert
    assert resultado == 0.0


def test_deve_lancar_erro_quando_lista_de_itens_estiver_vazia():
    # Act & Assert
    with pytest.raises(ValueError, match="Pedido deve ter pelo menos um item"):
        calcular_total_pedido([], 5.0, 0.0)
