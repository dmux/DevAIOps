# Instruções de Geração de Testes do Copilot (Python)

- Todas as dependências necessárias para rodar os testes já estão instaladas no ambiente do projeto.
- Todos os testes devem ser escritos exclusivamente com **pytest** e **pytest-mock**. Não utilize `unittest`.
- Garanta cobertura mínima de **95%** do código testado (use `pytest-cov` para medir).
- Gere testes para todos os novos fluxos e alterações de código.
- Mocke serviços externos (ex: AWS, APIs externas) e acesso ao filesystem obrigatoriamente, nunca interaja com recursos reais.
- Certifique-se de que os testes sejam claros, concisos e fáceis de manter.
- Inclua casos positivos e negativos para cada função ou método.
- Inclua testes específicos para tratamento de exceções, garantindo que erros sejam tratados corretamente e exceções esperadas sejam lançadas.
- Forneça nomes de teste e comentários significativos para clareza.
- Os testes devem ser determinísticos e não depender de estado externo.
- Verifique se todos os testes passam e a cobertura está acima de 95% antes de submeter o código para revisão.

## Como executar os testes (Linux, macOS e Windows)

### Linux/macOS

```bash
export PYTHONPATH=${workspaceFolder}
uv run pytest -vvv --cov
```

Se não houver `uv`, ative o ambiente virtual local:

```bash
export PYTHONPATH=${workspaceFolder}
source .venv/bin/activate
pytest -vvv --cov
```

### Windows (cmd)

```cmd
set PYTHONPATH=${workspaceFolder}
uv run pytest -vvv --cov
```

Se não houver `uv`, ative o ambiente virtual local:

```cmd
set PYTHONPATH=${workspaceFolder}
.venv\Scripts\activate
pytest -vvv --cov
```

> Estas instruções são aplicadas automaticamente à geração de testes neste repositório.
