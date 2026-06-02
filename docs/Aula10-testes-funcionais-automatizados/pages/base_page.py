"""Classe base do Page Object Model.

Concentra comportamento comum a todas as páginas (URL base, navegação e
espera por estabilização de rede), evitando repetição nas páginas filhas.
"""

from playwright.sync_api import Page

BASE_URL = "https://local-eats-unisenac.vercel.app/"


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def aguardar_rede_estavel(self, timeout: int = 15000) -> None:
        """Espera as requisições assíncronas (fetch dos restaurantes) terminarem."""
        self.page.wait_for_load_state("networkidle", timeout=timeout)
