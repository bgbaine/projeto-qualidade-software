"""Page Object da página inicial (lista de restaurantes) do LocalEats."""

from playwright.sync_api import Page, expect

from .base_page import BasePage, BASE_URL


class HomePage(BasePage):
    """Representa a home: listagem, filtros por categoria, busca e navegação."""

    def __init__(self, page: Page):
        super().__init__(page)
        # O título é um <h2> no HTML real do site.
        self.titulo = page.get_by_role(
            "heading", name="Descubra sabores incríveis", exact=False
        )
        self.campo_busca = page.get_by_placeholder("Buscar")
        self.link_explorar = page.get_by_role("link", name="Explorar")
        self.link_favoritos = page.get_by_role("link", name="Meus Favoritos")
        self.link_pedidos = page.get_by_role("link", name="Meus Pedidos")
        # Cada restaurante é um <a class="rest-card"> gerado dinamicamente.
        self.cards_restaurantes = page.locator(".rest-card")

    # ---- Ações -----------------------------------------------------------

    def acessar(self) -> "HomePage":
        self.page.goto(BASE_URL)
        return self

    def aguardar_restaurantes_carregarem(self) -> "HomePage":
        expect(self.cards_restaurantes.first).to_be_visible(timeout=15000)
        self.aguardar_rede_estavel()
        return self

    def filtrar_por_categoria(self, categoria: str) -> "HomePage":
        self.page.get_by_role("button", name=categoria).click()
        self.aguardar_rede_estavel()
        # Aguarda o primeiro card reaparecer após o re-render do filtro.
        expect(self.cards_restaurantes.first).to_be_visible(timeout=10000)
        return self

    def buscar(self, termo: str) -> "HomePage":
        self.campo_busca.fill(termo)
        self.campo_busca.press("Enter")
        self.aguardar_rede_estavel()
        return self

    def abrir_primeiro_restaurante(self) -> str:
        """Abre o detalhe do primeiro restaurante e devolve o nome clicado."""
        primeiro = self.cards_restaurantes.first
        primeiro.wait_for(state="visible", timeout=15000)
        # O nome limpo fica no atributo alt da imagem do card.
        nome = primeiro.locator("img").get_attribute("alt") or ""
        primeiro.click()
        return nome

    # ---- Consultas -------------------------------------------------------

    def quantidade_de_restaurantes(self) -> int:
        return self.cards_restaurantes.count()
