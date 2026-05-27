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
