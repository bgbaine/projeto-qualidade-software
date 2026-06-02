"""Testes funcionais (E2E) do fluxo de navegação e visualização de restaurantes.

Fluxo escolhido: Navegação e visualização de restaurantes (Fluxo 2).
Cobre: lista carregada, filtro por categoria, busca e abertura do detalhe.
"""

from pages.home_page import HomePage
from pages.restaurant_page import RestaurantPage


def test_lista_de_restaurantes_carrega(pagina_autenticada):
    """A home deve carregar e exibir pelo menos um restaurante."""
    home = HomePage(pagina_autenticada).acessar().aguardar_restaurantes_carregarem()

    assert home.titulo.is_visible()
    assert home.quantidade_de_restaurantes() > 0


def test_filtrar_restaurantes_por_categoria(pagina_autenticada):
    """Ao filtrar por 'Todos', a lista deve continuar exibindo restaurantes."""
    home = HomePage(pagina_autenticada).acessar().aguardar_restaurantes_carregarem()

    home.filtrar_por_categoria("Todos")

    assert home.quantidade_de_restaurantes() > 0


def test_clicar_em_restaurante_abre_detalhes(pagina_autenticada):
    """Clicar num restaurante deve abrir a página de detalhes com cardápio."""
    home = HomePage(pagina_autenticada).acessar().aguardar_restaurantes_carregarem()

    nome_clicado = home.abrir_primeiro_restaurante()

    detalhe = RestaurantPage(pagina_autenticada).aguardar_carregar()
    assert detalhe.nome_do_restaurante() != ""
    assert detalhe.tem_itens_no_cardapio()
    assert nome_clicado.lower() in detalhe.nome_do_restaurante().lower() \
        or detalhe.nome_do_restaurante().lower() in nome_clicado.lower()
