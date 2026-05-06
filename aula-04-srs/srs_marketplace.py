# ==========================================
# PARTE 2 — Validador de Requisitos
# ==========================================


class RequisitoFuncional:
    def __init__(self, id, nome, descricao, pre_condicao=""):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.pre_condicao = pre_condicao


def validar_requisito(rf: RequisitoFuncional) -> dict:
    """
    Valida se um requisito funcional segue as boas práticas.
    """
    resultados = {
        "tamanho_maior_20_chars": len(rf.descricao) > 20,
        "tem_pre_condicao": rf.pre_condicao.strip() != "",
        "tem_criterio_mensuravel": any(char.isdigit() for char in rf.descricao),
    }
    return resultados


# Testando a validação com o RF-001
rf1 = RequisitoFuncional(
    id="RF-001",
    nome="Cadastro de Produto",
    descricao="O aluno vendedor deve poder cadastrar até 10 produtos com título, preço e 1 foto.",
    pre_condicao="Estar logado com e-mail @fiap.com.br",
)

print(f"Validando {rf1.id}:")
validacao = validar_requisito(rf1)
for regra, passou in validacao.items():
    print(f"[{'x' if passou else ' '}] {regra}")


# ==========================================
# PARTE 3 — Desafio Extra (Gerador Markdown)
# ==========================================


def exportar_markdown(rfs, rnfs):
    """Gera o texto em Markdown pronto pro Notion/Confluence"""
    md = "# SRS - FIAP Marketplace\n\n## Requisitos Funcionais\n"
    for rf in rfs:
        md += f"- **{rf.id}**: {rf.descricao}\n"

    md += "\n## Requisitos Não-Funcionais\n"
    for rnf in rnfs:
        md += f"- **{rnf['id']}**: {rnf['descricao']}\n"
    return md


# Testando o export do desafio 3
lista_rfs = [rf1]
lista_rnfs = [
    {"id": "RNF-001", "descricao": "O marketplace deve garantir 99.9% de uptime."}
]

print("\n" + "=" * 40)
print("Output do Gerador Markdown:\n")
print(exportar_markdown(lista_rfs, lista_rnfs))
