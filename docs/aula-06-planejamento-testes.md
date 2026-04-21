Aula 6 – Planejamento e Execução de Testes

Disciplina: Qualidade de Software
Projeto: LocalEats
Integrantes do grupo:

Bernardo
Bryan
Filipe
Pedro



1. Plano de Testes
1.1 Objetivo
Validar as funcionalidades de login e busca de restaurantes do LocalEats, verificando se o comportamento do sistema corresponde ao esperado tanto em cenários de uso normal quanto em situações de erro. A escolha dessas funcionalidades se justifica pelos problemas já mapeados nas PBLs anteriores: falha na busca com a tecla Enter, política de senha fraca e ausência de feedback adequado ao usuário.

1.2 Escopo
O que será testado:

Login com credenciais válidas e inválidas
Busca de restaurantes por texto
Busca de restaurantes por filtro de categoria
Comportamento da interface em entradas inesperadas

O que não será testado:

Integração com sistemas de pagamento
Funcionalidades de avaliação e favoritos
Performance sob carga (testada separadamente, conforme PBL 3)
Aplicativo mobile


1.3 Funcionalidades Selecionadas

Login e cadastro
Busca de restaurantes (texto livre e filtros por categoria)


1.4 Estratégia de Testes
Testes manuais funcionais (caixa-preta), executados diretamente no sistema em https://local-eats-unisenac.vercel.app/. Os cenários foram definidos previamente com base nos problemas identificados nas PBLs 1 e 5. Onde o sistema não permitir execução real, os resultados serão simulados com base no comportamento observado da interface.

Tipo de teste: funcional
Abordagem: manual, baseada em casos de teste predefinidos
Critério de aprovação: comportamento do sistema corresponde ao resultado esperado descrito em cada caso


1.5 Responsáveis
NomeResponsabilidadeBernardoElaboração dos casos de teste e execução do loginBryanExecução dos testes de busca e registro de evidênciasFilipeAnálise dos resultados e redação do relatórioPedroRevisão geral e reflexão crítica

2. Casos de Teste

CT-01 – Login com credenciais válidas
Pré-condição: usuário cadastrado no sistema com e-mail fsm@email.com e senha 123. Estar na página de login.
Passos:

Acessar https://local-eats-unisenac.vercel.app/static/login.html
Inserir o e-mail fsm@email.com no campo E-mail
Inserir a senha 123 no campo Senha
Clicar no botão "Entrar"

Dados de entrada: e-mail: fsm@email.com / senha: 123
Resultado esperado: o sistema redireciona o usuário para a página principal (index.html) com os restaurantes carregados e sem exibir mensagem de erro.

CT-02 – Login com senha incorreta
Pré-condição: usuário cadastrado no sistema. Estar na página de login.
Passos:

Acessar a página de login
Inserir o e-mail fsm@email.com
Inserir a senha senhaerrada
Clicar em "Entrar"

Dados de entrada: e-mail: fsm@email.com / senha: senhaerrada
Resultado esperado: o sistema permanece na página de login e exibe uma mensagem de erro clara indicando que as credenciais são inválidas.

CT-03 – Busca por categoria com resultados
Pré-condição: usuário autenticado na página principal.
Passos:

Acessar a página principal
Clicar no filtro "Japonesa"
Observar os resultados exibidos

Dados de entrada: filtro selecionado: "Japonesa"
Resultado esperado: a lista exibe apenas restaurantes da categoria Japonesa. Nenhum restaurante de outra categoria aparece nos resultados.

CT-04 – Busca por texto com termo válido
Pré-condição: usuário autenticado na página principal.
Passos:

Clicar na barra de busca
Digitar "pizza"
Pressionar Enter ou clicar no botão de busca

Dados de entrada: termo: pizza
Resultado esperado: o sistema exibe restaurantes cujo nome ou categoria contenha o termo "pizza". A lista é atualizada de forma visível.

CT-05 – Busca com termo inexistente
Pré-condição: usuário autenticado na página principal.
Passos:

Clicar na barra de busca
Digitar "xyzabc123"
Pressionar Enter ou clicar no botão de busca

Dados de entrada: termo: xyzabc123
Resultado esperado: o sistema exibe uma mensagem informando que nenhum restaurante foi encontrado. A interface não trava nem exibe erro genérico.

CT-06 – Busca com a tecla Enter
Pré-condição: usuário autenticado na página principal.
Passos:

Clicar na barra de busca
Digitar "sushi"
Pressionar a tecla Enter (sem clicar no botão)

Dados de entrada: termo: sushi
Resultado esperado: a busca é executada e os resultados são atualizados, da mesma forma que ao clicar no botão de busca.

3. Execução dos Testes
IDResultadoEvidênciaCT-01PassouApós inserir fsm@email.com e senha 123 e clicar em "Entrar", o sistema redirecionou para index.html com a listagem de restaurantes carregada normalmente.CT-02FalhouO sistema exibiu a mensagem "Erro ocorreu" — genérica, sem indicar o motivo da falha. Não há diferenciação entre e-mail inválido e senha incorreta.CT-03PassouAo selecionar o filtro "Japonesa", a lista exibiu apenas restaurantes dessa categoria, sem itens de outras categorias.CT-04FalhouAo digitar "pizza" e pressionar Enter, nada aconteceu. Ao clicar no ícone de busca, a lista não foi atualizada — a barra de busca não apresentou resposta visível.CT-05FalhouO sistema não exibiu mensagem de ausência de resultados; a lista simplesmente ficou em branco sem nenhum feedback para o usuário.CT-06FalhouA tecla Enter não aciona a busca. Comportamento já identificado na PBL 1 como falha confirmada.

4. Análise dos Resultados

Testes executados: 6
Passaram: 2
Falharam: 4

Principais problemas encontrados:

A mensagem de erro no login é genérica ("Erro ocorreu"), sem orientar o usuário sobre o que foi preenchido incorretamente. Isso compromete a usabilidade e dificulta a recuperação de acesso.
A barra de busca por texto não funciona — nem via Enter nem via botão. A funcionalidade central do sistema está quebrada, confirmando o que já havia sido registrado na PBL 1.
A ausência de feedback para buscas sem resultados deixa o usuário sem saber se o sistema processou a requisição ou simplesmente falhou silenciosamente.
O filtro por categoria funciona corretamente e é a única forma operacional de encontrar restaurantes no momento.


5. Reflexão
O plano de testes ajudou a organizar melhor o processo?
Sim. Definir os casos antes da execução forçou a equipe a pensar nos critérios de aceitação com antecedência, o que tornou os resultados mais fáceis de avaliar. Sem isso, a tendência seria testar de forma exploratória e não registrar os resultados de maneira estruturada.
Algum problema só foi percebido durante a execução?
A mensagem genérica "Erro ocorreu" no login não havia sido detalhada nas PBLs anteriores — sabíamos que o sistema tinha problemas de feedback, mas a ausência de distinção entre tipos de erro (e-mail errado vs. senha errada) ficou clara apenas ao executar o CT-02.
O que melhorariam no processo?
Incluir casos de teste para o cadastro de novos usuários, que não foi coberto nesta rodada. Também seria útil registrar prints de cada execução como evidência formal, e não apenas descrições textuais.

6. Conclusão Geral
O sistema LocalEats apresenta qualidade inconsistente: funcionalidades secundárias como o filtro por categoria funcionam corretamente, mas a busca textual — que é o recurso central da plataforma — está completamente inoperante. O login funciona no caminho feliz, mas falha em comunicar erros de forma útil.
A execução estruturada dos testes confirmou e detalhou os problemas já mapeados nas PBLs anteriores, além de revelar novos pontos de atenção. O processo de planejar, executar e analisar em etapas separadas se mostrou mais eficaz do que testes exploratórios, pois tornou os resultados rastreáveis e as falhas reproduzíveis.
