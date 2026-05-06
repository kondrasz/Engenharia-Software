# 🎯 Exercício Prático: Fluxo de Cadastro e Aprovação

Este documento detalha a modelagem de processos via Diagrama de Atividades e a implementação técnica em Python para o sistema de registro de usuários.

---

## 🎨 Parte 1: Diagrama de Atividades (Miro)

O diagrama foi estruturado utilizando **Swimlanes** (Raias) para separar as responsabilidades entre o usuário final e o processamento automatizado do sistema.

- **Atores (Raias):**
  - **Usuário:** Responsável pelo preenchimento do formulário e interação com o e-mail de confirmação.
  - **Sistema:** Responsável pelas validações de formato, verificação de banco de dados e envio de notificações.
- **Pontos de Decisão:**
  - **[E-mail válido?]:** Verifica se o input segue o padrão `usuario@dominio.com`.
  - **[E-mail já cadastrado?]:** Consulta a existência prévia do usuário para evitar duplicidade.
- **Transições:** O fluxo é interrompido em caso de dados inválidos ou finalizado com a liberação do acesso após a confirmação.

---

## 📋 Parte 2: Especificação do Fluxo

### Fluxo de Cadastro e Validação

- **Ator Principal:** Usuário.
- **Pré-condições:** O usuário deve fornecer um e-mail válido e não possuir conta anterior.
- **Fluxo Principal:**
  1. O Usuário envia os dados de cadastro (e-mail e senha).
  2. O Sistema valida o formato do e-mail.
  3. O Sistema verifica se o e-mail já consta na base de dados.
  4. O Sistema cria o registro e envia um e-mail de confirmação.
  5. O Usuário confirma o recebimento.
  6. O Sistema altera o status do usuário para "Ativo" e libera o acesso.
- **Fluxos de Exceção:**
  - **E-mail Inválido:** O sistema retorna erro e solicita nova digitação.
  - **E-mail em Uso:** O sistema impede o cadastro e sugere recuperação de senha.
- **Pós-condições:** Usuário autenticado e com acesso total às funcionalidades do App.

---

## 💻 Parte 3: Implementação em Python

Abaixo, a implementação funcional do fluxo desenhado no Miro, utilizando expressões regulares para validação:

```python
# ============================================================
# 🚀 SISTEMA DE CADASTRO — Engenharia da Computação
# Implementação baseada no Diagrama de Atividades
# ============================================================

import re

def cadastro_usuario(email: str, senha: str, email_ja_existe: bool, confirmou_email: bool) -> str:
    """
    Simula o fluxo de validação e aprovação de um novo usuário.
    """

    # ------------------------------------------------------------
    # 1. VALIDAÇÃO DE FORMATO (Decisão 1 no Miro)
    # ------------------------------------------------------------
    padrao_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(padrao_email, email):
        return "❌ Erro: Formato de e-mail inválido."

    # ------------------------------------------------------------
    # 2. VERIFICAÇÃO DE DUPLICIDADE (Decisão 2 no Miro)
    # ------------------------------------------------------------
    if email_ja_existe:
        return "⚠️ Alerta: Este e-mail já possui uma conta ativa."

    # ------------------------------------------------------------
    # 3. CRIAÇÃO DE CONTA E CONFIRMAÇÃO (Ações do Sistema)
    # ------------------------------------------------------------
    # Simula o envio de e-mail e a espera pela ação do usuário
    if not confirmou_email:
        return "⏳ Registro Criado: Aguardando confirmação de e-mail."

    # ------------------------------------------------------------
    # 4. LIBERAÇÃO DE ACESSO (Nó Final de Sucesso)
    # ------------------------------------------------------------
    return f"✅ Sucesso: Conta de '{email}' ativada. Acesso liberado!"

# ============================================================
# 🧪 TESTES DO SISTEMA (Não apagar)
# ============================================================

print(f"Cenário 1 (Sucesso):   {cadastro_usuario('joao@email.com', 'senha123', False, True)}")
print(f"Cenário 2 (Inválido):  {cadastro_usuario('email-invalido', 'senha123', False, True)}")
print(f"Cenário 3 (Duplicado): {cadastro_usuario('joao@email.com', 'senha123', True, True)}")
```
