# Projeto Django DRF: Gerenciamento de Personagens, Armas e Avatares

## Descrição

Este projeto cria uma API utilizando Django e Django REST Framework para gerenciar objetos `Personagem`, `Arma` e `Avatar`. Cada `Avatar` pode selecionar um `Personagem` e uma `Arma`.

## Pré-requisitos

- Python 3.8+
- Django 4.0+
- Django REST Framework

## Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/usuario/projeto-django-drf.git
cd projeto-django-drf

2. Criar e ativar um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`

3. Instalar dependências
pip install -r requirements.txt

4. Configurar o banco de dados
Edite o arquivo settings.py para configurar o banco de dados, caso necessário. Por padrão, o projeto está configurado para usar o SQLite.

5. Aplicar migrações
python manage.py migrate


6. Criar superusuário (opcional)
python manage.py createsuperuser


7. Rodar o servidor
python manage.py runserver


Estrutura do Projeto
`Personagem`: App para gerenciar personagens.
`arma`: App para gerenciar armas.
`avatar`: App para gerenciar avatares.

Testando a API
Você pode usar ferramentas como Postman ou cURL para testar os endpoints da API.

Endpoints
GET /api/personagens/: Lista todos os personagens
POST /api/personagens/: Cria um novo personagem
GET /api/personagens/{id}/: Detalha um personagem específico
PUT /api/personagens/{id}/: Atualiza um personagem específico
DELETE /api/personagens/{id}/: Deleta um personagem específico
Endpoints semelhantes existem para armas e avatares.