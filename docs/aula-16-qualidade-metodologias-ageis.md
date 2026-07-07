# PBL 11 — Qualidade em Metodologias Ágeis — LocalEats

**Centro Universitário Senac-RS**
**ADS - Análise e Desenvolvimento de Sistemas / SPI - Sistemas para Internet**
**Unidade Curricular:** Qualidade de Software
**Prof.:** Luciano Zanuz

**Equipe:** Bernardo Carvalho, Bryan Laquimam, Filipe Maciel, Pedro Hasse

**Sistema analisado:** [LocalEats](https://local-eats-unisenac.vercel.app/)

---

## 1. Análise de Práticas Ágeis no Processo

| Prática | Existe no processo? | Como é aplicada atualmente? | Pode ser melhorada? |
|---|---|---|---|
| Planejamento iterativo | Parcialmente | O trabalho é dividido em entregas por aula/sprint, mas sem um planejamento formal de sprint (sem sprint planning documentado ou metas claras por ciclo) | Sim — adotar reuniões curtas de planejamento no início de cada ciclo, definindo objetivo e escopo da entrega |
| Priorização de funcionalidades | Parcialmente | As funcionalidades são escolhidas de forma informal, geralmente pela ordem em que surgem as ideias ou pela urgência da entrega | Sim — usar um backlog priorizado (ex.: MoSCoW ou priorização por valor/esforço) |
| Entregas incrementais | Sim | O sistema evolui em partes (cadastro, listagem de locais, avaliações etc.), entregues aos poucos ao longo do semestre | Sim — formalizar cada incremento como uma versão testável e documentada |
| Feedback frequente | Não | O feedback acontece principalmente nas correções das aulas/PBLs, sem ciclo de revisão constante com o grupo ou usuários | Sim — instituir revisões periódicas entre os integrantes e, se possível, testes com usuários reais |
| Trabalho colaborativo | Sim | A equipe divide tarefas entre os integrantes e utiliza um repositório Git compartilhado | Sim — adotar pair programming ou revisões de código (code review) antes do merge |
| Controle visual das atividades | Não | Não há um quadro visual formal; o acompanhamento das tarefas é feito de forma verbal ou por mensagens no grupo | Sim — implementar um quadro Kanban (Trello, GitHub Projects) |
| Melhoria contínua | Parcialmente | Ajustes são feitos quando surgem problemas, mas não há um momento formal de retrospectiva | Sim — realizar retrospectivas curtas ao final de cada entrega |

### Conclusão

O processo do LocalEats já apresenta pontos fortes, como entregas incrementais e um bom nível de trabalho colaborativo via Git. Por outro lado, faltam práticas estruturadas de planejamento, priorização e controle visual, o que torna o fluxo de trabalho mais reativo do que proativo. A ausência de feedback frequente e de retrospectivas dificulta a identificação precoce de problemas e a melhoria contínua do processo. No geral, a equipe tem uma base ágil informal, mas ainda distante de um processo estruturado segundo Scrum, Kanban ou XP. Formalizar o backlog, adotar um quadro visual e criar rituais leves de revisão são os passos mais simples e com maior impacto imediato na qualidade do processo.

---

## 2. Propostas de Melhoria Ágil

| Melhoria Proposta | Metodologia Relacionada | Benefício Esperado | Proposto por |
|---|---|---|---|
| Implementar um quadro Kanban (ex.: GitHub Projects) para visualizar o status de cada tarefa (a fazer, em andamento, em revisão, concluído) | Kanban | Maior visibilidade do fluxo de trabalho e identificação rápida de gargalos | Bernardo Carvalho |
| Adotar reuniões curtas e frequentes (dailies/checkpoints) entre os integrantes para alinhar progresso e bloqueios | Scrum | Comunicação mais frequente, detecção antecipada de problemas e menor retrabalho | Bryan Laquimam |
| Criar um backlog priorizado de funcionalidades, com critérios claros de valor e esforço, revisado a cada novo ciclo | Lean Software Development | Foco no que realmente agrega valor ao usuário e redução de desperdício de esforço | Filipe Maciel |
| Adotar revisão de código entre pares (code review) antes de integrar novas funcionalidades ao repositório principal | XP (Extreme Programming) | Redução de defeitos, código mais consistente e disseminação do conhecimento entre a equipe | Pedro Hasse |

---

## 3. Definition of Ready (DoR)

Uma funcionalidade só entra em desenvolvimento quando atender aos seguintes critérios:

1. O requisito possui critérios de aceitação definidos e claros.
2. A funcionalidade está descrita de forma compreensível para todos os integrantes da equipe.
3. As dependências técnicas (ex.: banco de dados, APIs externas, componentes já existentes) estão identificadas.
4. O esforço estimado da tarefa foi discutido e é considerado viável dentro do prazo do ciclo.
5. Já foi definido quem será o responsável pela implementação.
6. Não existem impedimentos conhecidos (ex.: falta de acesso, decisão de design pendente) que bloqueiem o início do desenvolvimento.

---

## 4. Definition of Done (DoD)

Uma funcionalidade é considerada concluída quando atender aos seguintes critérios:

1. Os critérios de aceitação da funcionalidade foram atendidos.
2. O código foi revisado por pelo menos outro integrante da equipe (code review).
3. A funcionalidade foi testada manualmente e não apresenta erros conhecidos no fluxo principal.
4. O código está versionado e documentado (commit claro, sem trechos de teste ou comentários desnecessários).
5. A funcionalidade foi integrada à branch principal sem quebrar o restante do sistema.
6. A documentação do projeto (README ou changelog) foi atualizada, se aplicável.

---

## Mentalidade da equipe

> "Como podemos tornar nosso processo mais ágil sem abrir mão da qualidade?"

Acreditamos que pequenas mudanças estruturais — como um quadro visual, um backlog priorizado e revisões periódicas — já trazem ganhos significativos de organização e qualidade, sem exigir a adoção completa e rígida de um framework ágil formal.
