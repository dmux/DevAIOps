# DevAIOps: Automação e Boas Práticas com Copilot no VS Code

Este repositório demonstra como adotar automações inteligentes com GitHub Copilot no Visual Studio Code, promovendo padrões de qualidade, segurança e colaboração para projetos Python e open source.

## Objetivo

Facilitar a adoção de práticas modernas de desenvolvimento, revisão, testes e documentação automatizada, utilizando Copilot e integrações no VS Code.

## Principais Funcionalidades

- **Exemplos de código limpo e code smells** para aprendizado e revisão.
- **Diretrizes automatizadas** para mensagens de commit, pull requests, revisões e geração de testes.
- **Configuração de ambiente Python moderna** (PEP 621, pyproject.toml, dependências de dev).
- **Scripts e exemplos de segurança** (incluindo exemplos de vulnerabilidades para análise com ferramentas como Bandit).

## Estrutura do Projeto

```
.
├── example_file_manager.py         # Exemplo de código limpo e seguro
├── pyproject.toml                 # Configuração do projeto Python
├── samples/
│   ├── code_smells_example.py     # Exemplo de code smells para revisão
│   ├── example_file_manager.py    # Outro exemplo de boas práticas
│   └── vulnerable_exec.py         # Exemplo de vulnerabilidade (NÃO usar em produção)
├── .github/
│   └── instructions/              # Instruções automatizadas para Copilot
│       ├── commit-message.instructions.md
│       ├── pull-request-description.instructions.md
│       ├── review.instructions.md
│       └── test-generation.instructions.md
└── README.md
```

## Como Usar

1. **Abra o projeto no VS Code** com a extensão GitHub Copilot ativada.
2. **Siga as instruções automáticas**: ao criar commits, pull requests, revisões ou testes, Copilot irá sugerir padrões e templates baseados nos arquivos `.github/instructions/`.
3. **Analise os exemplos** em `samples/` para identificar boas práticas e problemas comuns (code smells, vulnerabilidades).
4. **Utilize as ferramentas de lint, formatação e segurança** já configuradas no `pyproject.toml` (black, flake8, isort, mypy, bandit).

## Diretrizes Automatizadas

- **Commits**: Siga Conventional Commits com gitmoji e mensagens claras.
- **Pull Requests**: Use descrições objetivas, contexto, checklist e instruções de validação.
- **Revisão de Código**: Adote tópicos construtivos, destaque problemas e sugira melhorias.
- **Testes**: Gere testes claros, com mocks e casos positivos/negativos.

As instruções completas estão em `.github/instructions/`.

## Exemplos de Código

- `example_file_manager.py`: Gerenciamento seguro de arquivos, tratamento de exceções, uso de tipagem.
- `samples/code_smells_example.py`: Código propositalmente ruim para treinar revisões.
- `samples/vulnerable_exec.py`: Demonstração de vulnerabilidade via `exec` (NÃO use em produção).

## Ambiente de Desenvolvimento

- Python 3.12+
- Dependências de desenvolvimento: black, flake8, isort, mypy, bandit
- Instale com:

  ```sh
  pip install -r requirements.txt  # ou use pyproject.toml com poetry/pdm/uv
  ```

## Segurança

- O projeto inclui exemplos inseguros apenas para fins educacionais.
- Use ferramentas como Bandit para análise estática de segurança.

## Contribuição

- Siga as diretrizes automatizadas para garantir qualidade e padronização.
- Revise exemplos e contribua com novos fluxos de automação e boas práticas.

## Licença

MIT

---

Este README foi gerado para maximizar a adoção de automações Copilot e servir como referência para a comunidade open source.
