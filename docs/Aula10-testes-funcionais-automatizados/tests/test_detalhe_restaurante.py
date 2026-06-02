"""Testes funcionais (E2E) do fluxo de visualização de detalhes de um restaurante.

Fluxo escolhido: Visualização de detalhes de um restaurante (Fluxo 3).
Cobre: nome visível, cardápio com itens e navegação para a aba de avaliações.
"""

from playwright.sync_api import expect

from pages.restaurant_page import RestaurantPage

RESTAURANTE_ID = 1


def test_detalhe_exibe_nome_do_restaurante(pagina_autenticada):
    """A página de detalhe deve exibir o nome do restaurante como título."""
    detalhe = RestaurantPage(pagina_autenticada).acessar(RESTAURANTE_ID).aguardar_carregar()
    assert detalhe.nome_do_restaurante() != ""


def test_detalhe_exibe_cardapio_com_itens(pagina_autenticada):
    """O cardápio deve conter ao menos um item com botão 'Adicionar'."""
    detalhe = RestaurantPage(pagina_autenticada).acessar(RESTAURANTE_ID).aguardar_carregar()
    assert detalhe.tem_itens_no_cardapio()


def test_detalhe_permite_navegar_para_aba_avaliacoes(pagina_autenticada):
    """Clicar na aba 'Avaliações' deve torná-la visível/ativa."""
    detalhe = RestaurantPage(pagina_autenticada).acessar(RESTAURANTE_ID).aguardar_carregar()
    detalhe.abrir_aba_avaliacoes()
    expect(detalhe.aba_avaliacoes).to_be_visible()
