# ============================================================
# 🎬 SISTEMA DE STREAMING — Modelagem de Classes
# ============================================================


class Filme:
    def __init__(self, titulo: str, duracao: int, genero: str):
        self.titulo = titulo
        self.duracao = duracao
        self.genero = genero

    def __repr__(self):
        return f"{self.titulo} ({self.duracao} min) - {self.genero}"


class Avaliacao:
    def __init__(self, nota: float, comentario: str):
        self.nota = nota
        self.comentario = comentario
        self.filme_avaliado = None  # Será preenchido ao avaliar


class Usuario:
    def __init__(self, nome: str, email: str, plano: str):
        self.nome = nome
        self.email = email
        self.plano = plano
        self.minhas_avaliacoes = []

    def avaliar(self, filme: Filme, avaliacao: Avaliacao):
        avaliacao.filme_avaliado = filme
        self.minhas_avaliacoes.append(avaliacao)
        print(
            f"✨ {self.nome} avaliou o filme '{filme.titulo}' com nota {avaliacao.nota}"
        )

    def ver_avaliacoes(self):
        print(f"\n📝 Avaliações de {self.nome}:")
        for av in self.minhas_avaliacoes:
            print(f"   - {av.filme_avaliado.titulo}: {av.nota} ('{av.comentario}')")


class Catalogo:
    def __init__(self, titulo_catalogo: str, qtd_filmes: int):
        self.titulo_catalogo = titulo_catalogo
        self.lista_filmes = []

    def add_filme(self, filme: Filme):
        self.lista_filmes.append(filme)
        print(
            f"🎬 Filme '{filme.titulo}' adicionado ao catálogo {self.titulo_catalogo}."
        )

    def listar_filmes(self):
        print(f"\n📂 Catálogo: {self.titulo_catalogo}")
        for filme in self.lista_filmes:
            print(f"   🎞️ {filme}")


class Plataforma:
    def __init__(self, nome: str, pais: str):
        self.nome = nome
        self.pais = pais
        print(f"🚀 Plataforma {self.nome} ({self.pais}) inicializada com sucesso!")


# ============================================================
# ⚙️ EXECUÇÃO DO FLUXO (Conforme solicitado)
# ============================================================

# Inicializando a plataforma e catálogo
netflix = Plataforma("Netflix", "EUA")
catalogo = Catalogo("Filmes em Destaque", 0)

# Criando filmes (Entidades independentes)
filme1 = Filme("Corra", 104, "Terror")
filme2 = Filme("Beetlejuice", 92, "Comédia")

# Agregando filmes ao catálogo
catalogo.add_filme(filme1)
catalogo.add_filme(filme2)

# Usuário e Avaliação
usuario = Usuario("Ana", "ana@email.com", "Premium")
avaliacao = Avaliacao(9.5, "Incrível! Assisti duas vezes")

# Realizando a avaliação
usuario.avaliar(filme1, avaliacao)

# Outputs finais
catalogo.listar_filmes()
usuario.ver_avaliacoes()
