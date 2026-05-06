# 🏦 Exercício Prático: Sistema de Transferência Nubank

Este projeto consiste na modelagem e implementação de um fluxo de transferência bancária, integrando conceitos de **Diagrama de Sequência (UML)** e **Programação Orientada a Objetos (POO)**.

---

## 🎨 Parte 1: Diagrama de Sequência (Miro)

O diagrama de sequência modela a interação temporal entre quatro participantes principais para completar uma transação de "Cenário Feliz" e tratamento de exceção (saldo insuficiente).

- **Participantes:**
  - **Usuário:** Ator que inicia a solicitação.
  - **App Nubank:** Interface que coleta dados e exibe feedbacks.
  - **Servidor Nubank:** Camada de lógica de negócio e processamento.
  - **Banco de Dados:** Camada de persistência onde o saldo é consultado e atualizado.

- **Lógica Condicional (ALT):**
  - O diagrama utiliza um fragmento combinado para decidir entre a **aprovação** (débito realizado) ou a **recusa** (saldo insuficiente) da operação.

---

## 📋 Parte 2: Especificação Técnica

O sistema foi desenhado seguindo o padrão de responsabilidades delimitadas:

1. **Solicitação:** O App não processa dinheiro, apenas envia a requisição para o Servidor.
2. **Validação:** O Servidor consulta o Banco de Dados para verificar a viabilidade da transação.
3. **Persistência:** O Banco de Dados é o único componente autorizado a alterar os valores monetários.
4. **Resposta:** O status da operação (Aprovado/Recusado) retorna em cascata até o usuário final.

---

## 💻 Parte 3: Implementação em Python

A implementação utiliza classes para representar cada participante do diagrama, garantindo o encapsulamento e a organização do código.

```python
# ============================================================
# 🏦 SIMULAÇÃO DE SISTEMA BANCÁRIO — NUBANK
# ============================================================

class BancoDeDados:
    def __init__(self):
        self.saldos = {"user_123": 500.0}

    def verificar_saldo(self, user_id: str) -> float:
        return self.saldos.get(user_id, 0.0)

    def debitar(self, user_id: str, valor: float) -> bool:
        if self.verificar_saldo(user_id) >= valor:
            self.saldos[user_id] -= valor
            return True
        return False

class ServidorNubank:
    def __init__(self):
        self.banco = BancoDeDados()

    def processar_transferencia(self, user_id: str, valor: float) -> dict:
        if self.banco.debitar(user_id, valor):
            saldo_atual = self.banco.verificar_saldo(user_id)
            return {"status": "aprovado", "saldo_restante": saldo_atual}
        return {"status": "recusado", "motivo": "saldo insuficiente"}

class AppNubank:
    def __init__(self):
        self.servidor = ServidorNubank()

    def transferir(self, user_id: str, valor: float):
        print(f"[APP] Iniciando transferência de R$ {valor:.2f}...")
        res = self.servidor.processar_transferencia(user_id, valor)

        if res["status"] == "aprovado":
            print(f"[APP] ✅ Transferência aprovada! Saldo: R$ {res['saldo_restante']:.2f}")
        else:
            print(f"[APP] ❌ Transferência recusada: {res['motivo']}")

# --- EXECUÇÃO DE TESTES ---
app = AppNubank()
app.transferir("user_123", 200.0) # Teste de Sucesso
app.transferir("user_123", 500.0) # Teste de Erro
```
