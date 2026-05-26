import pytest
from src.desconto import calcular_desconto


def test_deve_aplicar_desconto_corretamente():
    # Act
    resultado = calcular_desconto(100.0, 10.0)

    # Assert
    assert resultado == 90.0


def test_deve_lancar_erro_quando_percentual_for_invalido():
    # Act & Assert
    with pytest.raises(ValueError, match="Percentual inválido"):
        calcular_desconto(50.0, 150.0)


def test_deve_aplicar_desconto_maximo_total_gratuito():
    # Act
    resultado = calcular_desconto(50.0, 100.0)

    # Assert
    assert resultado == 0.0
