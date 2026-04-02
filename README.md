# 💈 Barbearia — Agendamento Online

Sistema completo de agendamento para barbearia, desenvolvido como projeto fullstack de aprendizado. O projeto cobre desde a interface do usuário até a API backend com autenticação, gerenciamento de serviços e controle de agendamentos.

---

## 📸 Preview

<img src="../BARBER-PROJECT/front end/img/backendreadme.png" alt="preview-back">
<img src="../BARBER-PROJECT/front end/img/preview.png" alt="preview">

---

## 🧱 Visão Geral do Projeto

Este projeto é dividido em duas partes:

- **Frontend** — interface web desenvolvida com HTML, CSS e JavaScript, com páginas para login, cadastro, listagem de serviços e agendamento
- **Backend** — API RESTful construída com Python e Django REST Framework, responsável por autenticação JWT, gerenciamento de serviços e controle de agendamentos por usuário

---

## 🚀 Tecnologias

### Frontend
| Tecnologia | Uso |
|---|---|
| HTML5 | Estrutura semântica das páginas |
| CSS3 | Estilização e layout responsivo |
| JavaScript | Consumo da API e interatividade |

### Backend
| Tecnologia | Uso |
|---|---|
| Python | Linguagem principal |
| Django | Framework web |
| Django REST Framework | Construção da API RESTful |
| dj-rest-auth | Autenticação com JWT |
| PostgreSQL | Banco de dados relacional |
| django-cors-headers | Liberação de requisições do frontend |

---

## 🗂️ Estrutura do Projeto

```
barbearia/
│
├── frontend/
│   ├── index.html                  # Página inicial / Home
│   ├── html/
│   │   ├── login.html
│   │   ├── cadastro.html
│   │   ├── servicos.html
│   │   ├── agendamento.html
│   │   └── meus-agendamentos.html
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   ├── auth.js                 # Login, cadastro e token
│   │   ├── servicos.js             # Busca e exibe serviços
│   │   └── agendamentos.js         # Cria e cancela agendamentos
│   └── img/
│
└── backend/
    ├── manage.py
    ├── core/                       # Configurações do projeto Django
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── auth_app/                   # App de autenticação
    ├── services/                   # App de serviços da barbearia
    ├── appointments/               # App de agendamentos
    ├── requirements.txt
    └── .env.example
```

---

## 🖥️ Telas (Frontend)

| Tela | Descrição |
|---|---|
| **Login** | Email, senha e botão de entrada |
| **Cadastro** | Nome, email e senha |
| **Home** | Lista de serviços disponíveis com botão "Agendar" |
| **Serviços** | Listagem com nome, preço e duração de cada serviço |
| **Agendamento** | Seleção de serviço, data e horário disponível |
| **Meus Agendamentos** | Visualização e cancelamento dos agendamentos do usuário |
| **Admin** *(futuro)* | Gerenciar serviços e visualizar todos os agendamentos |

---

## 🔌 Endpoints da API

### 🔐 Autenticação (dj-rest-auth)

| Método | Rota | Descrição |
|---|---|---|
| `POST` | `/auth/registration/` | Cadastro de novo usuário |
| `POST` | `/auth/login/` | Login e geração do token JWT |
| `POST` | `/auth/logout/` | Logout |
| `GET` | `/auth/user/` | Dados do usuário autenticado |

### ✂️ Serviços

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/services/` | Listar todos os serviços |
| `GET` | `/services/{id}/` | Detalhe de um serviço |
| `POST` | `/services/` | Criar serviço *(admin)* |
| `PUT` | `/services/{id}/` | Atualizar serviço *(admin)* |
| `DELETE` | `/services/{id}/` | Remover serviço *(admin)* |

### 📅 Agendamentos

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/appointments/` | Listar agendamentos do usuário logado |
| `POST` | `/appointments/` | Criar novo agendamento |
| `GET` | `/appointments/{id}/` | Detalhe de um agendamento |
| `DELETE` | `/appointments/{id}/` | Cancelar agendamento |

---

## 🔗 Conexão Tela ↔ Endpoint

| Tela | Endpoint |
|---|---|
| Login | `POST /auth/login/` |
| Cadastro | `POST /auth/register/` |
| Home / Serviços | `GET /services/` |
| Agendamento | `POST /appointments/` |
| Meus Agendamentos | `GET /appointments/` |
| Cancelar | `DELETE /appointments/{id}/` |

---

## 🔄 Fluxo da Aplicação

```
Usuário abre o site
    ↓
Faz login (ou cadastro)
    ↓
Vê os serviços disponíveis
    ↓
Escolhe serviço, data e horário
    ↓
Confirma o agendamento
    ↓
Visualiza ou cancela nos "Meus Agendamentos"
```

---

## ⚠️ Regras de Negócio

- Cada usuário só pode visualizar e cancelar **os próprios agendamentos**
- Horários já ocupados não devem aparecer como disponíveis
- Apenas usuários com perfil **admin** podem criar, editar ou remover serviços

---

## ⚙️ Como Executar Localmente

### Frontend

```bash
# Clone o repositório
git clone https://github.com/eduardonunesfvm/Page-Barbearia.git
cd Page-Barbearia

# Abra o index.html diretamente no navegador
# ou use uma extensão como Live Server no VS Code
```

### Backend

```bash
# Clone o repositório (quando disponível)
git clone https://github.com/eduardonunesfvm/barbearia-api.git
cd barbearia-api

# Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp .env.example .env
# edite o .env com suas credenciais

# Execute as migrations
python manage.py migrate

# Crie um superusuário (admin)
python manage.py createsuperuser

# Inicie o servidor
python manage.py runserver
```

### Variáveis de Ambiente

```env
SECRET_KEY=sua_chave_secreta_django
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost/barbearia
ALLOWED_HOSTS=localhost,127.0.0.1
```

---

## ✅ Status do Projeto

| Etapa | Status |
|---|---|
| Páginas HTML/CSS | 🔄 Em desenvolvimentoo |
| Interatividade com JavaScript | 🔄 Em desenvolvimento |
| Configuração do Django + DRF | 🔄 Em desenvolvimento |
| Autenticação JWT (dj-rest-auth) | 🔄 Em desenvolvimento |
| CRUD de Serviços | ⏳ Pendente |
| Sistema de Agendamentos | ⏳ Pendente |
| Regras de permissão | ⏳ Pendente |
| Testes automatizados | ⏳ Pendente |
| Deploy em produção | ⏳ Pendente |

---

## 🔮 Próximas Melhorias

- Painel administrativo para gestão de serviços e agendamentos
- Controle de horários disponíveis por dia
- Paginação e filtros nos agendamentos
- Notificações por e-mail
- Testes automatizados

---

## 👨‍💻 Autor

Desenvolvido por **Eduardo Nunes** como projeto fullstack de aprendizado.

🔗 [GitHub](https://github.com/eduardonunesfvm)
