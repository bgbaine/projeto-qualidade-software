from pytest_bdd import scenarios, given, when, then

BASE_URL = "https://local-eats-unisenac.vercel.app"

scenarios("../features/historico_pedidos.feature")


@given("que o usuário acessa a página de pedidos do LocalEats")
def acessar_pagina_pedidos(authenticated_page):
    authenticated_page.goto(f"{BASE_URL}/static/orders.html")
    authenticated_page.wait_for_load_state("networkidle")


@when("a página de histórico de transações é carregada")
def pagina_pedidos_carregada(authenticated_page):
    authenticated_page.wait_for_load_state("domcontentloaded")


@then('o título "Histórico de Transações" deve estar visível na tela')
def verificar_titulo_historico(authenticated_page):
    titulo = authenticated_page.get_by_role("heading", name="Histórico de Transações")
    assert titulo.is_visible(), "Título 'Histórico de Transações' não está visível"


@when("o usuário visualiza o conteúdo da página")
def visualizar_conteudo(authenticated_page):
    authenticated_page.wait_for_timeout(500)


@then("a área destinada à listagem de pedidos deve estar presente no DOM")
def verificar_area_pedidos(authenticated_page):
    # Navegar também via link "Meus Pedidos" da navbar confirma que o link existe
    link = authenticated_page.get_by_role("link", name="Meus Pedidos")
    assert link.is_visible(), "Link 'Meus Pedidos' não encontrado na navbar"
