# 🎬 Exercício: Modelagem de Sistema de Streaming

Este projeto exercita os conceitos de **Agregação vs Composição** em diagramas de classe e sua conversão para código Python.

## 🗺️ Modelagem (Miro)

- **Plataforma (Todo) ↔ Catálogo (Parte):** Relacionamento de **Composição**. A existência do catálogo depende da plataforma.
- **Catálogo (Todo) ↔ Filme (Parte):** Relacionamento de **Agregação**. O filme existe fora do catálogo.
- **Usuário ↔ Avaliação:** O usuário possui uma lista de objetos de avaliação.

## 🚀 Como Funciona

O código utiliza métodos de instância para conectar as classes:

1. `Catalogo.add_filme(Filme)`: Demonstra a agregação.
2. `Usuario.avaliar(Filme, Avaliacao)`: Demonstra a associação entre usuário, sua nota e a obra.

---
