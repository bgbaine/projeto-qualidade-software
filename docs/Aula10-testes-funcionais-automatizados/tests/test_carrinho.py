"""Testes funcionais (E2E) do fluxo de adição de item ao carrinho.

Fluxo escolhido: Adição de item ao carrinho (Fluxo 4).
Cobre: carrinho vazio ao abrir restaurante; atualização de contagem e total após adicionar.
"""

from pages.restaurant_page import RestaurantPage
from pages.cart_page import CartPage

RESTAURANTE_ID = 1


def test_carrinho_inicia_vazio(pagina_autenticada):
    """Ao abrir um restaurante o carrinho deve mostrar 0 itens e total R$ 0,00."""
    RestaurantPage(pagina_autenticada).acessar(RESTAURANTE_ID).aguardar_carregar()

    carrinho = CartPage(pagina_autenticada)
    assert carrinho.quantidade_de_itens() == 0
    assert carrinho.total_e_zero()


def test_adicionar_item_atualiza_carrinho(pagina_autenticada):
    """Adicionar um item deve incrementar a contagem e alterar o total no carrinho."""
    detalhe = RestaurantPage(pagina_autenticada).acessar(RESTAURANTE_ID).aguardar_carregar()
    assert detalhe.tem_itens_no_cardapio()

    detalhe.adicionar_primeiro_item()

    carrinho = CartPage(pagina_autenticada)
    carrinho.aguardar_item_adicionado()
    assert carrinho.quantidade_de_itens() == 1
    assert not carrinho.total_e_zero()
