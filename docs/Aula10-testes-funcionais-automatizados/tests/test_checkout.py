"""Testes funcionais (E2E) do fluxo de finalização de pedido (checkout).

Fluxo escolhido: Fluxo de pedido / checkout (Fluxo 5).
Cobre: finalizar pedido com item no carrinho, heading "Pedido Realizado!" e link 'Ver Detalhes'.
"""

import pytest

from pages.restaurant_page import RestaurantPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

RESTAURANTE_ID = 1


@pytest.fixture
def pagina_com_item_no_carrinho(pagina_autenticada):
    """Pré-condição: abre o restaurante diretamente e adiciona um item ao carrinho."""
    RestaurantPage(pagina_autenticada).acessar(RESTAURANTE_ID).aguardar_carregar().adicionar_primeiro_item()
    CartPage(pagina_autenticada).aguardar_item_adicionado()
    return pagina_autenticada


def test_finalizar_pedido_exibe_confirmacao(pagina_com_item_no_carrinho):
    """Com item no carrinho, 'Finalizar Pedido' deve exibir 'Pedido Realizado!'."""
    page = pagina_com_item_no_carrinho
    CartPage(page).finalizar_pedido()

    confirmacao = CheckoutPage(page).aguardar_confirmacao()
    assert confirmacao.pedido_confirmado()


def test_confirmacao_exibe_opcao_ver_detalhes(pagina_com_item_no_carrinho):
    """A tela de confirmação deve oferecer o link 'Ver Detalhes' do pedido."""
    page = pagina_com_item_no_carrinho
    CartPage(page).finalizar_pedido()

    confirmacao = CheckoutPage(page).aguardar_confirmacao()
    assert confirmacao.link_ver_detalhes.is_visible()
