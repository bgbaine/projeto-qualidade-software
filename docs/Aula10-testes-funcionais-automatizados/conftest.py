"""Configuração compartilhada do pytest-playwright."""

import os

import pytest
from playwright.sync_api import Page

_EMAIL = os.getenv("LOCALEATS_EMAIL", "bernardo@email.com")
_SENHA = os.getenv("LOCALEATS_SENHA", "123")


@pytest.fixture
def pagina_autenticada(page: Page):
    """Fixture que fornece uma página já autenticada no LocalEats."""
    from pages.login_page import LoginPage

    login = LoginPage(page)
    login.acessar()
    login.realizar_login(_EMAIL, _SENHA)
    page.wait_for_url("**/index.html**", timeout=10000)
    yield page
