# Aula 17 – Integração Contínua, Qualidade Automatizada, Métricas e Gestão de Defeitos

## Integrantes

- Bernardo Ginar de Carvalho — 782410122
- Bryan Laquimam Lübke Gonçalves — 782410011
- Filipe Silveira Maciel — 71901368
- Pedro Hasse Niemczewski — 781310203

---

## 1. Repositório da Atividade

| Item | Descrição |
|--------|--------|
| Nome do repositório | projeto-qualidade-software-aula-17 |
| Link do repositório | https://github.com/pedrohassen/projeto-qualidade-software-aula-17 |

### Estrutura de Diretórios

```text
projeto-qualidade-software-aula-17/
├── tests/ 
│   └── test_entrega.py
├── .github/
│   └── workflows/
│       └── quality.yml
└── entrega.py
```

---

## 2. Planejamento da Funcionalidade

| Item | Descrição |
|--------|--------|
| Título da Issue | Implementar cálculo do valor total do pedido |
| Objetivo da funcionalidade | Calcular automaticamente a taxa de entrega |
| Link da Issue | https://github.com/pedrohassen/projeto-qualidade-software-aula-17/issues/1 |

---

## 3. Teste Automatizado

| Item | Descrição |
|--------|--------|
| Tipo de teste | TDD |
| Objetivo do teste | Verificar o cálculo correto da taxa de entrega |
| Link para o arquivo do teste | https://github.com/pedrohassen/projeto-qualidade-software-aula-17/blob/main/tests/test_entrega.py |

```python
import pytest

from entrega import calcular_taxa_entrega


def test_deve_cobrar_taxa_fixa_para_distancia_ate_3km():
    # Arrange
    distancia = 2.5

    # Act
    resultado = calcular_taxa_entrega(distancia)

    # Assert
    assert resultado == 5.0


def test_deve_lancar_erro_quando_distancia_for_negativa():
    # Arrange
    distancia_invalida = -1.5

    # Act & Assert
    with pytest.raises(ValueError, match="Distância inválida"):
        calcular_taxa_entrega(distancia_invalida)


def test_deve_cobrar_taxa_proporcional_acima_de_3km():
    # Arrange
    distancia = 5.0

    # Act
    resultado = calcular_taxa_entrega(distancia)

    # Assert
    assert resultado == 9.0
```

---

## 4. Pipeline de Integração Contínua

| Item | Descrição |
|--------|--------|
| Nome do workflow | Quality Check |
| Evento que dispara a execução | push e pull_request |
| Link para o workflow | https://github.com/pedrohassen/projeto-qualidade-software-aula-17/blob/main/.github/workflows/quality.yml |
| Link da execução | https://github.com/pedrohassen/projeto-qualidade-software-aula-17/actions |

```yaml
name: Quality Check
on:
  push:
  pull_request:
jobs:
  tests:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
    
      - name: Instalar dependencias
        run: |
          pip install pytest

      - name: Executar testes
        run: pytest
      
      - name: Instalar dependencias (com extras)
        run: |
          pip install pytest flake8 pytest-cov

      - name: Verificar estilo do codigo
        run: flake8 . --max-line-length=100 --exclude=.venv

      - name: Executar testes com cobertura
        run: pytest --cov=. --cov-fail-under=80
```

---

## 5. Indicadores de Qualidade

| Indicador | Valor |
|------------|---------|
| Quantidade de testes executados | 1 |
| Quantidade de testes aprovados | 1 |
| Quantidade de testes com falha | 0 |
| Status final do pipeline | Sucesso |

---

## 6. Registro de Defeito

| Item | Descrição |
|--------|--------|
| Título do defeito | Erro no cálculo da taxa de entrega |
| Severidade | Alta |
| Link da Issue | https://github.com/pedrohassen/projeto-qualidade-software-aula-17/issues/4 |

O defeito foi simulado alterando a função para retornar um valor incorreto (zero) quando a distância informada for negativa. O problema foi identificado pela falha do teste automatizado durante a execução do pipeline. Após corrigir a implementação, os testes voltaram a ser aprovados.