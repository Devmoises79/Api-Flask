# 🚗 API Flask — Cadastro de Veículos

📖 Sobre o Projeto

Este projeto consiste em uma API REST desenvolvida com Flask, permitindo realizar operações básicas de cadastro e listagem de veículos.

A aplicação simula um backend real, com manipulação de dados em memória e endpoints acessíveis via requisições HTTP.

# 🎯 Objetivos
- Praticar desenvolvimento de APIs REST com Flask
- Trabalhar rotas HTTP (GET e POST)
- Manipular dados em formato JSON
- Simular operações de CRUD
- Utilizar ferramentas externas como Postman para testes

# ⚙️ Tecnologias Utilizadas
- Python 3
- Flask
- JSON (estrutura de dados)
- Postman (para testes de requisições)

# 🧩 Funcionalidades

- 📥 Listagem de veículos (GET /carros)
- ➕ Cadastro de veículos (POST /carros)
- 📦 Armazenamento em memória (lista Python)
- 🔄 Retorno de respostas em JSON
- 📡 API pronta para testes via HTTP
- 📌 Estrutura da API

```bash
GET /carros

Retorna todos os veículos cadastrados:

[
  {
    "id": 1,
    "marca": "Fiat",
    "modelo": "Palio"
  }
]
POST /carros

Adiciona um novo veículo:

{
  "id": 6,
  "marca": "Honda",
  "modelo": "Civic"
}
```

# 🧠 Aprendizados

Este projeto reforça conceitos fundamentais de backend:

- Criação de APIs REST
- Manipulação de requisições HTTP
- Estrutura de dados em Python
- Serialização JSON
- Conceito básico de CRUD

# 🚀 Execução

Para rodar o projeto:

```bash
pip install flask
python main.py

```

# 👨‍💻 Autor

Projeto desenvolvido por Moisés Aniceto como parte de estudos em desenvolvimento backend com Python e introdução a APIs.
