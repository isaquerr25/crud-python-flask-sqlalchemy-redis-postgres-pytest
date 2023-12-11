---
runme:
  id: 01HHA6S1J4NBH1JPZN2N2HMJS3
  version: v2.0
---

Passo 4: Executando o aplicativo com Docker Compose

Execute os seguintes comandos no terminal:

bash

docker-compose build


docker-compose up -d

Isso iniciará o aplicativo em http://localhost:5000.

Passo 5: Executando os testes com Pytest

Execute o seguinte comando para executar os testes:

bash

docker-compose exec web pytest

Isso executará os testes dentro do contêiner do aplicativo.

Este é um exemplo básico de um CRUD em Python usando Flask, SQLAlchemy, Redis, Docker Compose e Pytest, com boas práticas de OOP. Certifique-se de adaptar o código conforme necessário para atender aos requisitos específicos do seu projeto.