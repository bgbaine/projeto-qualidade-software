| Problema identificado | Atributo de qualidade afetado | Justificativa técnica |
| :---------------- | :------: | ----: |
| Lentidão em horários de pico | Desempenho | Tempo de resposta elevado prejudica a experiência do usuário |
| Homepage visível sem autenticação por alguns segundos | Segurança | Exposição indevida de conteúdo antes da validação de acesso indica falha no controle de autenticação |
| Política de senha fraca e sem confirmação | Segurança | Senhas simples e ausência de confirmação aumentam o risco de contas comprometidas |
| Ausência de verificação de e-mail no cadastro | Segurança | Permite criação de contas com e-mails inválidos, reduzindo confiabilidade e abrindo margem para abusos |
| Armazenamento de dados sensíveis no localStorage sem validação | Segurança | Permite manipulação direta pelo usuário, caracterizando falhas como IDOR e controle de acesso inadequado |
| Uso de ID sequencial simples ao invés de UUID | Segurança | Facilita enumeração de usuários e exploração de vulnerabilidades como acesso indevido |
| Problemas de responsividade | Usabilidade | Interface não adaptável prejudica a navegação em diferentes dispositivos |
| Barra de pesquisa não funcional e sem suporte à tecla Enter | Usabilidade | Funcionalidade essencial quebrada compromete a eficiência e a experiência do usuário |
| Interfaces confusas e experiência do usuário pobre | Usabilidade | Dificulta a interação do usuário e reduz a eficiência no uso do sistema |