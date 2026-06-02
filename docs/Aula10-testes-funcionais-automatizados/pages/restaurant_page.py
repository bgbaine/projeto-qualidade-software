"""Page Object da página de detalhes de um restaurante."""

from playwright.sync_api import Page

from .base_page import BasePage, BASE_URL

RESTAURANT_URL = BASE_URL + "static/restaurant.html"


class RestaurantPage(BasePage):
    """Detalhe do restaurante: nome, cardápio, avaliações e favoritar."""

    def __init__(self, page: Page):
        super().__init__(page)
        # Nome do restaurante: primeiro <h2> da página.
        self.titulo_restaurante = page.locator("h2").first
        # Botões "Adicionar" dos itens do cardápio usam class="add-cart-btn".
        self.botoes_adicionar = page.locator("button.add-cart-btn")
        # Abas de conteúdo implementadas como <button> (sem role="tab").
        self.aba_cardapio = page.get_by_role("button", name="Cardápio")
        self.aba_avaliacoes = page.get_by_role("button", name="Avaliações")
        self.botao_favoritar = page.get_by_role("button", name="Favoritar")

    def acessar(self, id: int) -> "RestaurantPage":
        """Navega diretamente para o restaurante pelo ID."""
        self.page.goto(f"{RESTAURANT_URL}?id={id}")
        return self

    def aguardar_carregar(self) -> "RestaurantPage":
        self.titulo_restaurante.wait_for(state="visible", timeout=15000)
        self.aguardar_rede_estavel()
        return self

    def nome_do_restaurante(self) -> str:
        return self.titulo_restaurante.inner_text().strip()

    def tem_itens_no_cardapio(self) -> bool:
        return self.botoes_adicionar.count() > 0

    def adicionar_primeiro_item(self) -> "RestaurantPage":
        """Clica em 'Adicionar' do primeiro item do cardápio."""
        primeiro = self.botoes_adicionar.first
        primeiro.wait_for(state="visible", timeout=10000)
        primeiro.click()
        return self

    def abrir_aba_cardapio(self) -> "RestaurantPage":
        self.aba_cardapio.click()
        return self

    def abrir_aba_avaliacoes(self) -> "RestaurantPage":
        self.aba_avaliacoes.click()
        return self
