# Aula 9 – Testes Unitários e TDD

### Estrutura do Projeto

```text
.
├── src/
│   ├── pedido.py
│   ├── desconto.py
│   └── entrega.py
└── tests/
    ├── test_pedido.py
    ├── test_desconto.py
    └── test_entrega.py
```

### 2. Testes Unitários

Cada integrante implementou seus testes unitários no respectivo arquivo dentro da pasta /tests.

#### 2.1 Pedro Hasse Niemczewski – Testes (entrega)

**Teste 1 – Distância até 3km**

* **Cenário:** Taxa fixa
* **Resultado esperado:** Valor fixo

**TDD**

* **Red:** falha inicial por função inexistente (`ModuleNotFoundError`)
* **Green:** retorno fixo de `5.0` inserido no arquivo `src/entrega.py` para fazer o teste passar
* **Refactor:** organização inicial da estrutura de importação do módulo

**Refatoração**

* Ajuste do escopo do arquivo e caminhos de execução

**Execução**

* **Resultado:** Passou

**Teste 2 – Distância negativa**

* **Cenário:** Entrada inválida
* **Resultado esperado:** Erro

**TDD**

* **Red:** falha por não lançar a exceção esperada (`AssertionError`), já que a função ainda retornava apenas o valor fixo
* **Green:** inclusão da estrutura condicional `if distancia < 0` lançando `ValueError("Distância inválida")`
* **Refactor:** isolamento das regras de validação no topo da função

**Refatoração**

* Garantia de integridade dos dados de entrada antes da execução da lógica de cálculo

**Execução**

* **Resultado:** Passou

#### 2.2 Reflexão

* **Foi difícil escrever testes antes do código?**
  * Sim, exige uma quebra de paradigma pensar nas saídas e nos cenários de erro antes mesmo de começar a programar a lógica principal da função.
* **O TDD ajudou no desenvolvimento?**
  * Com certeza, pois ao focar em um único problema por vez (primeiro fazer a função existir, depois tratar o erro), o código nasce mais direto e sem complexidade desnecessária.
* **Os testes aumentaram a confiança no código?**
  * Sim, saber que a validação de distância inválida está automatizada dá total segurança de que alterações futuras não vão quebrar essa regra de negócio de forma silenciosa.
* **O que melhorariam?**
  * Adicionar cenários de teste adicionais, como o cálculo proporcional exato para distâncias bem longas (acima de 3km) e tipos de dados inválidos (como strings).
* **Como isso ajuda no projeto?**
  * Garante que as regras críticas do LocalEats (como frete e checkout) fiquem blindadas contra regressões à medida que novos recursos forem integrados pelo grupo.