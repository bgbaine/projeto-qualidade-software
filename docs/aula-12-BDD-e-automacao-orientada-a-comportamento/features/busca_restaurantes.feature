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
