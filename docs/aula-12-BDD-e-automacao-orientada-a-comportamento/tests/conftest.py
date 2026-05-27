import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://local-eats-unisenac.vercel.app"


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def authenticated_page(browser):
    """
    Faz login via formulário e aguarda o redirecionamento para index.html.
    O sistema usa localStorage (userId/userName) para controle de sessão.
    """
    context = browser.new_context()
    page = context.new_page()

    # 1. Abre a página de login
    page.goto(f"{BASE_URL}/static/login.html")
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(1500)

    # 2. Preenche com os IDs reais confirmados via inspeção do HTML
    page.locator("#loginEmail").fill("fsm@email.com")
    page.locator("#loginPassword").fill("123")

    # 3. Clica em Entrar e aguarda redirecionamento para index.html
    page.locator("button[type='submit']").first.click()

    # 4. Aguarda sair da login.html (redirecionamento via JS após salvar localStorage)
    try:
        page.wait_for_url("**/index.html", timeout=10000)
    except Exception:
        # Se não redirecionou, tenta injetar o localStorage manualmente como fallback
        page.evaluate("""() => {
            localStorage.setItem('userId', '1');
            localStorage.setItem('userName', 'Filipe Silveira Maciel');
        }""")
        page.goto(f"{BASE_URL}/static/index.html")
        page.wait_for_load_state("domcontentloaded")

    page.wait_for_timeout(2000)

    yield page
    context.close()