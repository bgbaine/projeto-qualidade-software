# Diagnóstico de Qualidade – Startup Local Eats

## 1. Diagnóstico da Situação Atual

### Papéis Atuais (Prováveis)
Atualmente, a startup opera em um modelo focado exclusivamente em velocidade de entrega, sem processos formais de validação. Os papéis existentes provavelmente são:
* **Desenvolvedores (Fullstack):** Responsáveis por todo o ciclo de vida da funcionalidade, desde a interface até o banco de dados, sem revisão de pares.
* **Gerente de Produto / Fundador:** Focado em prazos de mercado e no evento gastronômico, definindo requisitos muitas vezes de forma verbal ou pouco documentada.

### Responsabilidade pela Qualidade
Atualmente, a qualidade é uma **responsabilidade implícita e isolada do desenvolvedor**. Não há uma etapa de verificação independente. O desenvolvedor "testa" o próprio código, o que leva ao vício de confirmação (testar apenas o caminho feliz).

### Problemas da Falta de Clareza nas Responsabilidades
* **Conflito de Interesses:** O desenvolvedor é pressionado por prazo, o que o leva a negligenciar testes em prol da entrega.
* **Falta de Dono (Bug Ping-Pong):** Quando ocorre um erro como "pedido duplicado", gasta-se mais tempo tentando descobrir de quem é a culpa (frontend ou backend) do que resolvendo a causa raiz.
* **Baixa Confiabilidade:** Erros críticos chegam ao cliente final, gerando prejuízo financeiro direto para os restaurantes parceiros.

### A Qualidade como Responsabilidade Compartilhada
A qualidade deve ser entendida como um **processo coletivo**. O QA não é o único responsável, mas o facilitador. O desenvolvedor é responsável pela qualidade do código (testes unitários), o PO pela qualidade do requisito (clareza) e o QA pela qualidade da experiência e integração.

---

## 2. Papéis da Equipe e Responsabilidades

Propomos a seguinte estrutura para formalizar a qualidade no Local Eats:

| Papel | Responsabilidade Principal | Relação com a Qualidade |
| :--- | :--- | :--- |
| **Desenvolvedor** | Implementação técnica de features. | Responsável pela integridade do código e criação de testes unitários. |
| **Analista de Qualidade (QA)** | Estratégia e execução de testes. | Identificar riscos, planejar cenários de erro e validar a experiência do usuário. |
| **Product Owner (PO)** | Gestão do Backlog e Requisitos. | Definir "Critérios de Aceite" claros para que a equipe saiba exatamente o que testar. |
| **DevOps** | Automação de deploy e infraestrutura. | Garantir que o ambiente de teste seja igual ao de produção e automatizar pipelines de execução de testes. |

---

## 3. Práticas de QA Sugeridas

Para estabilizar a plataforma, recomendamos a implementação imediata de:

1.  **Definição de Pronto (Definition of Done - DoD):** Acordo onde uma tarefa só é considerada concluída se: passou por revisão de código, não possui bugs críticos e foi validada em ambiente de homologação.
2.  **Code Review (Revisão por Pares):** Implementar a obrigatoriedade de que todo *Pull Request* seja revisado por outro desenvolvedor para identificar falhas lógicas (como a que gera pedidos duplicados).
3.  **Gestão e Tracking de Defeitos:** Utilização de uma ferramenta (como GitHub Issues ou Jira) para documentar bugs com passos para reprodução, prioridade e severidade.
4.  **Testes de Fumaça (Smoke Tests):** Um conjunto rápido de testes manuais ou automatizados nos fluxos críticos (Login e Finalizar Pedido) que devem ser executados antes de qualquer deploy em produção.

---

## 4. Anúncios de Contratação

### Vaga 01: Analista de Qualidade de Software (QA)
**Empresa:** Local Eats  
**Sobre a vaga:** Buscamos um QA para transformar nossa cultura de desenvolvimento. Você será responsável por garantir que nossos usuários e restaurantes tenham uma experiência livre de erros.

* **Principais Responsabilidades:**
    * Planejar e executar testes funcionais e exploratórios (Web e Mobile).
    * Documentar e acompanhar o ciclo de vida de bugs.
    * Apoiar o PO na escrita de critérios de aceite robustos.
* **Requisitos Obrigatórios:**
    * Experiência com testes de software e metodologias ágeis.
    * Boa capacidade analítica e de comunicação.
* **Requisitos Desejáveis:**
    * Conhecimento básico em SQL para validação de dados.
    * Noções de automação de testes (Cypress ou Selenium).
* **Certificação Desejável:** ISTQB-CTFL.

---

### Vaga 02: Desenvolvedor Backend (.NET / Node.js)
**Empresa:** Local Eats  
**Sobre a vaga:** Procuramos uma pessoa desenvolvedora com foco em robustez. Seu desafio será otimizar nossas APIs e garantir que falhas de persistência ou concorrência sejam mitigadas no código.

* **Principais Responsabilidades:**
    * Desenvolver APIs escaláveis e seguras.
    * Implementar e manter testes unitários e de integração.
    * Participar ativamente de revisões de código.
* **Requisitos Obrigatórios:**
    * Sólida experiência em C#/.NET ou Node.js (TypeScript).
    * Conhecimento em boas práticas (SOLID e Clean Code).
* **Requisitos Desejáveis:**
    * Experiência com arquitetura de microserviços.
    * Conhecimento em bancos de dados relacionais e estratégias de cache.
* **Certificação Desejável:** AZ-204 ou certificações correlatas de desenvolvimento.
