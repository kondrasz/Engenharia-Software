# 🎯 Exercício Prático: SRS do FIAP Marketplace

**Contexto:** Desenvolvimento de um marketplace interno voltado para a comercialização de produtos artesanais exclusivamente entre alunos da instituição.

---

## ⚙️ Parte 1: Requisitos Funcionais (RFs)

Os requisitos funcionais descrevem as funcionalidades diretas que o sistema deve oferecer aos usuários.

### RF-001 - Cadastro de Produto

- **Descrição:** O aluno vendedor deve poder cadastrar até 10 produtos, incluindo obrigatoriamente título, preço e 1 foto.
- **Pré-condição:** O usuário deve estar autenticado no sistema utilizando seu e-mail institucional `@fiap.com.br`.

### RF-002 - Busca por Categoria

- **Descrição:** O sistema deve oferecer a funcionalidade de filtragem de produtos através da seleção de uma categoria específica.
- **Pré-condição:** O usuário deve estar localizado na tela inicial de catálogo de produtos.

### RF-003 - Avaliação do Vendedor

- **Descrição:** O aluno comprador deve ter a permissão de atribuir uma nota técnica (escala de 1 a 5 estrelas) ao vendedor após a finalização de uma transação.
- **Pré-condição:** O status do pedido vinculado à transação deve estar marcado como 'Concluído'.

---

## 🛡️ Parte 2: Requisitos Não-Funcionais (RNFs)

Os requisitos não-funcionais definem os critérios de operação e qualidades do sistema (como o sistema deve se comportar).

### RNF-001 - Disponibilidade

- **Critério:** O marketplace deve garantir um índice de disponibilidade (_uptime_) de **99.9%**.
- **Contexto Crítico:** Este nível de serviço é mandatório especialmente durante as semanas de provas e períodos de entregas de RM (Registro de Matrícula).

### RNF-002 - Segurança (Conformidade LGPD)

- **Critério:** Em conformidade com a Lei Geral de Proteção de Dados, todos os dados sensíveis, incluindo histórico de compras e senhas dos alunos, devem ser obrigatoriamente criptografados antes do armazenamento no banco de dados.

---

## 📝 Notas de Implementação

> **Dica:** Ao documentar requisitos, lembre-se que os **RFs** focam na jornada do usuário (o que ele faz), enquanto os **RNFs** focam na infraestrutura e segurança (como o sistema sustenta a operação).
