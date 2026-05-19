import pytest

from src.entrega import calcular_taxa_entrega


def test_deve_cobrar_taxa_fixa_para_distancia_ate_3km():
    # Arrange
    distancia = 2.5

    # Act
    resultado = calcular_taxa_entrega(distancia)

    # Assert
    assert resultado == 5.0


def test_deve_lancar_erro_quando_distancia_for_negativa():
    # Arrange
    distancia_invalida = -1.5

    # Act & Assert
    with pytest.raises(ValueError, match="Distância inválida"):
        calcular_taxa_entrega(distancia_invalida)


def test_deve_cobrar_taxa_proporcional_acima_de_3km():
    # Arrange
    distancia = 5.0

    # Act
    resultado = calcular_taxa_entrega(distancia)

    # Assert
    assert resultado == 9.0
