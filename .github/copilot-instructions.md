# Diretrizes de Revisão de Código Clean Code

Ao revisar código, siga os princípios derivados do Clean Code de Uncle Bob.

## Nomes Significativos

- Use nomes descritivos e não ambíguos.
- Evite abreviações, a menos que sejam amplamente compreendidas.
- Use nomes pronunciáveis e mantenha convenções de nomenclatura consistentes.

## Funções Pequenas

- Garanta que as funções sejam pequenas e realizem apenas uma tarefa.
- Evite argumentos de controle (flags) e efeitos colaterais.
- Cada função deve operar em um único nível de abstração.

## Princípios SOLID

- **Responsabilidade Única (SRP):** Cada classe ou função deve ter apenas um motivo para mudar. Separe responsabilidades e encapsule preocupações de forma apropriada.
- **Aberto/Fechado (OCP):** Estruture o código para ser aberto para extensão, mas fechado para modificação. Prefira abstrações e evite alterar código já testado.
- **Substituição de Liskov (LSP):** Garanta que subclasses possam ser usadas no lugar das superclasses sem causar erros ou comportamentos inesperados.
- **Segregação de Interfaces (ISP):** Prefira interfaces pequenas e específicas, evitando obrigar implementações a depender de métodos que não utilizam.
- **Inversão de Dependência (DIP):** Dependa de abstrações, não de implementações concretas. Utilize injeção de dependência sempre que possível.

## Design Patterns Genéricos Aplicáveis

- Utilize padrões de projeto reconhecidos para resolver problemas recorrentes de forma elegante e sustentável.
- Prefira padrões como Singleton, Factory, Strategy, Observer e Adapter quando apropriado ao contexto.
- Evite aplicar padrões de forma desnecessária ou excessiva (overengineering).
- Documente a escolha do padrão quando ele não for óbvio no contexto do código.

## Formatação Limpa

- Para código Python, siga o padrão PEP8 para indentação, espaçamento e organização dos blocos.
- Use indentação e espaçamento consistentes em todas as linguagens.
- Separe blocos de código com linhas em branco quando necessário para legibilidade.

## Evite Comentários

- Escreva código autoexplicativo que não exija comentários.
- Use comentários apenas para explicar lógica complexa ou APIs públicas.

## Tratamento de Erros

- Use exceções em vez de códigos de retorno.
- Evite capturar exceções genéricas.
- Falhe rápido e trate exceções em um nível superior.

## Evite Duplicação

- Extraia lógica comum em funções ou classes.
- DRY – Não se repita.

## "Code Smells" para Sinalizar

- Funções longas
- Classes grandes
- Aninhamento profundo
- Obsessão por tipos primitivos
- Listas longas de parâmetros
- Números ou strings mágicos
- Nomes inconsistentes

## Estilo de Revisão

- Mantenha um tom rigoroso, porém construtivo.
- Use tópicos (bullet points) para listar problemas.
- Forneça alternativas e sugestões de código aprimorado.
