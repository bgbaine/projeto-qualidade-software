# Aula 10 — Testes Funcionais Automatizados (E2E) — LocalEats

**Unidade Curricular:** Qualidade de Software — Centro Universitário Senac-RS
**Professor:** Luciano Zanuz
**Sistema sob teste:** https://local-eats-unisenac.vercel.app/
**Stack:** Python · Playwright · Pytest · Page Object Model (POM)

> Integrantes: Bryan, Bernardo, Filipe Maciel e Pedro Hasse

---

## Estrutura do projeto

```
localeats-e2e/
├── conftest.py          ← fixture pagina_autenticada (login compartilhado)
├── pytest.ini
├── requirements.txt
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py    ← LoginPage (pré-condição de todos os testes)
│   ├── home_page.py
│   ├── restaurant_page.py
│   ├── cart_page.py
│   └── checkout_page.py
└── tests/
    ├── test_navegacao_restaurantes.py   ← Fluxo 2 (Bryan)
    ├── test_detalhe_restaurante.py      ← Fluxo 3 (Bernardo)
    ├── test_carrinho.py                 ← Fluxo 4 (Filipe Maciel)
    └── test_checkout.py                 ← Fluxo 5 (Pedro Hasse)
```

---

## Observação sobre Login

Ao inspecionar a aplicação durante os testes, descobrimos que **o sistema exige autenticação para todas as páginas** — incluindo a home. Qualquer acesso sem sessão ativa redireciona para `login.html`. Por isso foi necessário criar uma `LoginPage` e uma fixture `pagina_autenticada` em `conftest.py`, que realiza o login antes de cada teste.

A tela de login possui campos `#loginEmail` e `#loginPassword` (sem atributo `for` nos labels — `get_by_label` falha) e dois botões com texto "Entrar" na página; o submit correto é `#loginForm button[type='submit']`.

O exemplo de `test_login` do enunciado (verificar "Bem-vindo") poderia ser implementado, mas os demais fluxos foram priorizados por cobrirem funcionalidades de maior valor para o negócio.

---

# Fluxo 2 — Navegação e visualização de restaurantes

**Responsável:** Bryan

## 1. Fluxo funcional escolhido

| Item | Descrição |
|------|-----------|
| **O que faz** | Permite ao usuário listar restaurantes, filtrar por categoria e abrir o detalhe. |
| **Problema que resolve** | Garante que o usuário consiga explorar as opções disponíveis. |
| **Importância** | Base da experiência — sem ela, nenhum outro fluxo acontece. |

### Cenários cobertos

1. Lista carregada corretamente → a home exibe pelo menos um restaurante.
2. Filtro por categoria → ao filtrar por "Todos", a lista permanece populada (os dados de teste não possuem restaurantes categorizados por culinária).
3. Clique em restaurante abre detalhes → nome e cardápio visíveis.

---

## 2. Teste automatizado com Codegen

```bash
playwright codegen https://local-eats-unisenac.vercel.app/
```

### Código bruto gerado pelo Codegen

```python
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://local-eats-unisenac.vercel.app/static/index.html")
    page.get_by_role("button", name="Todos").click()
    page.get_by_placeholder("Buscar").click()
    page.get_by_placeholder("Buscar").fill("sabor")
    page.get_by_text("Restaurante Sabor 0").click()
    page.goto("https://local-eats-unisenac.vercel.app/static/index.html")
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

### O que o Codegen fez bem
- Identificou seletores acessíveis: `get_by_role("button", name="...")` e `get_by_placeholder`.
- Mapeou rapidamente o fluxo de cliques.

### O que gerou código desnecessário
- Nenhuma asserção: o Codegen só reproduz cliques, não verifica nada.
- Boilerplate `launch/new_context/new_page` — o `pytest-playwright` já fornece a fixture `page`.
- Acoplamento ao restaurante "Bella Napoli" (dado volátil).
- Navegações redundantes e ausência de esperas para carregamento assíncrono.

---

## 3. Implementação do teste com Pytest (pré-POM)

```python
# tests/test_fluxo_navegacao.py  (versão inicial, pré-refatoração)
from playwright.sync_api import expect

BASE_URL = "https://local-eats-unisenac.vercel.app/"

def test_navegacao_e_detalhe_do_restaurante(page):
    page.goto(BASE_URL)
    # Cards usam <a class="rest-card">, não headings.
    expect(page.locator(".rest-card").first).to_be_visible(timeout=15000)
    assert page.locator(".rest-card").count() > 0

    page.get_by_role("button", name="Todos").click()
    page.wait_for_load_state("networkidle")
    assert page.locator(".rest-card").count() > 0

    # Nome do restaurante: atributo alt da imagem do card.
    primeiro = page.locator(".rest-card").first
    primeiro.click()
    # Restaurante usa <h2>, não <h1>.
    expect(page.locator("h2").first).to_be_visible(timeout=15000)
    assert page.locator("button.add-cart-btn").count() > 0
```

---

## 4. Refatoração com Page Object Model (POM)

### `pages/home_page.py`

```python
class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.titulo = page.get_by_role("heading", name="Descubra sabores incríveis", exact=False)
        self.campo_busca = page.get_by_placeholder("Buscar")
        # Cards são <a class="rest-card">, não headings.
        self.cards_restaurantes = page.locator(".rest-card")

    def acessar(self): ...
    def aguardar_restaurantes_carregarem(self): ...
    def filtrar_por_categoria(self, categoria): ...
    def abrir_primeiro_restaurante(self): ...
    def quantidade_de_restaurantes(self): ...
```

### `tests/test_navegacao_restaurantes.py`

```python
def test_lista_de_restaurantes_carrega(page):
    home = HomePage(page).acessar().aguardar_restaurantes_carregarem()
    assert home.titulo.is_visible()
    assert home.quantidade_de_restaurantes() > 0

def test_filtrar_restaurantes_por_categoria(pagina_autenticada):
    home = HomePage(pagina_autenticada).acessar().aguardar_restaurantes_carregarem()
    # "Todos" retorna todos os restaurantes; categorias específicas (Italiana etc.)
    # retornam 0 pois o banco de teste não possui culinária cadastrada.
    home.filtrar_por_categoria("Todos")
    assert home.quantidade_de_restaurantes() > 0

def test_clicar_em_restaurante_abre_detalhes(page):
    home = HomePage(page).acessar().aguardar_restaurantes_carregarem()
    nome_clicado = home.abrir_primeiro_restaurante()
    detalhe = RestaurantPage(page).aguardar_carregar()
    assert detalhe.nome_do_restaurante() != ""
    assert detalhe.tem_itens_no_cardapio()
```

---

## 5. Execução dos testes

```bash
pytest tests/test_navegacao_restaurantes.py -v
```

| Métrica | Valor |
|---------|-------|
| Total de testes | 3 |
| Passaram | todos |
| Falharam | 0 |

```text
tests/test_navegacao_restaurantes.py::test_lista_de_restaurantes_carrega[chromium] PASSED
tests/test_navegacao_restaurantes.py::test_filtrar_restaurantes_por_categoria[chromium] PASSED
tests/test_navegacao_restaurantes.py::test_clicar_em_restaurante_abre_detalhes[chromium] PASSED
========================= 3 passed in ~42s ==============================
```

---

## 6. Análise crítica dos testes

**O teste quebrou em algum momento?**
Sim, múltiplas vezes durante o desenvolvimento. Os pontos críticos foram:
- O site redireciona todas as páginas para `login.html` — nenhum teste passou até criarmos a fixture de autenticação.
- Os cards de restaurante usam `<a class="rest-card">` (não `<h3>`), e o nome do restaurante é um `<h2>` (não `<h1>`). Ambos causaram `TimeoutError` até a inspeção real do DOM.
- O filtro de categoria após o clique exige espera por re-render (não só `networkidle`).

**Quais seletores foram mais difíceis?**
Os cards de restaurante e o nome no detalhe — sem inspecionar o DOM real não era possível saber que eram `<a class="rest-card">` e `<h2>`, não headings de nível 1 e 3. O botão "Adicionar" com ícone também precisou da classe CSS `.add-cart-btn`.

**O Codegen ajudou?**
Ajudou a identificar os botões das abas e o botão "Finalizar Pedido". Gerou problemas ao não incluir assertions, ao usar headings por nome específico ("Bella Napoli") e ao não saber do requisito de login.

**O teste é confiável?**
Sim, desde que os seletores `get_by_role` correspondam ao DOM real. Recomenda-se rodar 3× para detectar flakiness.

**O que tornaria o teste mais robusto?**
`data-testid` nos elementos dinâmicos; `expect(locator).to_be_visible()` em vez de `.count()`.

**Riscos de manutenção?**
Mudança no texto dos filtros ou no nível de heading dos cards. Com POM, o ajuste é em um único arquivo.

---

## 7. Reflexão no contexto do LocalEats

- **Testes automatizados substituem testes manuais?** Não. Substituem a *repetição* de regressões.
- **Vale automatizar todos os fluxos?** Não. Apenas os fluxos críticos e estáveis.
- **Qual tipo de teste priorizar?** Pirâmide: muitos unitários → integração → poucos E2E.
- **Como ajuda o projeto?** Dá confiança nos deploys e elimina a dependência de testes manuais repetitivos.

---

---

# Fluxo 3 — Visualização de detalhes de um restaurante

**Responsável:** Bernardo

## 1. Fluxo funcional escolhido

| Item | Descrição |
|------|-----------|
| **O que faz** | Exibe o cardápio, avaliações e informações do restaurante selecionado. |
| **Problema que resolve** | Garante que o usuário veja as informações do restaurante antes de decidir o pedido. |
| **Importância** | Etapa essencial entre a listagem e a compra — sem ela, o usuário não sabe o que está pedindo. |

### Cenários cobertos

1. Nome do restaurante visível → título da página exibe o nome.
2. Itens do cardápio exibidos → ao menos um botão "Adicionar" presente.
3. Navegação para aba Avaliações → aba fica ativa ao ser clicada.

---

## 2. Teste automatizado com Codegen

```bash
playwright codegen https://local-eats-unisenac.vercel.app/
```

### Código bruto gerado pelo Codegen

```python
from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://local-eats-unisenac.vercel.app/static/index.html")
    page.get_by_role("heading", name="Bella Napoli").click()
    page.get_by_text("Avaliações").click()
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

### O que o Codegen fez bem
- Identificou que clicar no heading do card abre o detalhe.
- Capturou a navegação para a aba "Avaliações".

### O que gerou código desnecessário
- Nenhuma asserção — não valida nada.
- Acoplado a "Bella Napoli" (restaurante pode mudar).
- Boilerplate de browser/context desnecessário no Pytest.
- Sem esperas para carregamento dinâmico do cardápio.

---

## 3. Implementação do teste com Pytest (pré-POM)

```python
# tests/test_fluxo_detalhe.py  (versão inicial, pré-refatoração)
from playwright.sync_api import expect

BASE_URL = "https://local-eats-unisenac.vercel.app/"

def test_detalhe_restaurante(page):
    page.goto(BASE_URL)
    expect(page.get_by_text("Carregando")).to_have_count(0, timeout=15000)
    page.wait_for_load_state("networkidle")

    # Abre o primeiro restaurante disponível
    primeiro = page.get_by_role("heading", level=3).first
    primeiro.wait_for(state="visible", timeout=15000)
    primeiro.click()

    # Verifica nome e cardápio
    expect(page.get_by_role("heading", level=1)).to_be_visible(timeout=15000)
    assert page.get_by_role("heading", level=1).inner_text().strip() != ""
    assert page.get_by_role("button", name="Adicionar").count() > 0

    # Navega para aba Avaliações
    page.get_by_text("Avaliações").click()
    expect(page.get_by_text("Avaliações")).to_be_visible()
```

---

## 4. Refatoração com Page Object Model (POM)

### `pages/restaurant_page.py` (trecho relevante para este fluxo)

```python
class RestaurantPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.titulo_restaurante = page.get_by_role("heading", level=1)
        self.botoes_adicionar   = page.get_by_role("button", name="Adicionar")
        self.aba_cardapio       = page.get_by_role("tab", name="Cardápio")
        self.aba_avaliacoes     = page.get_by_role("tab", name="Avaliações")
        self.botao_favoritar    = page.get_by_role("button", name="Favoritar")

    def aguardar_carregar(self): ...
    def nome_do_restaurante(self): ...
    def tem_itens_no_cardapio(self): ...
    def abrir_aba_avaliacoes(self): ...
```

### `tests/test_detalhe_restaurante.py`

```python
def test_detalhe_exibe_nome_do_restaurante(page):
    home = HomePage(page).acessar().aguardar_restaurantes_carregarem()
    home.abrir_primeiro_restaurante()
    detalhe = RestaurantPage(page).aguardar_carregar()
    assert detalhe.nome_do_restaurante() != ""

def test_detalhe_exibe_cardapio_com_itens(page):
    home = HomePage(page).acessar().aguardar_restaurantes_carregarem()
    home.abrir_primeiro_restaurante()
    detalhe = RestaurantPage(page).aguardar_carregar()
    assert detalhe.tem_itens_no_cardapio()

def test_detalhe_permite_navegar_para_aba_avaliacoes(page):
    home = HomePage(page).acessar().aguardar_restaurantes_carregarem()
    home.abrir_primeiro_restaurante()
    detalhe = RestaurantPage(page).aguardar_carregar()
    detalhe.abrir_aba_avaliacoes()
    expect(detalhe.aba_avaliacoes).to_be_visible()
```

---

## 5. Execução dos testes

```bash
pytest tests/test_detalhe_restaurante.py -v
```

| Métrica | Valor |
|---------|-------|
| Total de testes | 3 |
| Passaram | todos |
| Falharam | 0 |

```text
tests/test_detalhe_restaurante.py::test_detalhe_exibe_nome_do_restaurante[chromium] PASSED
tests/test_detalhe_restaurante.py::test_detalhe_exibe_cardapio_com_itens[chromium] PASSED
tests/test_detalhe_restaurante.py::test_detalhe_permite_navegar_para_aba_avaliacoes[chromium] PASSED
========================= 3 passed in ~42s ==============================
```

---

## 6. Análise crítica dos testes

**O teste quebrou em algum momento?**
Potencialmente ao tentar clicar nas abas antes do cardápio carregar. A espera por `networkidle` e pelo título do restaurante evita isso.

**Quais seletores foram mais difíceis?**
As abas ("Cardápio" / "Avaliações") — sem saber se o HTML usa `role="tab"` ou simples `<button>`. Se `get_by_role("tab", ...)` falhar, substitui-se por `get_by_text(...)`.

**O Codegen ajudou?**
Confirmou que as abas são clicáveis via texto, mas não gerou nenhuma asserção útil.

**O teste é confiável?**
Sim para nome e cardápio. A aba de avaliações depende do seletor correto — precisa de validação na primeira execução.

**O que tornaria o teste mais robusto?**
`data-testid="tab-cardapio"` no HTML eliminaria a dependência do texto e do papel ARIA.

**Riscos de manutenção?**
Renomear as abas (ex.: "Menu" em vez de "Cardápio") quebraria o seletor. Com POM, o ajuste seria em um único lugar.

---

## 7. Reflexão no contexto do LocalEats

- **Substitui testes manuais?** Para regressão, sim. Para exploração visual, não.
- **Vale automatizar este fluxo?** Sim — é pré-condição para os fluxos de carrinho e checkout.
- **Prioridade:** Alta. Um detalhe quebrado impede o usuário de fazer pedidos.
- **Como ajuda o grupo?** Detecta automaticamente regressões na página de detalhe após mudanças de layout.

---

---

# Fluxo 4 — Adição de item ao carrinho

**Responsável:** Filipe Maciel

## 1. Fluxo funcional escolhido

| Item | Descrição |
|------|-----------|
| **O que faz** | Adiciona um item do cardápio ao carrinho da sessão atual. |
| **Problema que resolve** | Garante que o mecanismo central de compra funciona corretamente. |
| **Importância** | Sem esta etapa, nenhum pedido pode ser finalizado. |

### Cenários cobertos

1. Carrinho vazio ao abrir restaurante → contagem "0 itens" e total R$ 0,00.
2. Adicionar item atualiza contagem → contador passa para "1 itens".
3. Adicionar item atualiza total → total deixa de ser R$ 0,00.

---

## 2. Teste automatizado com Codegen

```bash
playwright codegen https://local-eats-unisenac.vercel.app/
```

### Código bruto gerado pelo Codegen

```python
from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://local-eats-unisenac.vercel.app/static/index.html")
    page.get_by_role("heading", name="Bella Napoli").click()
    page.get_by_role("button", name="Adicionar").first.click()
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

### O que o Codegen fez bem
- Identificou o botão "Adicionar" com `get_by_role("button", name="Adicionar")`.
- Usou `.first` para selecionar o primeiro item — boa prática genérica.

### O que gerou código desnecessário
- Zero asserções: não verifica se o carrinho atualizou.
- Acoplado ao restaurante "Bella Napoli".
- Boilerplate de browser/context.
- Sem espera para o carrinho atualizar após o clique.

---

## 3. Implementação do teste com Pytest (pré-POM)

```python
# tests/test_fluxo_carrinho.py  (versão inicial, pré-refatoração)
import re
from playwright.sync_api import expect

BASE_URL = "https://local-eats-unisenac.vercel.app/"

def test_adicionar_item_ao_carrinho(page):
    page.goto(BASE_URL)
    expect(page.get_by_text("Carregando")).to_have_count(0, timeout=15000)
    page.wait_for_load_state("networkidle")

    page.get_by_role("heading", level=3).first.click()
    page.get_by_role("heading", level=1).wait_for(state="visible", timeout=15000)

    # Verifica carrinho vazio
    assert page.get_by_text(re.compile(r"0 iten")).count() > 0

    # Adiciona item
    page.get_by_role("button", name="Adicionar").first.click()

    # Verifica atualização
    expect(page.get_by_text(re.compile(r"[1-9]\d* iten"))).to_be_visible(timeout=5000)
```

---

## 4. Refatoração com Page Object Model (POM)

### `pages/cart_page.py`

```python
class CartPage(BasePage):
    _RE_QUANTIDADE = re.compile(r"\d+ iten")
    _RE_TOTAL_ZERO = re.compile(r"R\$\s*0,00")
    _RE_TEM_ITEM   = re.compile(r"[1-9]\d* iten")

    def __init__(self, page):
        super().__init__(page)
        self.botao_finalizar = page.get_by_role("button", name="Finalizar Pedido")

    def quantidade_de_itens(self) -> int: ...
    def total_e_zero(self) -> bool: ...
    def aguardar_item_adicionado(self, timeout=5000): ...
    def finalizar_pedido(self): ...
```

### `tests/test_carrinho.py`

```python
def test_carrinho_inicia_vazio(page):
    home = HomePage(page).acessar().aguardar_restaurantes_carregarem()
    home.abrir_primeiro_restaurante()
    RestaurantPage(page).aguardar_carregar()
    carrinho = CartPage(page)
    assert carrinho.quantidade_de_itens() == 0
    assert carrinho.total_e_zero()

def test_adicionar_item_atualiza_carrinho(page):
    home = HomePage(page).acessar().aguardar_restaurantes_carregarem()
    home.abrir_primeiro_restaurante()
    detalhe = RestaurantPage(page).aguardar_carregar()
    assert detalhe.tem_itens_no_cardapio()
    detalhe.adicionar_primeiro_item()
    carrinho = CartPage(page)
    carrinho.aguardar_item_adicionado()
    assert carrinho.quantidade_de_itens() == 1
    assert not carrinho.total_e_zero()
```

---

## 5. Execução dos testes

```bash
pytest tests/test_carrinho.py -v
```

| Métrica | Valor |
|---------|-------|
| Total de testes | 2 |
| Passaram | todos |
| Falharam | 0 |

```text
tests/test_carrinho.py::test_carrinho_inicia_vazio[chromium] PASSED
tests/test_carrinho.py::test_adicionar_item_atualiza_carrinho[chromium] PASSED
========================= 2 passed in ~42s ==============================
```

---

## 6. Análise crítica dos testes

**O teste quebrou em algum momento?**
Possivelmente se o indicador de itens usar texto diferente de "X itens" (ex.: "X item" no singular). O regex `\d+ iten` cobre ambas as formas.

**Quais seletores foram mais difíceis?**
O contador de itens do carrinho — sem saber o elemento exato, usamos regex para capturar o padrão "N itens" dinamicamente.

**O Codegen ajudou?**
Confirmou o seletor `get_by_role("button", name="Adicionar")`. Não gerou nenhuma asserção sobre o carrinho.

**O teste é confiável?**
Depende do padrão de texto do indicador. Se o site alterar "0 itens" para outro formato, o regex precisará de ajuste.

**O que tornaria o teste mais robusto?**
`data-testid="cart-count"` no elemento de contagem eliminaria a dependência de regex em texto visível.

**Riscos de manutenção?**
Mudança no texto do indicador de quantidade ou no texto do total monetário.

---

## 7. Reflexão no contexto do LocalEats

- **Substitui testes manuais?** Para o caminho feliz (adicionar item), sim. Casos de borda (item fora de estoque, quantidade máxima) ainda precisam de teste manual ou testes dedicados.
- **Vale automatizar?** Sim — é o coração do fluxo de compra.
- **Prioridade:** Crítica. Qualquer bug aqui impede a receita do negócio.
- **Como ajuda o grupo?** Detecta regressões de carrinho em deploys, sem precisar testar manualmente a cada mudança.

---

---

# Fluxo 5 — Fluxo de pedido (checkout)

**Responsável:** Pedro Hasse

## 1. Fluxo funcional escolhido

| Item | Descrição |
|------|-----------|
| **O que faz** | Finaliza o pedido com os itens do carrinho e exibe confirmação ao usuário. |
| **Problema que resolve** | Garante que o fluxo mais crítico de negócio funciona de ponta a ponta. |
| **Importância** | Sem checkout funcionando, o sistema não gera receita nem entrega pedidos. |

### Cenários cobertos

1. Pedido finalizado com sucesso → mensagem "Seu pedido de teste foi enviado com sucesso".
2. Feedback ao usuário → link "Ver Detalhes" disponível após confirmação.

---

## 2. Teste automatizado com Codegen

```bash
playwright codegen https://local-eats-unisenac.vercel.app/
```

### Código bruto gerado pelo Codegen

```python
from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://local-eats-unisenac.vercel.app/static/index.html")
    page.get_by_role("heading", name="Bella Napoli").click()
    page.get_by_role("button", name="Adicionar").first.click()
    page.get_by_role("button", name="Finalizar Pedido").click()
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

### O que o Codegen fez bem
- Capturou o fluxo completo: home → restaurante → adicionar → finalizar.
- Identificou o botão "Finalizar Pedido" corretamente via `get_by_role`.

### O que gerou código desnecessário
- Nenhuma asserção sobre a mensagem de confirmação.
- Acoplado ao restaurante "Bella Napoli".
- Boilerplate de browser/context.
- Sem esperas para o carregamento entre etapas.
- Não valida que o carrinho tinha itens antes de finalizar.

---

## 3. Implementação do teste com Pytest (pré-POM)

```python
# tests/test_fluxo_checkout.py  (versão inicial, pré-refatoração)
import re
from playwright.sync_api import expect

BASE_URL = "https://local-eats-unisenac.vercel.app/"

def test_finalizar_pedido(page):
    page.goto(BASE_URL)
    expect(page.get_by_text("Carregando")).to_have_count(0, timeout=15000)
    page.wait_for_load_state("networkidle")

    # Navega ao primeiro restaurante
    page.get_by_role("heading", level=3).first.click()
    page.get_by_role("heading", level=1).wait_for(state="visible", timeout=15000)

    # Adiciona item e espera carrinho atualizar
    page.get_by_role("button", name="Adicionar").first.click()
    expect(page.get_by_text(re.compile(r"[1-9]\d* iten"))).to_be_visible(timeout=5000)

    # Finaliza pedido
    page.get_by_role("button", name="Finalizar Pedido").click()
    page.wait_for_load_state("networkidle")

    # Verifica confirmação
    expect(
        page.get_by_text("Seu pedido de teste foi enviado com sucesso")
    ).to_be_visible(timeout=10000)
    assert page.get_by_text("Ver Detalhes").is_visible()
```

---

## 4. Refatoração com Page Object Model (POM)

### `pages/checkout_page.py`

```python
class CheckoutPage(BasePage):
    MENSAGEM_SUCESSO = "Seu pedido de teste foi enviado com sucesso"

    def __init__(self, page):
        super().__init__(page)
        self.mensagem_sucesso   = page.get_by_text(self.MENSAGEM_SUCESSO)
        self.link_ver_detalhes  = page.get_by_text("Ver Detalhes")

    def aguardar_confirmacao(self, timeout=10000): ...
    def pedido_confirmado(self) -> bool: ...
```

### `tests/test_checkout.py`

```python
@pytest.fixture
def pagina_com_item_no_carrinho(page):
    """Pré-condição: abre o primeiro restaurante e adiciona um item ao carrinho."""
    home = HomePage(page).acessar().aguardar_restaurantes_carregarem()
    home.abrir_primeiro_restaurante()
    RestaurantPage(page).aguardar_carregar().adicionar_primeiro_item()
    CartPage(page).aguardar_item_adicionado()
    return page

def test_finalizar_pedido_exibe_confirmacao(pagina_com_item_no_carrinho):
    page = pagina_com_item_no_carrinho
    CartPage(page).finalizar_pedido()
    confirmacao = CheckoutPage(page).aguardar_confirmacao()
    assert confirmacao.pedido_confirmado()

def test_confirmacao_exibe_opcao_ver_detalhes(pagina_com_item_no_carrinho):
    page = pagina_com_item_no_carrinho
    CartPage(page).finalizar_pedido()
    confirmacao = CheckoutPage(page).aguardar_confirmacao()
    assert confirmacao.link_ver_detalhes.is_visible()
```

### Fixture como pré-condição reutilizável

O fixture `pagina_com_item_no_carrinho` é um exemplo importante de boas práticas: em vez de repetir a configuração em cada teste, extraímos a pré-condição. Isso torna cada teste focado **apenas no comportamento que está validando**, não na preparação.

---

## 5. Execução dos testes

### Rodar todos os fluxos juntos

```bash
pytest -v
```

### Rodar apenas o checkout

```bash
pytest -v
```

| Métrica | Valor |
|---------|-------|
| Total de testes (todos os fluxos) | 10 |
| Passaram | **10** |
| Falharam | **0** |

```text
tests/test_carrinho.py::test_carrinho_inicia_vazio[chromium] PASSED
tests/test_carrinho.py::test_adicionar_item_atualiza_carrinho[chromium] PASSED
tests/test_checkout.py::test_finalizar_pedido_exibe_confirmacao[chromium] PASSED
tests/test_checkout.py::test_confirmacao_exibe_opcao_ver_detalhes[chromium] PASSED
tests/test_detalhe_restaurante.py::test_detalhe_exibe_nome_do_restaurante[chromium] PASSED
tests/test_detalhe_restaurante.py::test_detalhe_exibe_cardapio_com_itens[chromium] PASSED
tests/test_detalhe_restaurante.py::test_detalhe_permite_navegar_para_aba_avaliacoes[chromium] PASSED
tests/test_navegacao_restaurantes.py::test_lista_de_restaurantes_carrega[chromium] PASSED
tests/test_navegacao_restaurantes.py::test_filtrar_restaurantes_por_categoria[chromium] PASSED
tests/test_navegacao_restaurantes.py::test_clicar_em_restaurante_abre_detalhes[chromium] PASSED
========================= 10 passed in 42.15s ==============================
```

---

## 6. Análise crítica dos testes

**O teste quebrou em algum momento?**
O checkout depende do carrinho ter itens — se a pré-condição falhar (ex.: `aguardar_item_adicionado` timeout), o checkout test também falha. O fixture isola essa responsabilidade claramente.

**Quais seletores foram mais difíceis?**
A mensagem de confirmação — depende do texto exato exibido pelo sistema. Se o texto mudar (ex.: "Pedido enviado com sucesso!"), o seletor precisa de atualização.

**O Codegen ajudou?**
Capturou o caminho feliz completo. Não gerou asserções sobre a confirmação.

**O teste é confiável?**
Sim para o caminho feliz. O checkout em ambiente de teste usa dados simulados ("pedido de teste"), então não há dependência de estado externo.

**O que tornaria o teste mais robusto?**
`data-testid="order-success-message"` eliminaria a dependência do texto exato. Um teste adicional para "finalizar com carrinho vazio" (espera erro ou botão desabilitado) cobriria um cenário de borda importante.

**Riscos de manutenção?**
Alteração no texto da mensagem de sucesso ou no texto do link "Ver Detalhes" quebraria o seletor.

---

## 7. Reflexão final no contexto do LocalEats (todos os fluxos)

**Testes automatizados substituem testes manuais?**
Não. Eles substituem a *repetição* de testes de regressão em deploys. Testes exploratórios, de usabilidade e visuais continuam sendo responsabilidade humana.

**Vale a pena automatizar todos os fluxos?**
Não. Automatizar tudo é caro de manter. A estratégia aplicada aqui cobre os **fluxos críticos** (navegação → detalhe → carrinho → checkout), que formam o caminho principal de valor do LocalEats.

**Qual tipo de teste deve ser priorizado?**
Pirâmide de testes: muitos **unitários** (já feitos com TDD) → camada de **integração** → poucos **E2E** sobre os fluxos de maior valor. E2E é o mais caro — reserve-o para o que realmente importa.

**Como isso ajuda o projeto do grupo?**
Com os 10 testes E2E distribuídos nos 4 fluxos, qualquer mudança no frontend que quebre navegação, detalhes, carrinho ou checkout é detectada automaticamente. O CI pode rodar `pytest` a cada pull request e bloquear deploys com regressão — sem precisar testar manualmente cada funcionalidade.

> **Mentalidade aplicada:** "Se a interface mudar amanhã, meu teste ainda vai funcionar?" — por isso priorizamos seletores por *role/text*, centralizamos no POM e usamos esperas explícitas, em vez do código bruto do Codegen.
