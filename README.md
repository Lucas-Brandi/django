# 📝 Django Blog & User System

Aplicação web desenvolvida em **Python** com o framework **Django**, contando com um sistema de publicações (blog) e uma estrutura completa de autenticação e gerenciamento de usuários (cadastro, login, logout e recuperação de senha).

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Django](https://img.shields.io/badge/Django-5.x-092E20?logo=django)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📌 Funcionalidades

- 📰 Listagem e visualização de posts do blog
- 👤 Cadastro, login e logout de usuários
- 🔑 Fluxo completo de redefinição de senha (via e-mail)
- 🛠️ Painel administrativo do Django para gestão de conteúdo e usuários
- 🧪 Testes unitários para as apps `blog` e `users`

---

## 📂 Estrutura de Pastas e Arquivos

```text
django_project/
├── manage.py                   # Script CLI principal do Django
├── db.sqlite3                  # Banco de dados SQLite padrão
├── django_project/             # Configurações globais do projeto
│   ├── __init__.py
│   ├── asgi.py                 # Configuração para servidores ASGI
│   ├── settings.py             # Configurações do projeto (apps, DB, middleware, etc.)
│   ├── urls.py                 # Roteamento principal de URLs
│   └── wsgi.py                 # Configuração para servidores WSGI
├── blog/                       # Aplicação responsável pelo Blog
│   ├── migrations/              # Histórico de migrações do banco
│   │   └── 0001_initial.py
│   ├── templates/blog/          # Templates HTML da aplicação Blog
│   │   ├── about.html
│   │   ├── base.html
│   │   └── home.html
│   ├── admin.py                 # Registro de modelos no Admin
│   ├── apps.py                  # Configuração da app Blog
│   ├── models.py                # Modelos de dados (ex: Posts)
│   ├── tests.py                 # Testes unitários do Blog
│   ├── urls.py                  # Roteamento interno de URLs do Blog
│   └── views.py                 # Lógica das views (páginas e dados)
└── users/                       # Aplicação responsável pelos Usuários
    ├── migrations/               # Histórico de migrações do banco
    ├── templates/users/          # Templates HTML da aplicação Users
    │   ├── login.html
    │   ├── logout.html
    │   ├── password_reset.html
    │   ├── password_reset_complete.html
    │   ├── password_reset_confirm.html
    │   ├── password_reset_done.html
    │   ├── password_reset_email.html
    │   └── register.html
    ├── admin.py                  # Registro de perfis no Admin
    ├── apps.py                   # Configuração da app Users
    ├── forms.py                  # Formulários de registro e perfil
    ├── models.py                 # Modelos de usuário/perfil
    ├── tests.py                  # Testes unitários dos Usuários
    └── views.py                  # Lógica de cadastro, login e perfil
```

---

## 🛠️ Requisitos Prévios

Certifique-se de ter instalado em sua máquina:

- **Python 3.10+** (recomendado 3.12 ou 3.13)
- **Pip** (gerenciador de pacotes do Python)
- **Git**

---

## 💻 Passo a Passo para Executar Localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/Lucas-Brandi/django.git
cd django/django_project
```

### 2. Criar e ativar o ambiente virtual (venv)

É recomendável isolar as dependências do projeto em um ambiente virtual.

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell)**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (CMD)**

```cmd
python -m venv venv
venv\Scripts\activate.bat
```

### 3. Instalar as dependências

```bash
pip install django Pillow
```

> 💡 O pacote **Pillow** é necessário para manipulação de campos de imagem em modelos de usuário/perfil (`ImageField`).

Se o projeto tiver um `requirements.txt`, prefira:

```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente (opcional, recomendado)

Se o projeto usar `SECRET_KEY`, credenciais de e-mail (para o reset de senha) ou outras configurações sensíveis, crie um arquivo `.env` na raiz do projeto com base em um `.env.example`, e evite subir esses valores para o controle de versão.

### 5. Executar as migrações do banco de dados

```bash
python manage.py migrate
```

### 6. Criar um superusuário (administrador)

```bash
python manage.py createsuperuser
```

Siga as instruções no terminal para definir usuário, e-mail e senha.

### 7. Iniciar o servidor de desenvolvimento

```bash
python manage.py runserver
```

### 8. Acessar a aplicação

| Recurso                  | URL                                      |
|---------------------------|-------------------------------------------|
| Aplicação                 | http://127.0.0.1:8000/                    |
| Painel administrativo      | http://127.0.0.1:8000/admin/              |

---

## 🧪 Executando os Testes

Para rodar os testes unitários das aplicações `blog` e `users`:

```bash
python manage.py test
```

Para rodar os testes de uma app específica:

```bash
python manage.py test blog
python manage.py test users
```

---

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/minha-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona minha feature'`)
4. Faça o push para a branch (`git push origin feature/minha-feature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.
