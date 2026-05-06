import time

print("🏋️ GymTrack — Validador de Treino")
print("=" * 40)

# --- DADOS DO TREINO  ---
exercicio = "Supino Reto"
peso_kg = 80
repeticoes = 10

# -------------------------------------------------------
# RF01 — O sistema deve validar o nome do exercício
# -------------------------------------------------------
if exercicio != "":
    print(f"✅ [RF01] Exercício válido: {exercicio}")
else:
    print("❌ [RF01] Exercício inválido: não pode ser vazio.")

# -------------------------------------------------------
# RF02 — O peso deve estar entre 1 e 300 kg
# -------------------------------------------------------
if 1 <= peso_kg <= 300:
    print(f"✅ [RF02] Peso válido: {peso_kg}kg")
else:
    print("❌ [RF02] Peso inválido: deve estar entre 1 e 300 kg.")

# -------------------------------------------------------
# RF03 — As repetições devem estar entre 1 e 50
# -------------------------------------------------------
if 1 <= repeticoes <= 50:
    print(f"✅ [RF03] Repetições válidas: {repeticoes}")
else:
    print("❌ [RF03] Repetições inválidas: deve estar entre 1 e 50.")

# -------------------------------------------------------
# RNF01 — O registro deve ocorrer em menos de 200ms
# -------------------------------------------------------
inicio = time.time()

# Simula o registro no banco de dados
time.sleep(0.05)
print(f"✅ Série registrada: {exercicio} | {peso_kg}kg x {repeticoes} reps")

fim = time.time()
tempo_ms = (fim - inicio) * 1000

if tempo_ms < 200:
    print(f"✅ [RNF01] Tempo de registro: {tempo_ms:.0f}ms ← dentro do limite!")
else:
    print(f"❌ [RNF01] Lento demais: {tempo_ms:.0f}ms ← limite é 200ms")
