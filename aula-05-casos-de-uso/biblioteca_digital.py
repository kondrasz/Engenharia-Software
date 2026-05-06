# ============================================================
# 🏛️ SISTEMA DE BIBLIOTECA DIGITAL — Biblioteca FIAP
# Cada seção = um Caso de Uso do diagrama UML
# ============================================================

# ----------------------------
# 📦 DADOS DO SISTEMA
# ----------------------------
catalogo = [
    {"titulo": "Clean Code", "autor": "Robert C. Martin", "disponivel": True},
    {
        "titulo": "The Pragmatic Programmer",
        "autor": "Hunt & Thomas",
        "disponivel": True,
    },
    {"titulo": "Design Patterns", "autor": "Gang of Four", "disponivel": True},
]
emprestimos = []  # lista de {"leitor": ..., "livro": ...}

# ============================================================
# UC-01: LISTAR CATÁLOGO
# Ator: Leitor
# ============================================================
print("📚 Catálogo disponível:")
for livro in catalogo:
    status = "✅" if livro["disponivel"] else "❌"
    print(f"  {status} {livro['titulo']} — {livro['autor']}")

# ============================================================
# UC-02: BUSCAR LIVRO
# Ator: Leitor
# ============================================================
print("\n🔍 Buscando livro...")
busca = "clean"  # Simulação de entrada do usuário

encontrados = 0
for livro in catalogo:
    # Ignora maiúsculas/minúsculas na busca
    if busca.lower() in livro["titulo"].lower():
        status = "✅" if livro["disponivel"] else "❌"
        print(f"  Encontrado: {status} {livro['titulo']} ({livro['autor']})")
        encontrados += 1

if encontrados == 0:
    print(f"  ❌ Nenhum livro encontrado com o termo '{busca}'.")

# ============================================================
# UC-03: EMPRESTAR LIVRO
# Ator: Leitor | <<include>> UC-04 Verificar Disponibilidade
# ============================================================
print("\n📌 Iniciando Empréstimo:")
leitor = "Ana Silva"
titulo_alvo = "Clean Code"

livro_encontrado = None
for livro in catalogo:
    if livro["titulo"] == titulo_alvo:
        livro_encontrado = livro
        break

# Lógica de validação e fluxos de exceção
if livro_encontrado is None:
    print("  ❌ Erro: Livro não existe no catálogo.")
elif not livro_encontrado["disponivel"]:
    print(f"  ⚠️ Fluxo de Exceção: O livro '{titulo_alvo}' já está ocupado.")
else:
    # Fluxo Principal
    livro_encontrado["disponivel"] = False
    emprestimos.append({"leitor": leitor, "livro": titulo_alvo})
    print(f"  ✅ Sucesso: '{titulo_alvo}' emprestado para {leitor}!")

# ============================================================
# UC-04: DEVOLVER LIVRO
# Ator: Leitor | <<extend>> UC-05 Aplicar Multa
# ============================================================
print("\n🔄 Processando Devolução:")
leitor_devolvendo = "Ana Silva"
titulo_devolvendo = "Clean Code"
atrasado = True  # Simulação para testar o <<extend>>

registro_emprestimo = None
for emp in emprestimos:
    if emp["leitor"] == leitor_devolvendo and emp["livro"] == titulo_devolvendo:
        registro_emprestimo = emp
        break

if registro_emprestimo:
    # 1. Atualiza disponibilidade no catálogo
    for livro in catalogo:
        if livro["titulo"] == titulo_devolvendo:
            livro["disponivel"] = True
            break

    # 2. Remove dos empréstimos ativos
    emprestimos.remove(registro_emprestimo)
    print(f"  ✅ Livro '{titulo_devolvendo}' devolvido por {leitor_devolvendo}.")

    # <<extend>> UC-05: Aplicar Multa
    if atrasado:
        print("  📋 [EXTEND] Condição de atraso detectada: Multa aplicada!")
else:
    print(
        f"  ❌ Erro: Não há registro de empréstimo de '{titulo_devolvendo}' para {leitor_devolvendo}."
    )

# ============================================================
# 🔎 ESTADO FINAL DO SISTEMA
# ============================================================
print("\n" + "=" * 40)
print("📖 Relatório Final do Sistema:")
print(f"Catálogo Atualizado: {catalogo}")
print(f"Empréstimos Ativos: {emprestimos}")
print("=" * 40)
