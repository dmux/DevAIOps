"""
Exemplo de código Python com vulnerabilidade de segurança (execução de código arbitrário).
NÃO UTILIZAR EM PRODUÇÃO!
"""
def run_user_code(user_code: str):
    """Executa código Python fornecido pelo usuário (vulnerável a ataques)."""
    exec(user_code)  # Vulnerabilidade: permite execução arbitrária

if __name__ == "__main__":
    code = input("Digite um código Python para executar: ")
    run_user_code(code)
