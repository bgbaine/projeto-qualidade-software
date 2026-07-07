# Aula 15 – Modelos de Maturidade

> Disciplina: Qualidade de Software
> Projeto: LocalEats
> Integrantes do grupo:
>
> * Bernardo
> * Bryan
> * Filipe
> * Pedro

---

## 1. Diagnóstico de Maturidade

| Critério | Sim | Parcial | Não |
|---|---|---|---|
| Os requisitos são documentados? | | | X |
| Existe controle de mudanças? | | | X |
| Há atividades de teste definidas? | X | | |
| Os defeitos são registrados? | | X | |
| O processo de desenvolvimento é conhecido por toda a equipe? | | X | |
| As tarefas são planejadas e acompanhadas regularmente? | | X | |
| Existe padronização para implementação de funcionalidades? | | | X |
| Os testes são executados antes da entrega das funcionalidades? | X | | |
| Há revisão de código ou validação por outro integrante da equipe? | | X | |
| A equipe utiliza ferramentas para gerenciamento das atividades? | | | X |
| Os artefatos do projeto (requisitos, testes, código) são organizados e versionados? | | X | |
| Existe rastreabilidade entre requisitos e funcionalidades implementadas? | | | X |
| A equipe realiza reuniões ou momentos de retrospectiva para identificar melhorias? | | X | |
| Existem indicadores ou métricas para acompanhar a qualidade do projeto? | | | X |

### Classificação: Inicial

O processo da equipe se enquadra no nível **Inicial** do CMMI (nível 1) e no nível **H** do MPS.BR, com alguns elementos emergentes do nível Gerenciado. Os requisitos nunca foram formalmente documentados — o escopo do sistema existia apenas no entendimento compartilhado da equipe — e não há controle de mudanças estabelecido. A comunicação foi conduzida de forma informal, sem ferramentas de gestão de tarefas, e não foram utilizadas métricas formais de qualidade (como cobertura de testes ou taxa de defeitos). Apesar disso, a equipe demonstrou avanços pontuais: nas aulas 6 e 9, foram definidos casos de teste estruturados e praticado TDD, o que evidencia atividades de teste concretas e repetíveis. Os artefatos de código e testes estão versionados no GitHub, e os defeitos foram registrados nos documentos de cada PBL. As seções de reflexão presentes em cada PBL cumpriram informalmente o papel de retrospectiva, identificando melhorias a cada entrega. No entanto, essas práticas ocorreram por iniciativa das atividades acadêmicas, sem um processo contínuo e institucionalizado que independa do contexto de aula. O resultado é um processo reativo, dependente de esforço individual e sem garantia de repetibilidade entre entregas.

---

## 2. Identificação de Lacunas

| Lacuna | Impacto |
|---|---|
| Ausência de documentação de requisitos | Sem requisitos escritos, não há base para validar se uma funcionalidade foi entregue corretamente, o que aumenta o risco de entregas incompletas ou divergentes das expectativas |
| Falta de ferramenta de gestão de tarefas | Sem rastreabilidade das atividades, é difícil saber o que está em andamento, o que foi concluído e quem é responsável por cada item — o que gera retrabalho e perda de contexto |
| Ausência de processo formal de revisão de código | A revisão de código acontecia apenas ocasionalmente, sem critério definido. Isso reduz a detecção de erros antes da integração e compromete a consistência do código entre os membros |
| Falta de rastreabilidade entre requisitos e funcionalidades | Não há mapeamento entre o que foi pedido e o que foi implementado, dificultando a validação da cobertura de funcionalidades e a identificação de gaps |

---

## 3. Propostas de Melhoria

| Melhoria | Benefício |
|---|---|
| Documentar os requisitos como user stories com critérios de aceitação | Permite que toda a equipe tenha uma referência clara do que deve ser desenvolvido e testado, reduzindo ambiguidades e retrabalho |
| Adotar o GitHub Issues como ferramenta de gestão de tarefas e registro de defeitos | Centraliza o acompanhamento das atividades, torna os defeitos rastreáveis e estabelece um histórico formal das decisões tomadas durante o projeto |
| Estabelecer um processo obrigatório de code review via Pull Request | Garante que ao menos um integrante revise cada alteração antes da integração, aumentando a detecção de erros e promovendo padronização do código |
| Criar e manter uma Definition of Done (DoD) para o projeto | Define critérios claros de conclusão para cada funcionalidade (testes passando, código revisado, critérios de aceite atendidos), evitando entregas parciais e aumentando a confiabilidade das versões |
