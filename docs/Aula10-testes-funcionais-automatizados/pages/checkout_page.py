"""Page Object do estado de confirmação de pedido no LocalEats."""

from playwright.sync_api import Page

from .base_page import BasePage


class CheckoutPage(BasePage):
    """Representa a tela de confirmação exibida após 'Finalizar Pedido'."""

    def __init__(self, page: Page):
        super().__init__(page)
        # <h2>Pedido Realizado!</h2> aparece após o checkout.
        self.titulo_sucesso = page.get_by_role("heading", name="Pedido Realizado!")
        self.mensagem_sucesso = page.get_by_text(
            "Seu pedido de teste foi enviado com sucesso"
        )
        # "Ver Detalhes" é um <button>, não um link.
        self.link_ver_detalhes = page.get_by_role("button", name="Ver Detalhes")

    def aguardar_confirmacao(self, timeout: int = 10000) -> "CheckoutPage":
        self.titulo_sucesso.wait_for(state="visible", timeout=timeout)
        return self

    def pedido_confirmado(self) -> bool:
        return self.titulo_sucesso.is_visible()
