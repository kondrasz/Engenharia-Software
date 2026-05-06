# ============================================================
# 🏦 SIMULAÇÃO DE SISTEMA BANCÁRIO — NUBANK
# Arquitetura: App -> Servidor -> Banco de Dados
# ============================================================


# --- Célula 1: Participante "Banco de Dados" ---
class BancoDeDados:
    def __init__(self):
        # Banco de dados simulado com um usuário inicial
        self.saldos = {"user_123": 500.0}

    def verificar_saldo(self, user_id: str) -> float:
        # Retorna o saldo do usuário ou 0.0 se não existir (evita erro)
        return self.saldos.get(user_id, 0.0)

    def debitar(self, user_id: str, valor: float) -> bool:
        # Verifica se o saldo é suficiente antes de realizar a operação
        if self.verificar_saldo(user_id) >= valor:
            self.saldos[user_id] -= valor
            return True
        return False


# --- Célula 2: Participante "Servidor Nubank" ---
class ServidorNubank:
    def __init__(self):
        # O Servidor possui uma instância do Banco de Dados
        self.banco = BancoDeDados()

    def processar_transferencia(self, user_id: str, valor: float) -> dict:
        # Implementação da lógica [ALT] do diagrama de sequência
        sucesso = self.banco.debitar(user_id, valor)

        if sucesso:
            # Se debitou com sucesso, retorna o novo saldo
            saldo_atualizado = self.banco.verificar_saldo(user_id)
            return {"status": "aprovado", "saldo_restante": saldo_atualizado}
        else:
            # Caso contrário, retorna o motivo da falha
            return {"status": "recusado", "motivo": "saldo insuficiente"}


# --- Célula 3: Participante "App Nubank" ---
class AppNubank:
    def __init__(self):
        # O App se comunica com o Servidor
        self.servidor = ServidorNubank()

    def transferir(self, user_id: str, valor: float):
        print(f"[APP] Iniciando transferência de R$ {valor:.2f}...")

        # Chama o servidor para processar a solicitação
        resultado = self.servidor.processar_transferencia(user_id, valor)

        # Feedback visual para o usuário (Interação final da lifeline)
        if resultado["status"] == "aprovado":
            print(
                f"[APP] ✅ Transferência aprovada! Saldo: R$ {resultado['saldo_restante']:.2f}"
            )
        else:
            print(f"[APP] ❌ Transferência recusada: {resultado['motivo']}")


# --- Célula 4: Testes de Execução ---
# Criamos o objeto App e simulamos as transferências solicitadas
app = AppNubank()

print("=== Teste 1: Transferência dentro do saldo ===")
app.transferir("user_123", 200.0)  # Esperado: aprovado (Saldo final: 300)

print("\n=== Teste 2: Transferência acima do saldo ===")
app.transferir("user_123", 500.0)  # Esperado: recusado (Saldo insuficiente)

print("\n=== Teste 3: Múltiplas transferências ===")
app.transferir("user_123", 100.0)  # Esperado: aprovado (Saldo final: 200)
app.transferir("user_123", 250.0)  # Esperado: recusado (Saldo insuficiente)
