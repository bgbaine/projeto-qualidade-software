import pytest
from src.fidelidade import calcular_desconto_fidelidade


def test_deve_calcular_desconto_com_pontos_validos():
    # Arrange
    pontos = 50
    # Act
    desconto = calcular_desconto_fidelidade(pontos)
    # Assert
    assert desconto == 25.0


def test_deve_retornar_zero_se_nao_tiver_pontos():
    # Arrange
    pontos = 0
    # Act
    desconto = calcular_desconto_fidelidade(pontos)
    # Assert
    assert desconto == 0.0


def test_deve_lancar_erro_para_pontos_negativos():
    # Act & Assert
    with pytest.raises(ValueError, match="Os pontos não podem ser negativos"):
        calcular_desconto_fidelidade(-10)
