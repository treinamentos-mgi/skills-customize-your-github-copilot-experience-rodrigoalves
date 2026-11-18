# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Construa uma API REST com FastAPI para cadastrar e consultar livros. Pratique rotas HTTP, validação de dados, operações CRUD e códigos de status.

## 📝 Tarefas

### 🛠️ Criar a API e Consultar Livros

#### Descrição
Use o código inicial para criar os endpoints de consulta de livros. No terminal, instale as dependências e inicie a aplicação:

```bash
pip install fastapi "uvicorn[standard]"
uvicorn starter_code:app --reload
```

#### Requisitos
O programa concluído deve:

- Iniciar uma aplicação FastAPI acessível em `http://127.0.0.1:8000`.
- Implementar `GET /books` para listar os livros cadastrados.
- Implementar `GET /books/{book_id}` para consultar um livro pelo ID.
- Responder com o código `404` quando o ID solicitado não existir.

### 🛠️ Cadastrar e Atualizar Livros

#### Descrição
Adicione endpoints para criar livros e substituir os dados de um livro existente. Use o modelo `BookInput` do código inicial para validar os dados recebidos.

#### Requisitos
O programa concluído deve:

- Implementar `POST /books` para cadastrar um livro e retornar o livro criado com um ID.
- Responder com o código `201` ao criar um livro.
- Implementar `PUT /books/{book_id}` para substituir o título, autor e ano de um livro existente.
- Responder com o código `404` ao tentar atualizar um ID inexistente.
- Rejeitar títulos ou autores vazios e anos menores ou iguais a zero.

Exemplo de corpo para criar um livro:

```json
{
  "title": "A Ilha do Tesouro",
  "author": "Robert Louis Stevenson",
  "year": 1883
}
```

### 🛠️ Excluir Livros e Verificar a API

#### Descrição
Implemente a remoção de livros e verifique os endpoints pela documentação interativa do FastAPI, disponível em `http://127.0.0.1:8000/docs`.

#### Requisitos
O programa concluído deve:

- Implementar `DELETE /books/{book_id}` para remover um livro existente.
- Responder com o código `204` ao excluir um livro, sem retornar um corpo.
- Responder com o código `404` ao tentar excluir um ID inexistente.
- Usar a página `/docs` para testar a criação, consulta, atualização e exclusão de um livro.
- Usar o armazenamento em memória fornecido; os dados podem ser reiniciados quando a aplicação for encerrada.

---
