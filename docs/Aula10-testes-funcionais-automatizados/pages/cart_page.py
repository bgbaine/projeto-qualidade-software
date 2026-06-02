"""Page Object do painel de carrinho na página do restaurante."""

from playwright.sync_api import Page, expect

from .base_page import BasePage


class CartPage(BasePage):
    """Painel lateral do carrinho: contagem de itens, total e finalizar pedido."""

    def __init__(self, page: Page):
        super().__init__(page)
        # #cartCountBadge: mostra "0 itens", "1 itens", etc.
        self.badge_quantidade = page.locator("#cartCountBadge")
        # #cartTotalValue: mostra "R$ 0,00", "R$ 59,17", etc.
        self.valor_total = page.locator("#cartTotalValue")
        self.botao_finalizar = page.get_by_role("button", name="Finalizar Pedido")

    # ---- Consultas -----------------------------------------------------------

    def quantidade_de_itens(self) -> int:
        texto = self.badge_quantidade.inner_text()
        try:
            return int(texto.split()[0])
        except (ValueError, IndexError):
            return 0

    def total_e_zero(self) -> bool:
        return "0,00" in self.valor_total.inner_text()

    # ---- Esperas -------------------------------------------------------------

    def aguardar_item_adicionado(self, timeout: int = 5000) -> "CartPage":
        """Bloqueia até o badge mostrar pelo menos 1 item."""
        expect(self.badge_quantidade).not_to_have_text("0 itens", timeout=timeout)
        return self

    # ---- Ações ---------------------------------------------------------------

    def finalizar_pedido(self) -> None:
        self.botao_finalizar.wait_for(state="visible", timeout=10000)
        self.botao_finalizar.click()
        self.aguardar_rede_estavel()
