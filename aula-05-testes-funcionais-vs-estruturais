PBL 4

1. Funcionalidade Escolhida
Funcionalidade: Busca de Restaurantes
O que faz: Permite encontrar restaurantes por texto livre ou por filtro de categoria (Italiana, Japonesa, Brasileira, Mexicana). O sistema consulta a base de dados e retorna os resultados correspondentes.
O que o usuário espera: Resultados rápidos e relevantes ao digitar ou filtrar. Espera que a tecla Enter funcione, que filtros sejam aplicados corretamente e que a ausência de resultados seja comunicada de forma clara.

2. Testes Caixa-Preta (Visão do Usuário)
Testamos observando apenas entradas e saídas, sem conhecer o código — como um usuário real faria.
Cenários de teste

Busca por termo válido: digitar "pizza" e verificar se os resultados são coerentes com o termo.
Busca por termo inexistente: digitar "xyzabc" e verificar se o sistema exibe mensagem clara de ausência de resultados.
Tecla Enter: digitar um termo e pressionar Enter — falha já identificada na PBL 1.
Filtro por categoria: selecionar "Japonesa" e verificar se apenas restaurantes dessa culinária aparecem.
Campo vazio: acionar a busca sem digitar nada e observar o comportamento.
Caracteres especiais: digitar <script> ou @#$% e verificar se a interface se mantém estável.
Filtro + texto combinados: digitar "sushi" com filtro "Japonesa" ativo e verificar se ambos os critérios são respeitados.

Possíveis erros identificados

Resultados fora da categoria selecionada.
Nenhum feedback quando a busca não retorna resultados.
Busca não disparada ao pressionar Enter.
Erro ou travamento ao receber entradas inesperadas.


3. Testes Caixa-Branca (Visão do Sistema)
Com acesso ao código, é possível testar caminhos internos que o usuário nunca alcançaria diretamente.
Lógica hipotética
função buscarRestaurantes(termo, filtroCategoria):

  1. Se termo vazio e filtro "Todos": retornar lista completa
  2. Sanitizar entrada (trim, remover caracteres especiais)
  3. Se filtro ativo: filtrar por categoria
  4. Se termo não vazio: filtrar por nome ou categoria (case-insensitive)
  5. Se lista vazia: retornar mensagem de ausência
  6. Retornar lista ordenada
Situações a testar no código

Sanitização: verificar se entradas como <script> são tratadas antes da consulta — ausência disso abre brecha para XSS.
Case-insensitive: verificar se "pizza" e "Pizza" retornam o mesmo resultado.
Ordem das operações: testar se o filtro de categoria é aplicado antes ou depois do filtro textual e se isso altera os resultados.
Lista vazia: verificar se o sistema trata corretamente o retorno vazio sem lançar exceção (ex: .map() sobre undefined).
Evento de teclado: confirmar se há listener para keydown: Enter — ausência confirma a falha observada na caixa-preta.

Possíveis erros identificados

Ausência de sanitização expondo o sistema a injeção de código.
Comparação de strings sem normalização de caixa gerando resultados inconsistentes.
Exceção não tratada ao iterar sobre array vazio.
Listener de teclado ausente.


4. Comparação entre as Abordagens
A caixa-preta parte do comportamento visível: fornece entradas e avalia se as saídas correspondem ao esperado. A caixa-branca parte da estrutura interna: analisa condições, fluxos e caminhos que dificilmente seriam exercitados em uso normal.
Caixa-preta encontra falhas de comportamento — funcionalidades quebradas, resultados incorretos, ausência de feedback. Valida se os requisitos foram atendidos na prática.
Caixa-branca encontra falhas estruturais — lógica incorreta, caminhos não cobertos, ausência de sanitização, exceções não tratadas. Garante robustez técnica e segurança.

5. Reflexão no Contexto do LocalEats
O sistema apresenta problemas nos dois níveis. Falhas visíveis como a busca sem suporte a Enter e filtros inconsistentes são identificadas pela caixa-preta. Falhas internas como o armazenamento inseguro no localStorage e a ausência de sanitização só aparecem com análise do código.
Usar apenas uma abordagem seria insuficiente. A caixa-preta sozinha deixa vulnerabilidades ocultas; a caixa-branca sozinha pode garantir código correto que ainda assim não atende o usuário. Como estabelecido na PBL 3, qualidade exige combinação de perspectivas — e isso vale tanto para os níveis de teste quanto para as abordagens aplicadas.

Conclusão
A busca de restaurantes é a funcionalidade central do LocalEats e concentra riscos dos dois tipos. Testar apenas o que é visível não é suficiente para um sistema com as vulnerabilidades já mapeadas. A combinação das abordagens reflete o mesmo princípio das PBLs anteriores: qualidade é um processo contínuo que exige tanto a visão do usuário quanto a visão técnica.
