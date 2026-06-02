"""Page Object da página de login do LocalEats."""

from playwright.sync_api import Page, expect

from .base_page import BasePage, BASE_URL


class LoginPage(BasePage):
    """Tela de login: campos E-mail / Senha e botão Entrar."""

    def __init__(self, page: Page):
        super().__init__(page)
        # O <label> não tem atributo "for", então get_by_label falha.
        # Usamos os IDs definidos no HTML: #loginEmail e #loginPassword.
        self.campo_email = page.locator("#loginEmail")
        self.campo_senha = page.locator("#loginPassword")
        # Há dois botões "Entrar" na página (aba + submit). Usamos o submit do form.
        self.botao_entrar = page.locator("#loginForm button[type='submit']")
        self.mensagem_erro = page.get_by_text("Erro ocorreu")

    def acessar(self) -> "LoginPage":
        """Navega para o site — o redirect automático leva ao login.html."""
        self.page.goto(BASE_URL)
        self.aguardar_rede_estavel()
        return self

    def realizar_login(self, email: str, senha: str) -> "LoginPage":
        self.campo_email.fill(email)
        self.campo_senha.fill(senha)
        self.botao_entrar.click()
        self.aguardar_rede_estavel()
        return self

    def login_com_sucesso(self) -> bool:
        """Retorna True se saiu da tela de login após submeter."""
        return "login" not in self.page.url
