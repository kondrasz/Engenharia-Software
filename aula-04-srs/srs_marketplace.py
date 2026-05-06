from dataclasses import dataclass, field
from typing import List
from enum import Enum


class Prioridade(Enum):
    ALTA = "Alta"
    MEDIA = "Média"
    BAIXA = "Baixa"


@dataclass
class RequisitoFuncional:
    id: str
    nome: str
    descricao: str
    prioridade: Prioridade
    ator: str
    pre_condicao: str
    pos_condicao: str


@dataclass
class RequisitoNaoFuncional:
    id: str
    categoria: str
    descricao: str
    criterio_aceitacao: str


@dataclass
class SRS:
    projeto: str
    versao: str
    descricao: str
    requisitos_funcionais: List[RequisitoFuncional] = field(default_factory=list)
    requisitos_nao_funcionais: List[RequisitoNaoFuncional] = field(default_factory=list)

    def adicionar_rf(self, req: RequisitoFuncional):
        self.requisitos_funcionais.append(req)

    def adicionar_rnf(self, req: RequisitoNaoFuncional):
        self.requisitos_nao_funcionais.append(req)


# --- PARTE 2: Validação Crítica ---
def validar_requisito(rf: RequisitoFuncional) -> dict:
    return {
        "ID": rf.id,
        "Descrição Longa (>20)": len(rf.descricao) > 20,
        "Tem Pré-condição": rf.pre_condicao.strip() != "",
        "Mensurável (Contém Números)": any(char.isdigit() for char in rf.descricao),
    }


# --- PARTE 3: Exportar Markdown ---
def exportar_markdown(srs: SRS):
    md = f"# SRS - {srs.projeto}\n\n"
    md += f"**Versão:** {srs.versao}\n\n{srs.descricao}\n\n"
    md += "## 🔧 Requisitos Funcionais\n"
    for rf in srs.requisitos_funcionais:
        md += f"### {rf.id}: {rf.nome}\n- **Ator:** {rf.ator}\n- **Descrição:** {rf.descricao}\n\n"
    md += "## ⚡ Requisitos Não-Funcionais\n"
    for rnf in srs.requisitos_nao_funcionais:
        md += f"### {rnf.id}: {rnf.categoria}\n- **Criterio:** {rnf.criterio_aceitacao}\n\n"
    return md


# --- EXECUÇÃO: FIAP Marketplace ---
marketplace = SRS(
    "FIAP Marketplace", "1.0", "Plataforma de compra e venda entre alunos."
)

# Adicionando RFs
marketplace.adicionar_rf(
    RequisitoFuncional(
        "RF-001",
        "Cadastro de Produto",
        "Permitir que o aluno cadastre produtos com foto e preço.",
        Prioridade.ALTA,
        "Aluno Vendedor",
        "Estar logado",
        "Produto visível no feed",
    )
)
marketplace.adicionar_rf(
    RequisitoFuncional(
        "RF-002",
        "Busca por Categoria",
        "O sistema deve filtrar produtos por 5 categorias diferentes.",
        Prioridade.MEDIA,
        "Aluno Comprador",
        "Nenhuma",
        "Lista filtrada exibida",
    )
)

# Adicionando RNFs
marketplace.adicionar_rnf(
    RequisitoNaoFuncional("RNF-001", "Segurança", "Dados criptografados.", "Uso de SSL")
)

# Validando e Exibindo
print("--- VALIDAÇÃO DE REQUISITOS ---")
for rf in marketplace.requisitos_funcionais:
    print(validar_requisito(rf))

print("\n--- FORMATO MARKDOWN (CONFLUENCE) ---")
print(exportar_markdown(marketplace))
