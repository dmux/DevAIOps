"""
Exemplo de programa Python para validar as instruções de testes, revisão e PR do projeto.
Este módulo cobre casos positivos, negativos, exceções, uso de mocks e segue padrões de estilo.
"""
import os
from typing import Optional

class FileManager:
    """Gerencia operações seguras de leitura de arquivos."""
    def __init__(self, base_path: str):
        self.base_path = base_path

    def read_file(self, filename: str) -> Optional[str]:
        """Lê o conteúdo de um arquivo, retorna None se não existir."""
        path = os.path.join(self.base_path, filename)
        if not os.path.exists(path):
            return None
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    def file_exists(self, filename: str) -> bool:
        """Verifica se o arquivo existe."""
        return os.path.exists(os.path.join(self.base_path, filename))

    def count_lines(self, filename: str) -> int:
        """Conta o número de linhas de um arquivo. Lança exceção se não existir."""
        path = os.path.join(self.base_path, filename)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Arquivo não encontrado: {filename}")
        with open(path, 'r', encoding='utf-8') as f:
            return sum(1 for _ in f)

# Exemplo de função que acessa serviço externo (deve ser mockada em testes)
def get_env_variable(var_name: str) -> str:
    """Obtém variável de ambiente, lança exceção se não existir."""
    value = os.getenv(var_name)
    if value is None:
        raise EnvironmentError(f"Variável de ambiente não encontrada: {var_name}")
    return value

# Exemplo de uso
if __name__ == "__main__":
    fm = FileManager('.')
    print(fm.read_file('README.md'))
    print(fm.file_exists('README.md'))
    try:
        print(fm.count_lines('README.md'))
    except FileNotFoundError as e:
        print(e)
    try:
        print(get_env_variable('HOME'))
    except EnvironmentError as e:
        print(e)
