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
