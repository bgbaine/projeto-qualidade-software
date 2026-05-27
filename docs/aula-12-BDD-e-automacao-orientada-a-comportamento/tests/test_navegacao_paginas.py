from pytest_bdd import scenarios, given, when, then

BASE_URL = "https://local-eats-unisenac.vercel.app"

scenarios("../features/navegacao_paginas.feature")


@given("que o usuário acessa o sistema LocalEats")
def acessar_sistema(authenticated_page):
    authenticated_page.goto(f"{BASE_URL}/static/index.html")
    authenticated_page.wait_for_load_state("networkidle")


@given("que o usuário está na página principal do LocalEats")
def acessar_pagina_principal(authenticated_page):
    authenticated_page.goto(f"{BASE_URL}/static/index.html")
    authenticated_page.wait_for_load_state("networkidle")


@when("a página principal é carregada")
def pagina_carregada(authenticated_page):
    authenticated_page.wait_for_load_state("domcontentloaded")


@then("os cards de restaurantes devem estar visíveis na tela")
def verificar_cards_visiveis(authenticated_page):
    # O sistema exibe "Carregando os melhores restaurantes..." antes de carregar
    authenticated_page.wait_for_timeout(2000)
    cards = authenticated_page.locator(".restaurant-card")
    assert cards.count() > 0, "Nenhum card de restaurante encontrado na página principal"


@when('o usuário clica no link de navegação "Favoritos"')
def clicar_favoritos(authenticated_page):
    # Link real: "Meus Favoritos" → /static/profile.html
    authenticated_page.get_by_role("link", name="Meus Favoritos").click()
    authenticated_page.wait_for_load_state("networkidle")


@then("o sistema deve exibir a página de favoritos sem erros")
def verificar_pagina_favoritos(authenticated_page):
    assert "profile.html" in authenticated_page.url, \
        f"URL esperada contém 'profile.html', mas foi: {authenticated_page.url}"
    assert authenticated_page.get_by_role("heading", name="Restaurantes Favoritos").is_visible(), \
        "Título 'Restaurantes Favoritos' não encontrado na página"
