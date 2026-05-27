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
