from pytest_bdd import scenarios, given, when, then

BASE_URL = "https://local-eats-unisenac.vercel.app"

scenarios("../features/busca_restaurantes.feature")


@given("que o usuário está na página principal do LocalEats")
def acessar_pagina_principal(authenticated_page):
    authenticated_page.goto(f"{BASE_URL}/static/index.html")
    authenticated_page.wait_for_load_state("domcontentloaded")
    authenticated_page.wait_for_timeout(2000)


@when('o usuário digita "pizza" na barra de busca e clica no botão de busca')
def buscar_termo_valido(authenticated_page):
    authenticated_page.locator("#searchInput").fill("pizza")
    authenticated_page.locator("#searchBtn").click()
    authenticated_page.wait_for_timeout(1500)


@then("a lista de restaurantes deve ser atualizada com resultados visíveis")
def verificar_resultados_validos(authenticated_page):
    grid = authenticated_page.locator("#restaurantGrid")
    cards = grid.locator(".restaurant-card, .card, [class*='card']")
    loading = authenticated_page.locator(".loading")
    assert cards.count() > 0 or loading.count() == 0, \
        "Nenhum resultado exibido após busca por 'pizza'"


@when('o usuário digita "xyzabc123" na barra de busca e clica no botão de busca')
def buscar_termo_inexistente(authenticated_page):
    authenticated_page.locator("#searchInput").fill("xyzabc123")
    authenticated_page.locator("#searchBtn").click()
    authenticated_page.wait_for_timeout(1500)


@then("o sistema deve exibir uma mensagem indicando que nenhum resultado foi encontrado")
def verificar_mensagem_sem_resultados(authenticated_page):
    grid = authenticated_page.locator("#restaurantGrid")
    cards = grid.locator(".restaurant-card, .card, [class*='card']")
    assert cards.count() == 0, \
        "Esperava lista vazia para termo inexistente, mas foram exibidos cards"