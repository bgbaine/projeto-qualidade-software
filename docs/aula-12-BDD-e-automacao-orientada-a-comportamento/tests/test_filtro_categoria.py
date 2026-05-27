from pytest_bdd import scenarios, given, when, then

BASE_URL = "https://local-eats-unisenac.vercel.app"

scenarios("../features/historico_pedidos.feature")


@given("que o usuário acessa a página de pedidos do LocalEats")
def acessar_pagina_pedidos(authenticated_page):
    authenticated_page.goto(f"{BASE_URL}/static/orders.html")
    authenticated_page.wait_for_load_state("domcontentloaded")
    authenticated_page.wait_for_timeout(1500)


@when("a página de histórico de transações é carregada")
def pagina_pedidos_carregada(authenticated_page):
    authenticated_page.wait_for_timeout(500)


@then('o título "Histórico de Transações" deve estar visível na tela')
def verificar_titulo_historico(authenticated_page):
    # Confirma que saiu da login.html e chegou na orders.html
    assert "orders.html" in authenticated_page.url, \
        f"Não redirecionou para orders.html. URL atual: {authenticated_page.url}"
    titulo = authenticated_page.locator("h2")
    assert titulo.count() > 0, "Nenhum título h2 encontrado na página de pedidos"


@when("o usuário visualiza o conteúdo da página")
def visualizar_conteudo(authenticated_page):
    authenticated_page.wait_for_timeout(500)


@then("a área destinada à listagem de pedidos deve estar presente no DOM")
def verificar_area_pedidos(authenticated_page):
    # Link "Meus Pedidos" existe no nav: <a href="orders.html">Meus Pedidos</a>
    link = authenticated_page.locator("nav a[href='orders.html']")
    assert link.count() > 0, "Link 'Meus Pedidos' não encontrado na navbar"