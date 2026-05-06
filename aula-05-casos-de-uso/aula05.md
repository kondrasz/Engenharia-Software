# 📚 Exercício Prático: Sistema de Biblioteca Digital

Este documento detalha a modelagem UML, a especificação de casos de uso e a implementação técnica de um sistema de biblioteca digital[cite: 1].

---

## 🎨 Parte 1: Diagrama de Caso de Uso

O diagrama foi estruturado para representar as interações entre os usuários e os sistemas externos, delimitados pelo escopo da Biblioteca Digital[cite: 1]. Você pode visualizar a estrutura no arquivo `diagrama-casos-de-uso.png`.

- **Atores:** Leitor, Bibliotecário e Sistema de Pagamento[cite: 1].
- **Casos de Uso Principais:** Buscar livro, Emprestar livro, Devolver livro, Renovar empréstimo e Cadastrar usuário[cite: 1].
- **Relacionamentos:**
  - **<<include>>:** O caso de uso "Emprestar livro" sempre inclui a funcionalidade de "Verificar disponibilidade"[cite: 1].
  - **<<extend>>:** O caso de uso "Devolver livro" pode ser estendido para "Aplicar multa" caso haja atraso[cite: 1].

---

## 📋 Parte 2: Especificação de Caso de Uso

### UC-02: Emprestar Livro

- **Ator Principal:** Leitor[cite: 1].
- **Pré-condições:** O leitor deve estar cadastrado no sistema e o livro deve constar no catálogo[cite: 1].
- **Fluxo Principal:**
  1. O Leitor solicita o empréstimo de um livro específico[cite: 1].
  2. O sistema verifica obrigatoriamente a disponibilidade do item (<<include>>)[cite: 1].
  3. O sistema registra o empréstimo, associa ao leitor e define o prazo[cite: 1].
- **Fluxo de Exceção:**
  - Livro já emprestado: O sistema informa a indisponibilidade[cite: 1].
  - Leitor com bloqueio: O sistema impede o empréstimo por pendências[cite: 1].
- **Pós-condições:** O livro é marcado como indisponível e o registro de empréstimo é gerado[cite: 1].

---

## 💻 Parte 3: Implementação em Python

Abaixo, a implementação funcional dos Casos de Uso (UCs) utilizando listas e dicionários[cite: 1]:

```python
# ============================================================
# 🏛️ SISTEMA DE BIBLIOTECA DIGITAL — Biblioteca FIAP
# Cada seção representa um Caso de Uso (UC)
# ============================================================

# 📦 DADOS DO SISTEMA (Simulação de Banco de Dados)
catalogo = [
    {"titulo": "Clean Code",            "autor": "Robert C. Martin", "disponivel": True},
    {"titulo": "The Pragmatic Programmer", "autor": "Hunt & Thomas", "disponivel": True},
    {"titulo": "Design Patterns",       "autor": "Gang of Four",     "disponivel": True},
]
emprestimos = []

# ------------------------------------------------------------
# UC-01: LISTAR CATÁLOGO
# ------------------------------------------------------------
print("📚 Catálogo disponível:")
for livro in catalogo:
    status = "✅" if livro["disponivel"] else "❌"
    print(f"  {status} {livro['titulo']} — {livro['autor']}")

# ------------------------------------------------------------
# UC-02: BUSCAR LIVRO
# ------------------------------------------------------------
print("\n🔍 Buscando livro...")
busca = "clean"
for livro in catalogo:
    if busca.lower() in livro["titulo"].lower(): # Busca case-insensitive[cite: 1]
        print(f"  ✨ Resultado: {livro['titulo']} ({livro['autor']})")

# ------------------------------------------------------------
# UC-03: EMPRESTAR LIVRO (Com <<include>> de Disponibilidade)
# ------------------------------------------------------------
print("\n📌 Iniciando Empréstimo:")
leitor = "Ana Silva"
titulo = "Clean Code"

# Busca o livro no catálogo
livro_alvo = next((l for l in catalogo if l["titulo"] == titulo), None)

if livro_alvo is None:
    print("  ❌ Erro: Livro não localizado.")
elif not livro_alvo["disponivel"]: # Fluxo de exceção[cite: 1]
    print(f"  ⚠️ Alerta: '{titulo}' já está emprestado.")
else:
    # Fluxo principal
    livro_alvo["disponivel"] = False
    emprestimos.append({"leitor": leitor, "livro": titulo})
    print(f"  ✅ Sucesso: '{titulo}' emprestado para {leitor}!")

# ------------------------------------------------------------
# UC-04: DEVOLVER LIVRO (Com <<extend>> de Multa)
# ------------------------------------------------------------
print("\n🔄 Processando Devolução:")
leitor_dev = "Ana Silva"
livro_dev = "Clean Code"
atrasado = True # Gatilho para o <<extend>>[cite: 1]

# Localiza o registro de empréstimo
registro = next((e for e in emprestimos if e["leitor"] == leitor_dev and e["livro"] == livro_dev), None)

if registro:
```
