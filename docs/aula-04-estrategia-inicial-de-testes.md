# Estratégia Inicial de Testes – LocalEats

## 1. Funcionalidades
- Busca de Restaurantes
- Visualização de Cardápio e Avaliações
- Sistema de Favoritos
- Recomendações Personalizadas
- Compartilhamento de Experiências
- Sincronização Web/Mobile

---

## 2. Níveis de Teste

### Funcionalidade: Busca de Restaurantes
- **Unitário:** validar cálculo de distância por geolocalização e lógica dos filtros de preço
- **Integração:** verificar comunicação entre frontend, API de busca e banco de dados
- **Sistema:** usuário aplica filtros, visualiza resultados e seleciona um restaurante
- **Aceitação:** usuário encontra restaurante adequado ao seu gosto e orçamento rapidamente

### Funcionalidade: Visualização de Cardápio e Avaliações
- **Unitário:** validar renderização correta de imagens e formatação de texto
- **Integração:** verificar conexão com serviço de storage (CDN) para carregamento de fotos
- **Sistema:** usuário acessa perfil do restaurante, visualiza fotos, cardápio e avaliações existentes
- **Aceitação:** usuário consegue tomar decisão de visita baseada nas informações apresentadas

### Funcionalidade: Sistema de Favoritos
- **Unitário:** validar alternância de estado do botão favorito (ativo/inativo)
- **Integração:** verificar persistência correta do ID do restaurante na lista do usuário no banco
- **Sistema:** usuário favorita local no app e visualiza o mesmo salvo na versão web
- **Aceitação:** usuário consegue salvar locais de interesse para consulta futura

### Funcionalidade: Recomendações Personalizadas
- **Unitário:** validar algoritmo de sugestão baseado em histórico de interações
- **Integração:** verificar fluxo entre módulo de favoritos e módulo de recomendações
- **Sistema:** usuário recebe sugestões relevantes na tela inicial após interações anteriores
- **Aceitação:** usuário percebe valor nas recomendações sem necessidade de configuração manual

### Funcionalidade: Compartilhamento de Experiências
- **Unitário:** validar limites de caracteres, caracteres especiais e sistema de notas
- **Integração:** verificar envio correto da avaliação e associação com ID do restaurante e usuário
- **Sistema:** usuário escreve avaliação, atribui nota, envia e visualiza publicação
- **Aceitação:** usuário compartilha experiência e contribui para decisão de outros usuários

### Funcionalidade: Sincronização Web/Mobile
- **Unitário:** validar consistência de dados entre versões da aplicação
- **Integração:** verificar contratos de API entre clientes mobile/web e backend
- **Sistema:** usuário alterna entre dispositivos e mantém dados íntegros em ambos
- **Aceitação:** usuário tem experiência consistente independente da plataforma utilizada

---

## 3. Prioridades e Riscos

**Alta prioridade:**
- Busca de Restaurantes → sem busca funcional o propósito central do sistema é perdido
- Visualização de Cardápio e Avaliações → informações incorretas ou indisponíveis quebram confiança
- Sincronização Web/Mobile → inconsistências geram percepção de sistema quebrado

**Justificativa:**
Falhas nessas áreas impedem o uso da plataforma ou geram dano reputacional severo. A busca é a porta de entrada; sem resultados corretos o usuário abandona imediatamente. As avaliações que desaparecem (problema relatado) minam a credibilidade do sistema. A inconsistência entre plataformas foi explicitamente citada como problema real pela associação de comerciantes.

**Média prioridade:**
- Compartilhamento de Experiências → não bloqueia descoberta, mas reduz engajamento
- Recomendações Personalizadas → diferencial importante para retenção, mas usuário pode navegar manualmente

**Baixa prioridade:**
- Sistema de Favoritos → não impede uso principal do sistema

**Justificativa:**
Favoritos é funcionalidade complementar. O usuário pode encontrar restaurantes e visualizar informações mesmo sem salvar preferências. O impacto de uma falha aqui é limitado à conveniência, não à operação essencial da plataforma.

---

## 4. Pirâmide de Testes

- **Maior foco:** Testes Unitários
- **Médio foco:** Testes de Integração / API
- **Menor foco:** Testes End-to-End (UI)

**Justificativa:**
Concentramos maior quantidade na base (unitários) pois são baratos, rápidos e previnem regressões em lógicas críticas como filtros de busca e ordenação de avaliações. O foco médio em integração se justifica pela necessidade de garantir consistência entre web e mobile via contratos de API — problema real relatado no contexto. Menor foco em E2E devido ao alto custo de manutenção e execução lenta, reservando esses testes apenas para fluxos críticos de negócio que geram prejuízo direto se falharem.

---

## 5. Testes em Produção

- **Uso de:** Feature Flags e Monitoramento Real de Usuários (RUM)
- **Aplicar em:** Lançamentos graduais de novas funcionalidades e diagnóstico de performance

**Justificativa:**
O sistema já está em produção com usuários reais e enfrenta problemas como lentidão em horários de pico e falhas em determinados smartphones. Feature flags permitem ativar correções ou novas features para grupos reduzidos, mitigando riscos de impacto generalizado. O monitoramento real é essencial pois nenhum ambiente de staging replica condições reais de uso (5.000 usuários simultâneos, conexões móveis instáveis). A exceção são transações financeiras ou exclusão de dados — estas jamais devem ser testadas em produção.
