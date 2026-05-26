# Aula 9 – Testes Unitários e TDD

### Estrutura do Projeto

```text
.
├── src/
│   ├── fidelidade.py
│   ├── pedido.py
│   ├── desconto.py
│   └── entrega.py
└── tests/
    ├── test_fidelidade.py
    ├── test_pedido.py
    ├── test_desconto.py
    └── test_entrega.py
```

### 2. Testes Unitários

Cada integrante implementou seus testes unitários no respectivo arquivo dentro da pasta /tests.

#### 2.1 Pedro Hasse Niemczewski – Testes (entrega)

**Teste 1 – Distância até 3km**

- **Cenário:** Taxa fixa
- **Resultado esperado:** Valor fixo

**TDD**

- **Red:** falha inicial por função inexistente (`ModuleNotFoundError`)
- **Green:** retorno fixo de `5.0` inserido no arquivo `src/entrega.py` para fazer o teste passar
- **Refactor:** organização inicial da estrutura de importação do módulo

**Refatoração**

- Ajuste do escopo do arquivo e caminhos de execução

**Execução**

- **Resultado:** Passou

**Teste 2 – Distância negativa**

- **Cenário:** Entrada inválida
- **Resultado esperado:** Erro

**TDD**

- **Red:** falha por não lançar a exceção esperada (`AssertionError`), já que a função ainda retornava apenas o valor fixo
- **Green:** inclusão da estrutura condicional `if distancia < 0` lançando `ValueError("Distância inválida")`
- **Refactor:** isolamento das regras de validação no topo da função

**Refatoração**

- Garantia de integridade dos dados de entrada antes da execução da lógica de cálculo

**Execução**

- **Resultado:** Passou

**Teste 3 – Distância acima de 3km**

- **Cenário:** Taxa fixa + valor adicional por quilômetro extra
- **Resultado esperado:** Retorno de R$ 5,00 somado a R$ 2,00 por km excedente

**TDD**

- **Red:** falha por retornar apenas o valor fixo de `5.0` (`AssertionError`), já que a função ainda não calculava o excedente
- **Green:** implementação da lógica matemática com `quilometros_extras = distancia - 3` multiplicados pela taxa extra
- **Refactor:** limpeza da estrutura condicional usando retornos limpos para cada cenário de distância

**Refatoração**

- Separação explícita entre o fluxo de taxa fixa (até 3km) e o cálculo dinâmico de quilometragem excedente

**Execução**

- **Resultado:** Passou

#### 2.2 Bernardo Ginar de Carvalho – Testes (desconto)

**Teste 1 – Aplicação de desconto válido**

- **Cenário:** Pedido de R$ 100,00 com 10% de desconto
- **Resultado esperado:** Retornar R$ 90,00

**TDD**

- **Red:** Falhou porque o arquivo `src/desconto.py` e a função não existiam (`ImportError`).
- **Green:** Código implementado com a lógica matemática simples `valor - (valor * percentual / 100)`.
- **Refactor:** Tipagem de parâmetros e do retorno da função foram adicionados.

**Teste 2 – Percentual inválido**

- **Cenário:** Informar percentual de desconto > 100% ou < 0%
- **Resultado esperado:** Lançar `ValueError`

**TDD**

- **Red:** Falha de assertion inicialmente, pois a função não validava os limites do percentual.
- **Green:** Inclusão de um `if percentual_desconto < 0 or percentual_desconto > 100:` lançando erro.
- **Refactor:** Isolamento da checagem de erros no topo da função antes dos cálculos matemáticos.

**Teste 3 – Aplicação de desconto máximo (100%)**

- **Cenário:** Pedido de R$ 50,00 com 100% de desconto
- **Resultado esperado:** Retornar R$ 0,00

**TDD**

- **Red:** Falha potencial de lógica se a matemática deduzisse errado ou o sistema rejeitasse o número 100 (limite).
- **Green:** A lógica existente para calcular o desconto suporta o limite, retornando `0.0` com sucesso.
- **Refactor:** Confirmação da robustez do código testando os limites numéricos aceitos pela regra de negócios.

#### 2.3 Bryan Laquimam Lübke Gonçalves – Testes (pedido)

**Teste 1 – Fechamento de pedido normal**

- **Cenário:** Soma de itens, adição da taxa de entrega e subtração de descontos
- **Resultado esperado:** Retornar o valor exato final (ex: R$ 45,00)

**TDD**

- **Red:** Inicialmente falhou pois o arquivo `src/pedido.py` e a função não existiam (`ModuleNotFoundError`).
- **Green:** Criação da função somando os itens e a taxa, subtraindo o desconto.
- **Refactor:** Uso da função nativa `sum()` para simplificar a iteração sobre a lista de itens.

**Teste 2 – Total negativo**

- **Cenário:** Desconto concedido é maior do que o valor total de produtos mais frete
- **Resultado esperado:** O pedido deve custar R$ 0,00, não podendo haver saldo negativo/devedor para o sistema.

**TDD**

- **Red:** Ao aplicar um super desconto agressivo (ex: 50.0 em um total de 15.0), o sistema retornou valores negativos.
- **Green:** Ajuste na lógica incluindo a função `max(0.0, total)` no retorno para estabelecer um piso financeiro de R$ 0,00.
- **Refactor:** Garantia de que cálculos financeiros não resultem em crédito indevido para o usuário de forma sucinta e limpa.

**Teste 3 – Pedido sem itens**

- **Cenário:** Fechar um pedido enviando uma lista de itens vazia `[]`
- **Resultado esperado:** Lançar erro `ValueError`

**TDD**

- **Red:** A função aceitava listas vazias perfeitamente, o que acabava calculando apenas taxa de entrega menos desconto (um estado inválido para a regra de negócio).
- **Green:** Adicionado uma verificação `if not itens: raise ValueError(...)` parando a execução caso não haja produtos.
- **Refactor:** A validação foi colocada no início da função aplicando o conceito de _fail-fast_ (falhar rapidamente sem onerar o sistema computando o resto).

#### 2.4 Filipe Silveira Maciel – Testes (fidelidade)

**Teste 1 – Conversão de pontos em desconto**

- **Cenário:** Cliente possui 50 pontos acumulados e deseja converter (1 ponto = R$ 0,50).
- **Resultado esperado:** Retornar R$ 25,00 de desconto.

**TDD**

- **Red:** Falhou inicialmente por falta do módulo `src/fidelidade.py` e da função.
- **Green:** Implementação básica retornando a multiplicação dos pontos pelo fator de conversão `0.5`.
- **Refactor:** Definição clara da tipagem de parâmetros (`int`) e do retorno (`float`) para compor os descontos do pedido.

**Teste 2 – Conversão com zero pontos**

- **Cenário:** Cliente não possui pontos acumulados (0 pontos).
- **Resultado esperado:** Retornar R$ 0,00 de desconto.

**TDD**

- **Red:** Risco de quebra de lógica se o sistema recusasse a operação de cliente sem pontos.
- **Green:** A lógica direta de `pontos * 0.5` lidou perfeitamente com zero, retornando `0.0`.
- **Refactor:** Validação de segurança no fluxo feliz para garantir que clientes novos não encontrem erros no fechamento do carrinho.

**Teste 3 – Pontuação negativa inválida**

- **Cenário:** O sistema recebe um valor negativo de pontos (ex: -10) por alguma falha na base de dados.
- **Resultado esperado:** Lançar erro `ValueError`.

**TDD**

- **Red:** A função estava aceitando números negativos e gerando um desconto negativo (que acabaria somando indevidamente no total do carrinho do Bryan).
- **Green:** Adicionado a checagem `if pontos < 0: raise ValueError(...)`.
- **Refactor:** A checagem atua como um portão de segurança, protegendo as regras de negócio financeiras da plataforma.

### 3 Reflexão Geral

- **Foi difícil escrever testes antes do código?**
  - Sim, exige uma mudança de mentalidade. Pensar nos resultados esperados, cenários de erro e limites antes mesmo de programar a lógica principal força a equipe a entender a regra de negócio a fundo desde o início.
- **O TDD ajudou no desenvolvimento?**
  - Com certeza. Focar em resolver um problema por vez (primeiro fazer funcionar, depois melhorar) deixou o desenvolvimento mais organizado. Colocar as validações de erro logo no início das funções (como barrar itens vazios e pontos negativos) deixou o código mais seguro e limpo.
- **Os testes aumentaram a confiança no código?**
  - Sim. Saber que regras importantes (como cálculo de frete, descontos e fechamento de pedidos) estão testadas de forma automatizada traz muita segurança. Isso garante que alterações futuras feitas pela equipe não vão quebrar o que já está funcionando.
- **O que melhorariam?**
  - Poderíamos criar testes para situações onde dados no formato incorreto são enviados (como receber um texto onde se espera um número). Também seria interessante usar ferramentas para mostrar exatamente qual porcentagem do nosso código está coberta pelos testes.
- **Como isso ajuda no projeto?**
  - Garante que a parte financeira do aplicativo funcione sem erros. Testando essas funções matemáticas separadamente, passamos muito menos tempo procurando _bugs_ e entregamos um sistema muito mais estável para o usuário final.
