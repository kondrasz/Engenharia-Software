import re


def cadastro_usuario(
    email: str, senha: str, email_ja_existe: bool, confirmou_email: bool
) -> str:
    """
    Implementação do fluxo de Cadastro e Aprovação.
    """

    # 1. Validar se email tem formato correto (Regex simples)
    padrao_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(padrao_email, email):
        return "Erro: Formato de e-mail inválido."

    # 2. Verificar se email já está cadastrado
    if email_ja_existe:
        return "Erro: Este e-mail já está cadastrado no sistema."

    # 3. Criar conta (Simulação de persistência)
    # 4. Enviar e-mail de confirmação
    print(f"Sistema: Conta criada para {email}. E-mail de confirmação enviado!")

    # 5. Aguardar/Verificar confirmação
    if not confirmou_email:
        return "Aviso: O link de confirmação expirou ou não foi clicado."

    # 6. Liberar acesso
    return f"Sucesso: Acesso liberado para o usuário {email}!"


# --- Seção de Testes ---
print(
    f"Teste 1 (Sucesso): {cadastro_usuario('joao@email.com', 'senha123', False, True)}"
)
print("-" * 30)
print(
    f"Teste 2 (Inválido): {cadastro_usuario('email-invalido', 'senha123', False, True)}"
)
print("-" * 30)
print(
    f"Teste 3 (Duplicado): {cadastro_usuario('joao@email.com', 'senha123', True, True)}"
)
