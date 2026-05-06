# 🏋️ EXERCÍCIO PRÁTICO — Hands-on no Google Colab / VS Code

## 🎯 Missão: Validador de Requisitos para um App de Academia

Você foi contratado para desenvolver o sistema **GymTrack** — um app para academias acompanharem treinos de alunos.

---

## Parte 1 — Classificação

Liste 3 RFs e 3 RNFs para o GymTrack. Use a estrutura: `RF/RNF: O sistema deve [verbo] + [o quê/como]`.

### Requisitos Funcionais (RF)

- **RF01:** O sistema deve permitir que o usuário registre um novo treino diário.
- **RF02:** O sistema deve exibir o histórico de treinos realizados na última semana.
- **RF03:** O sistema deve calcular o volume total de peso levantado por exercício.

### Requisitos Não-Funcionais (RNF)

- **RNF01:** O sistema deve sincronizar os dados offline com o servidor em menos de 3 segundos após reconectar à internet (Desempenho).
- **RNF02:** O sistema deve criptografar as senhas e dados sensíveis dos alunos (Segurança).
- **RNF03:** O sistema deve funcionar perfeitamente nas plataformas Android e iOS (Portabilidade/Compatibilidade).

---

## Parte 2 — Implementação (Python)

Abaixo está o código do validador desenvolvido para testar as regras de negócio:

```python
import time

print("🏋️ GymTrack — Validador de Treino")
print("=" * 40)

# --- DADOS DO TREINO ---
exercicio = "Supino Reto"
peso_kg = 80
repeticoes = 10

# RF01 — Validação do nome do exercício (não pode ser vazio)
if exercicio != "":
    print(f"✅ [RF01] Exercício válido: {exercicio}")
else:
    print("❌ [RF01] Exercício inválido: não pode ser vazio.")

# RF02 — Validação do peso (1 a 300 kg)
if 1 <= peso_kg <= 300:
    print(f"✅ [RF02] Peso válido: {peso_kg}kg")
else:
    print("❌ [RF02] Peso inválido: deve estar entre 1 e 300 kg.")

# RF03 — Validação das repetições (1 a 50)
if 1 <= repeticoes <= 50:
    print(f"✅ [RF03] Repetições válidas: {repeticoes}")
else:
    print("❌ [RF03] Repetições inválidas: deve estar entre 1 e 50.")

# RNF01 — Validação de Performance (Tempo < 200ms)
inicio = time.time()

# Simula o registro no banco de dados
time.sleep(0.05)
print(f"\n✅ Série registrada: {exercicio} | {peso_kg}kg x {repeticoes} reps")

fim = time.time()
tempo_ms = (fim - inicio) * 1000

if tempo_ms < 200:
    print(f"✅ [RNF01] Tempo de registro: {tempo_ms:.0f}ms ← dentro do limite!")
else:
    print(f"❌ [RNF01] Lento demais: {tempo_ms:.0f}ms ← limite é 200ms")


```

---

## Parte 3 — Reflexão

**1. Qual a diferença entre RF e RNF que você percebeu na prática?**
Na prática, os RFs foram os blocos de lógica de negócio e validação que garantiam o funcionamento da regra (peso, repetições, nome)[cite: 1]. Já o RNF mediu o "como" a funcionalidade foi executada, focando em avaliar a performance e o tempo de resposta, sem alterar o dado em si[cite: 1].

**2. O que aconteceria se esquecêssemos o RNF de performance?**
O aplicativo poderia salvar os dados corretamente, mas o aluno teria que esperar vários segundos na academia para registrar uma simples série, gerando frustração e abandono do uso do app[cite: 1].

**3. Cite 1 RNF que o GymTrack deveria ter mas que você não implementou:**

- **Usabilidade:** O sistema deve possuir botões de incremento de carga grandes o suficiente para serem clicados facilmente na tela do celular durante o treino[cite: 1].
- **Confiabilidade:** O sistema deve estar disponível 99,9% do tempo para que o aluno nunca fique sem acesso à ficha de treino[cite: 1].
