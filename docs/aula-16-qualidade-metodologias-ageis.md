# PBL 11 — Qualidade em Metodologias Ágeis — LocalEats

**Centro Universitário Senac-RS**
**ADS - Análise e Desenvolvimento de Sistemas / SPI - Sistemas para Internet**
**Unidade Curricular:** Qualidade de Software
**Prof.:** Luciano Zanuz

**Equipe:** Bernardo Carvalho, Bryan Laquimam, Filipe Maciel, Pedro Hasse

**Sistema analisado:** [LocalEats](https://local-eats-unisenac.vercel.app/)

---

## 1. Análise de Práticas Ágeis no Processo

Esta análise parte do mapeamento de processo feito na Aula 14 (fluxo demanda → desenvolvimento → testes → correções → entrega) e do diagnóstico de maturidade da Aula 15 (processo classificado como **Inicial** no CMMI / nível **H** no MPS.BR).

| Prática | Existe no processo? | Como é aplicada atualmente? | Pode ser melhorada? |
|---|---|---|---|
| Planejamento iterativo | Parcialmente | Existe um ciclo implícito por PBL/entrega (Aula 14), mas sem sprint planning formal nem metas explícitas por ciclo — o fluxo é conhecido informalmente pela equipe, não documentado | Sim — formalizar um planejamento curto no início de cada entrega, com escopo e critérios de aceite definidos |
| Priorização de funcionalidades | Não | A Aula 15 já apontou a ausência de requisitos documentados e de padronização; funcionalidades são discutidas e priorizadas de forma verbal, sem backlog nem critério de valor/esforço | Sim — criar um backlog com user stories e critérios de aceitação (proposta já indicada na Aula 15) |
| Entregas incrementais | Sim | O LocalEats evolui em partes a cada PBL (mapeamento de processo, testes automatizados, BDD, maturidade etc.), cada entrega adicionando uma camada sobre a anterior | Sim — versionar cada incremento como um release testável, com changelog |
| Feedback frequente | Parcialmente | As seções de reflexão de cada PBL (como a da Aula 14) funcionam como uma retrospectiva informal, mas isso ocorre só por exigência da atividade acadêmica, sem ciclo contínuo entre entregas | Sim — transformar essas reflexões em retrospectivas curtas e recorrentes, independentes do calendário de aula |
| Trabalho colaborativo | Sim | A equipe divide tarefas e versiona tudo no GitHub; testes unitários (Aula 9, TDD) e BDD (Aula 12) já são praticados em conjunto | Sim — a Aula 15 identificou que a revisão de código ainda é ocasional e sem critério; tornar o code review obrigatório via Pull Request |
| Controle visual das atividades | Não | A Aula 15 confirma: a equipe não usa nenhuma ferramenta de gestão de tarefas; o acompanhamento é verbal/informal | Sim — adotar um quadro Kanban (ex.: GitHub Projects), complementando a proposta de GitHub Issues já feita na Aula 15 |
| Melhoria contínua | Parcialmente | Há avanços pontuais entre PBLs (ex.: TDD na Aula 9, BDD na Aula 12), mas sem indicadores de qualidade (cobertura de testes, taxa de defeitos) — a Aula 15 aponta essa lacuna | Sim — acompanhar métricas simples (ex.: cobertura de testes) a cada ciclo |

### Conclusão

O LocalEats já mostra pontos fortes de um processo ágil informal: entregas incrementais claras entre PBLs, trabalho colaborativo via Git e práticas técnicas consistentes como TDD e BDD. Por outro lado, o diagnóstico da Aula 15 (processo no nível Inicial do CMMI) confirma que faltam estruturas básicas de planejamento: não há backlog priorizado, não há ferramenta de gestão de tarefas e a revisão de código acontece de forma ocasional. O feedback existe, mas só na forma das reflexões exigidas por cada PBL, sem virar um hábito contínuo da equipe. Isso torna o processo mais reativo (resolver problemas quando aparecem) do que proativo. Os ganhos mais imediatos viriam de formalizar o que já foi identificado nas Aulas 14 e 15: um quadro visual, um backlog com critérios de aceite e um processo obrigatório de code review — peças que aproximariam o LocalEats de práticas reais de Scrum, Kanban e XP sem exigir a adoção rígida de um framework completo.

---

## 2. Propostas de Melhoria Ágil

As melhorias abaixo respondem diretamente às lacunas já diagnosticadas na Aula 15 (ausência de ferramenta de gestão de tarefas, falta de backlog/rastreabilidade de requisitos e revisão de código sem processo formal), agora reinterpretadas sob a ótica de práticas ágeis específicas.

| Melhoria Proposta | Metodologia Relacionada | Benefício Esperado | Proposto por |
|---|---|---|---|
| Implementar um quadro Kanban (ex.: GitHub Projects) para visualizar o status de cada tarefa (a fazer, em andamento, em revisão, concluído) — resolve a lacuna de "falta de ferramenta de gestão de tarefas" apontada na Aula 15 | Kanban | Maior visibilidade do fluxo de trabalho e identificação rápida de gargalos | Bernardo Carvalho |
| Adotar reuniões curtas e frequentes (dailies/checkpoints) entre os integrantes para alinhar progresso e bloqueios, no lugar da comunicação informal identificada no mapeamento da Aula 14 | Scrum | Comunicação mais frequente, detecção antecipada de problemas e menor retrabalho | Bryan Laquimam |
| Criar um backlog priorizado com user stories e critérios de aceitação, revisado a cada novo ciclo — dá continuidade à proposta de documentar requisitos já sugerida na Aula 15 | Lean Software Development | Foco no que realmente agrega valor ao usuário e redução de desperdício de esforço | Filipe Maciel |
| Tornar obrigatória a revisão de código entre pares (code review) via Pull Request antes de integrar novas funcionalidades ao repositório principal, substituindo a revisão ocasional identificada na Aula 15 | XP (Extreme Programming) | Redução de defeitos, código mais consistente e disseminação do conhecimento entre a equipe | Pedro Hasse |

---

## 3. Definition of Ready (DoR)

A ausência de requisitos documentados foi uma das lacunas centrais identificadas na Aula 15. A DoR abaixo formaliza o mínimo necessário para que isso deixe de acontecer: uma funcionalidade só entra em desenvolvimento quando atender aos seguintes critérios:

1. O requisito possui critérios de aceitação definidos e claros.
2. A funcionalidade está descrita de forma compreensível para todos os integrantes da equipe.
3. As dependências técnicas (ex.: banco de dados, APIs externas, componentes já existentes) estão identificadas.
4. O esforço estimado da tarefa foi discutido e é considerado viável dentro do prazo do ciclo.
5. Já foi definido quem será o responsável pela implementação.
6. Não existem impedimentos conhecidos (ex.: falta de acesso, decisão de design pendente) que bloqueiem o início do desenvolvimento.

---

## 4. Definition of Done (DoD)

A criação de uma DoD já havia sido apontada como melhoria necessária na Aula 15; esta seção formaliza esse critério. Uma funcionalidade é considerada concluída quando atender aos seguintes critérios:

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
