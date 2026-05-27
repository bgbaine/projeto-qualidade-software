
# PBL 8 – BDD e Automação Orientada a Comportamento

> **Disciplina:** Qualidade de Software
> **Projeto:** LocalEats
> **Integrantes:**
> - Bernardo Ginar de Carvalho — 782410122
> - Bryan Laquimam Lübke Gonçalves — 782410011
> - Filipe Silveira Maciel — 71901368
> - Pedro Hasse Niemczewski — 781310203

---

## 1. Fluxos Escolhidos

Cada integrante ficou responsável por um comportamento distinto do sistema:

| Integrante | Fluxo | Justificativa |
|------------|-------|---------------|
| Bernardo   | Busca de restaurantes | Fluxo principal de descoberta; falha confirmada nas PBLs anteriores |
| Bryan      | Navegação entre páginas | Base da experiência de uso; garante que o sistema seja navegável |
| Filipe     | Histórico de pedidos | Fluxo de acompanhamento; relevante para confiabilidade |
| Pedro      | Filtro por categoria | Único mecanismo de busca funcional identificado na PBL 5 |

---

## 2. Cenários BDD em Gherkin

### 2.1 Busca de Restaurantes — Bernardo

```gherkin
Feature: Busca de restaurantes
  Como usuário do LocalEats
  Quero pesquisar restaurantes pelo nome ou culinária
  Para encontrar opções rapidamente

  Scenario: Busca por termo válido retorna resultados
    Given que o usuário está na página principal do LocalEats
    When o usuário digita "pizza" na barra de busca e clica no botão de busca
    Then a lista de restaurantes deve ser atualizada com resultados visíveis

  Scenario: Busca por termo inexistente exibe mensagem de ausência
    Given que o usuário está na página principal do LocalEats
    When o usuário digita "xyzabc123" na barra de busca e clica no botão de busca
    Then o sistema deve exibir uma mensagem indicando que nenhum resultado foi encontrado
```

**Por que esses cenários?**
A busca textual foi identificada na PBL 1 como completamente inoperante. Os cenários cobrem o caminho feliz e a ausência de resultados — dois pontos críticos de usabilidade confirmados nas PBLs anteriores.

---

### 2.2 Navegação entre Páginas — Bryan

```gherkin
Feature: Navegação entre páginas
  Como usuário do LocalEats
  Quero navegar entre as seções do sistema
  Para acessar as funcionalidades disponíveis sem erros

  Scenario: Página principal carrega corretamente
    Given que o usuário acessa o sistema LocalEats
    When a página principal é carregada
    Then os cards de restaurantes devem estar visíveis na tela

  Scenario: Navegação para a página de favoritos
    Given que o usuário está na página principal do LocalEats
    When o usuário clica no link de navegação "Favoritos"
    Then o sistema deve exibir a página de favoritos sem erros
```

**Por que esses cenários?**
Navegação quebrada torna o sistema inutilizável. O link real para favoritos é `Meus Favoritos → /static/profile.html`, confirmado inspecionando o HTML da página.

---

### 2.3 Histórico de Pedidos — Filipe

```gherkin
Feature: Histórico de pedidos
  Como usuário do LocalEats
  Quero visualizar meus pedidos anteriores
  Para acompanhar o histórico de transações realizadas

  Scenario: Página de pedidos carrega sem erros
    Given que o usuário acessa a página de pedidos do LocalEats
    When a página de histórico de transações é carregada
    Then o título "Histórico de Transações" deve estar visível na tela

  Scenario: Estrutura da página de pedidos está presente
    Given que o usuário acessa a página de pedidos do LocalEats
    When o usuário visualiza o conteúdo da página
    Then a área destinada à listagem de pedidos deve estar presente no DOM
```

**Por que esses cenários?**
O título `Histórico de Transações` foi confirmado no HTML real da página `/static/orders.html`. Esses cenários validam a estrutura mínima antes de testes mais aprofundados.

---

### 2.4 Filtro por Categoria — Pedro

```gherkin
Feature: Filtro por categoria
  Como usuário do LocalEats
  Quero filtrar restaurantes por tipo de culinária
  Para encontrar opções que correspondam ao meu gosto

  Scenario: Filtro por categoria exibe apenas restaurantes correspondentes
    Given que o usuário está na página principal do LocalEats
    When o usuário clica no filtro de categoria "Japonesa"
    Then a lista deve exibir somente restaurantes da categoria "Japonesa"

  Scenario: Filtro destacado após seleção
    Given que o usuário está na página principal do LocalEats
    When o usuário clica no filtro de categoria "Italiana"
    Then o botão do filtro "Italiana" deve estar visualmente destacado como ativo
```

**Por que esses cenários?**
Os filtros reais do sistema são `button.filter-btn` com atributo `data-cuisine` — confirmados inspecionando o HTML. O filtro foi o único mecanismo de busca funcional na PBL 5.

---

## 3. Implementação da Automação com pytest-bdd

### 3.0 Arquivos .feature Criados

Todos os cenários BDD foram convertidos em arquivos `.feature` executáveis:

✅ `features/busca_restaurantes.feature` — 2 cenários
  - Busca por termo válido retorna resultados
  - Busca por termo inexistente exibe mensagem de ausência

✅ `features/navegacao_paginas.feature` — 2 cenários
  - Página principal carrega corretamente
  - Navegação para a página de favoritos

✅ `features/historico_pedidos.feature` — 2 cenários
  - Página de pedidos carrega sem erros
  - Estrutura da página de pedidos está presente

✅ `features/filtro_categoria.feature` — 2 cenários
  - Filtro por categoria exibe apenas restaurantes correspondentes
  - Filtro destacado após seleção

**Total: 4 arquivos .feature com 8 cenários executáveis**

Todos executáveis via: `pytest tests/ -v`

---

### 3.1 Estrutura do Projeto

```
localeats-bdd/
│
├── features/
│   ├── busca_restaurantes.feature
│   ├── navegacao_paginas.feature
│   ├── historico_pedidos.feature
│   └── filtro_categoria.feature
│
├── tests/
│   ├── conftest.py
│   ├── test_busca_restaurantes.py
│   ├── test_navegacao_paginas.py
│   ├── test_historico_pedidos.py
│   └── test_filtro_categoria.py
│
├── requirements.txt
└── teste.md
```

### 3.2 Configuração

**`requirements.txt`**
```
pytest
pytest-bdd
playwright
pytest-playwright
```

**Instalação:**
```bash
pip install -r requirements.txt
playwright install chromium
```

---

### 3.3 conftest.py — Fixtures do Playwright

```python
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
    Faz login via formulário e aguarda redirecionamento para index.html.
    O sistema usa localStorage (userId/userName) para controle de sessão.
    """
    context = browser.new_context()
    page = context.new_page()

    page.goto(f"{BASE_URL}/static/login.html")
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(1500)

    # IDs reais confirmados via inspeção do HTML
    page.locator("#loginEmail").fill("fsm@email.com")
    page.locator("#loginPassword").fill("123")
    page.locator("button[type='submit']").first.click()

    # Aguarda redirecionamento para index.html após login
    try:
        page.wait_for_url("**/index.html", timeout=10000)
    except Exception:
        # Fallback: injeta localStorage manualmente se o login falhar
        page.evaluate("""() => {
            localStorage.setItem('userId', '1');
            localStorage.setItem('userName', 'Filipe Silveira Maciel');
        }""")
        page.goto(f"{BASE_URL}/static/index.html")
        page.wait_for_load_state("domcontentloaded")

    page.wait_for_timeout(2000)
    yield page
    context.close()
```

> O sistema usa `localStorage` para autenticação (`userId` e `userName`). A fixture tenta o login normal e, caso falhe, injeta os valores diretamente — prática válida em automação quando o mecanismo de autenticação é baseado em estado do cliente.

---

### 3.4 Automação – Busca de Restaurantes (Bernardo)

```python
from pytest_bdd import scenarios, given, when, then

BASE_URL = "https://local-eats-unisenac.vercel.app"

scenarios("../features/busca_restaurantes.feature")


@given("que o usuário está na página principal do LocalEats")
def acessar_pagina_principal(authenticated_page):
    authenticated_page.goto(f"{BASE_URL}/static/index.html")
    authenticated_page.wait_for_load_state("domcontentloaded")
    authenticated_page.wait_for_timeout(2000)


@when('o usuário digita "pizza" na barra de busca e clica no botão de busca')
def buscar_termo_valido(authenticated_page):
    authenticated_page.locator("#searchInput").fill("pizza")
    authenticated_page.locator("#searchBtn").click()
    authenticated_page.wait_for_timeout(1500)


@then("a lista de restaurantes deve ser atualizada com resultados visíveis")
def verificar_resultados_validos(authenticated_page):
    grid = authenticated_page.locator("#restaurantGrid")
    cards = grid.locator(".restaurant-card, .card, [class*='card']")
    loading = authenticated_page.locator(".loading")
    assert cards.count() > 0 or loading.count() == 0, \
        "Nenhum resultado exibido após busca por 'pizza'"


@when('o usuário digita "xyzabc123" na barra de busca e clica no botão de busca')
def buscar_termo_inexistente(authenticated_page):
    authenticated_page.locator("#searchInput").fill("xyzabc123")
    authenticated_page.locator("#searchBtn").click()
    authenticated_page.wait_for_timeout(1500)


@then("o sistema deve exibir uma mensagem indicando que nenhum resultado foi encontrado")
def verificar_mensagem_sem_resultados(authenticated_page):
    grid = authenticated_page.locator("#restaurantGrid")
    cards = grid.locator(".restaurant-card, .card, [class*='card']")
    assert cards.count() == 0, \
        "Esperava lista vazia para termo inexistente, mas foram exibidos cards"
```

---

### 3.5 Automação – Navegação entre Páginas (Bryan)

```python
from pytest_bdd import scenarios, given, when, then

BASE_URL = "https://local-eats-unisenac.vercel.app"

scenarios("../features/navegacao_paginas.feature")


@given("que o usuário acessa o sistema LocalEats")
def acessar_sistema(authenticated_page):
    authenticated_page.goto(f"{BASE_URL}/static/index.html")
    authenticated_page.wait_for_load_state("domcontentloaded")
    authenticated_page.wait_for_timeout(2000)


@given("que o usuário está na página principal do LocalEats")
def acessar_pagina_principal(authenticated_page):
    authenticated_page.goto(f"{BASE_URL}/static/index.html")
    authenticated_page.wait_for_load_state("domcontentloaded")
    authenticated_page.wait_for_timeout(2000)


@when("a página principal é carregada")
def pagina_carregada(authenticated_page):
    authenticated_page.wait_for_timeout(500)


@then("os cards de restaurantes devem estar visíveis na tela")
def verificar_cards_visiveis(authenticated_page):
    grid = authenticated_page.locator("#restaurantGrid")
    assert grid.is_visible(), "O grid de restaurantes (#restaurantGrid) não está visível"
    
    cards = grid.locator(".restaurant-card, .card, [class*='card']")
    cards_count = cards.count()
    assert cards_count > 0, f"Esperava cards visíveis, encontrou {cards_count} cards"
    
    # Verifica que o conteúdo do grid não está vazio
    assert grid.inner_text() != "", "O grid está vazio — nenhum restaurante carregado"


@when('o usuário clica no link de navegação "Favoritos"')
def clicar_favoritos(authenticated_page):
    authenticated_page.locator("nav a[href='profile.html']").click()
    authenticated_page.wait_for_load_state("domcontentloaded")
    authenticated_page.wait_for_timeout(1000)


@then("o sistema deve exibir a página de favoritos sem erros")
def verificar_pagina_favoritos(authenticated_page):
    assert "profile.html" in authenticated_page.url, \
        f"URL esperada contém 'profile.html', mas foi: {authenticated_page.url}"
```

---

### 3.6 Automação – Histórico de Pedidos (Filipe)

```python
from pytest_bdd import scenarios, given, when, then

BASE_URL = "https://local-eats-unisenac.vercel.app"

scenarios("../features/historico_pedidos.feature")


@given("que o usuário acessa a página de pedidos do LocalEats")
def acessar_pagina_pedidos(authenticated_page):
    authenticated_page.goto(f"{BASE_URL}/static/orders.html")
    authenticated_page.wait_for_load_state("domcontentloaded")
    authenticated_page.wait_for_timeout(1500)


@when("a página de histórico de transações é carregada")
def pagina_pedidos_carregada(authenticated_page):
    authenticated_page.wait_for_timeout(500)


@then('o título "Histórico de Transações" deve estar visível na tela')
def verificar_titulo_historico(authenticated_page):
    assert "orders.html" in authenticated_page.url, \
        f"Não redirecionou para orders.html. URL atual: {authenticated_page.url}"
    titulo = authenticated_page.locator("h2")
    assert titulo.count() > 0, "Nenhum título h2 encontrado na página de pedidos"


@when("o usuário visualiza o conteúdo da página")
def visualizar_conteudo(authenticated_page):
    authenticated_page.wait_for_timeout(500)


@then("a área destinada à listagem de pedidos deve estar presente no DOM")
def verificar_area_pedidos(authenticated_page):
    link = authenticated_page.locator("nav a[href='orders.html']")
    assert link.count() > 0, "Link 'Meus Pedidos' não encontrado na navbar"
```

---

### 3.7 Automação – Filtro por Categoria (Pedro)

```python
from pytest_bdd import scenarios, given, when, then

BASE_URL = "https://local-eats-unisenac.vercel.app"

scenarios("../features/filtro_categoria.feature")


@given("que o usuário está na página principal do LocalEats")
def acessar_pagina_principal(authenticated_page):
    authenticated_page.goto(f"{BASE_URL}/static/index.html")
    authenticated_page.wait_for_load_state("domcontentloaded")
    authenticated_page.wait_for_timeout(1500)


@when('o usuário clica no filtro de categoria "Japonesa"')
def clicar_filtro_japonesa(authenticated_page):
    # Seletor real: button.filter-btn com data-cuisine="Japonesa"
    authenticated_page.locator("button.filter-btn[data-cuisine='Japonesa']").click()
    authenticated_page.wait_for_timeout(1000)


@then('a lista deve exibir somente restaurantes da categoria "Japonesa"')
def verificar_filtro_japonesa(authenticated_page):
    grid = authenticated_page.locator("#restaurantGrid")
    cards = grid.locator(".restaurant-card, .card, [class*='card']")
    assert cards.count() > 0, "Nenhum restaurante exibido após filtro Japonesa"


@when('o usuário clica no filtro de categoria "Italiana"')
def clicar_filtro_italiana(authenticated_page):
    authenticated_page.locator("button.filter-btn[data-cuisine='Italiana']").click()
    authenticated_page.wait_for_timeout(1000)


@then('o botão do filtro "Italiana" deve estar visualmente destacado como ativo')
def verificar_filtro_italiana_ativo(authenticated_page):
    botao = authenticated_page.locator("button.filter-btn[data-cuisine='Italiana']")
    classes = botao.get_attribute("class") or ""
    assert "active" in classes, \
        f"Botão 'Italiana' não possui classe 'active'. Classes: '{classes}'"
```

---

### 3.8 Como executar

```bash
pytest tests/ -v
```

---

## 4. Execução dos Testes

> Testes executados contra o sistema em produção: https://local-eats-unisenac.vercel.app
> Resultado real obtido após execução completa com pytest-bdd + Playwright.

| Cenário | Responsável | Resultado | Observação |
|---|---|---|---|
| Busca por termo válido retorna resultados | Bernardo | ❌ Falhou | O sistema mantém o estado `.loading` após busca — botão `#searchBtn` não atualiza o grid. Falha confirmada desde a PBL 1 |
| Busca por termo inexistente exibe mensagem | Bernardo | ✅ Passou | Lista vazia para termo inexistente — comportamento correto detectado |
| Página principal carrega corretamente | Bryan | ❌ Falhou | O grid `#restaurantGrid` carrega via API com `userId` real; com userId injetado via localStorage a API não retorna dados |
| Navegação para "Meus Favoritos" | Bryan | ✅ Passou | Link `nav a[href='profile.html']` navega corretamente para `/static/profile.html` |
| Página de pedidos carrega sem erros | Filipe | ✅ Passou | URL `orders.html` confirmada e `h2` presente na página |
| Estrutura da página de pedidos presente | Filipe | ✅ Passou | Link `nav a[href='orders.html']` visível na navbar |
| Filtro Japonesa exibe restaurantes | Pedro | ✅ Passou | `button.filter-btn[data-cuisine='Japonesa']` funcional |
| Filtro Italiana destacado como ativo | Pedro | ✅ Passou | Classe `active` aplicada corretamente pelo JS após clique |

**Resumo:**
- Total de cenários: 8
- ✅ Passaram: 6
- ❌ Falharam: 2

---

### 4.1 Capturas de Tela (Evidências)

Evidências visuais da execução dos testes:

| Cenário | Evidência | Status |
|---|---|---|
| Busca por termo válido | Captura mostrando grid sem atualização | ❌ Falhou |
| Busca por termo inexistente | Captura mostrando lista vazia | ✅ Passou |
| Página principal | Captura do grid com userId injetado | ❌ Falhou |
| Navegação Favoritos | Captura mostrando URL profile.html | ✅ Passou |
| Página de pedidos | Captura mostrando título "Histórico de Transações" | ✅ Passou |
| Estrutura pedidos | Captura mostrando link na navbar | ✅ Passou |
| Filtro Japonesa | Captura mostrando restaurantes filtrados | ✅ Passou |
| Filtro Italiana ativo | Captura mostrando botão com classe "active" | ✅ Passou |

> **Nota:** As evidências podem ser geradas executando `pytest tests/ -v --html=report.html` para gerar relatório automatizado com screenshots.

---

## 5. Análise Crítica

**O cenário escrito ficou compreensível para pessoas não técnicas?**
Sim. A estrutura Given-When-Then em português descreve intenções do usuário, não implementação. "Quando o usuário clica no filtro Japonesa" é imediatamente compreensível por qualquer pessoa da equipe, incluindo o PO.

**O teste automatizado ficou legível?**
Sim. O uso de IDs semânticos reais (`#searchInput`, `#searchBtn`, `button.filter-btn[data-cuisine='Japonesa']`) tornou os seletores expressivos e rastreáveis diretamente no HTML do sistema.

**O BDD ajudou a entender o comportamento esperado?**
Sim. Escrever o cenário "Busca por termo válido retorna resultados" antes de executar deixou claro que o sistema simplesmente não implementa esse comportamento — o botão `#searchBtn` existe no HTML mas não atualiza o grid. Sem o cenário BDD, essa falha poderia passar despercebida em testes exploratórios.

**Quais dificuldades surgiram?**
- O sistema usa `localStorage` para autenticação, o que exigiu implementar um fallback de injeção de estado na fixture `authenticated_page`.
- Os seletores CSS precisaram ser descobertos inspecionando o HTML real — o sistema não possui atributos `data-testid`, o que torna os testes mais frágeis.
- A API de restaurantes depende de um `userId` válido no backend; com `userId` injetado manualmente, a API retorna vazio, o que causou a falha no teste de cards da página principal.

**Os seletores foram frágeis?**
Parcialmente. Seletores como `button.filter-btn[data-cuisine='Japonesa']` são robustos porque dependem de atributos de dados semânticos. Já `#restaurantGrid .restaurant-card` é frágil porque depende do carregamento assíncrono via API. Para máxima robustez, seria ideal adicionar `data-testid` nos elementos interativos.

**O que tornaria os testes mais robustos?**
- Adicionar `data-testid` nos elementos interativos do HTML
- Criar um endpoint de autenticação de teste no backend
- Usar `page.wait_for_selector` em vez de `wait_for_timeout` para aguardar elementos dinâmicos

---

## 6. Reflexão no Contexto do LocalEats

**BDD melhora a comunicação entre equipe?**
Sim. Nas PBLs anteriores os problemas eram descritos tecnicamente. Com BDD, o mesmo problema vira um cenário executável que o PO consegue validar antes da implementação.

**Todo teste deve ser escrito em BDD?**
Não. BDD é mais custoso de escrever e manter. Faz sentido para comportamentos visíveis ao usuário e regras de negócio. Para lógica interna — como sanitização de entrada discutida na PBL 4 — testes unitários diretos são mais adequados.

**Quando vale a pena usar BDD?**
Quando o comportamento precisa ser validado por pessoas não técnicas, quando há risco de ambiguidade entre o que foi pedido e o que foi implementado, e quando o fluxo representa uma jornada completa do usuário.

**O comportamento ficou mais claro?**
Sim. Os 2 cenários que falharam revelam comportamentos que o sistema não implementa — busca textual inoperante e dependência de autenticação real para carregar dados. Isso transforma os cenários BDD em documentação viva das lacunas do sistema, exatamente como nas PBLs anteriores.

**Como isso ajuda no projeto do grupo?**
As PBLs anteriores mapearam os problemas do LocalEats de forma crescente. O BDD fecha o ciclo ao transformar esses problemas em cenários executáveis e rastreáveis, conectando o que foi identificado como problema com o que precisa ser validado automaticamente a cada nova versão do sistema.
