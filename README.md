# 🚀 AutoU Email Classifier

> **Solução completa de IA para classificação automática de emails corporativos**

Uma aplicação full-stack desenvolvida para automatizar a triagem de emails em empresas, utilizando Inteligência Artificial para classificar mensagens e gerar sugestões de resposta contextualizadas.

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias](#-tecnologias)
- [Documentação Detalhada](#-documentação-detalhada)
- [Arquitetura](#-arquitetura)
- [Instalação com Docker](#-instalação-com-docker-recomendado)
- [Troubleshooting Docker](#-troubleshooting-docker)
- [Uso da Aplicação](#-uso-da-aplicação)
- [Dados de Exemplo](#-dados-de-exemplo)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [APIs e Endpoints](#-apis-e-endpoints)
- [Performance e Escalabilidade](#-performance-e-escalabilidade)
- [Segurança](#-segurança)

## 🎯 Sobre o Projeto

### **Problema**

Grandes empresas do setor financeiro lidam diariamente com um alto volume de emails que podem ser:

- 📈 **Produtivos**: Solicitações de status, uploads de arquivos, comunicações que exigem ação
- 📭 **Improdutivos**: Conversas informais, piadas, conteúdo sem relevância para o trabalho

### **Solução**

O AutoU Email Classifier utiliza IA generativa (Google Gemini) para:

- ✅ **Classificar automaticamente** emails em categorias PRODUTIVO/IMPRODUTIVO
- 🤖 **Gerar sugestões de resposta** contextualizadas e profissionais
- 📊 **Organizar histórico** de processamentos com interface intuitiva
- ⚡ **Processar de forma assíncrona** para melhor experiência do usuário

## ✨ Funcionalidades

### **🔐 Autenticação Segura**

- Sistema JWT com registro e login
- Rotas protegidas
- Gerenciamento de sessão

### **📧 Processamento Inteligente**

- Upload de texto direto ou arquivos (PDF/TXT)
- Classificação automática por IA
- Geração de respostas contextualizadas
- Processamento assíncrono com Celery

### **📊 Dashboard Completo**

- Histórico de emails processados
- Estados visuais (Processando/Concluído/Falhou)
- Visualização de classificações e respostas
- Interface responsiva e moderna

### **🛠️ Pipeline de NLP**

- Pré-processamento de texto
- Remoção de stopwords
- Análise de tokens
- Limpeza e formatação

## 🔧 Tecnologias

### **Frontend**

- **React 19** - Biblioteca para interfaces reativas
- **Vite** - Build tool moderna com HMR
- **Tailwind CSS** - Framework CSS utilitário
- **React Router DOM** - Roteamento SPA
- **Axios** - Cliente HTTP
- **React Hot Toast** - Sistema de notificações

### **Backend**

- **FastAPI** - Framework web assíncrono
- **SQLModel** - ORM baseado em SQLAlchemy
- **Alembic** - Gerenciamento de migrações
- **Celery** - Processamento assíncrono
- **Redis** - Broker de mensagens
- **Google Gemini API** - IA generativa

### **Infraestrutura**

- **PostgreSQL** - Banco de dados relacional
- **Docker Compose** - Orquestração de containers
- **Nginx** - Servidor web para produção

### **Fluxo de Processamento**

1. **Upload**: Usuário envia email via interface web
2. **Enqueue**: Backend enfileira tarefa no Redis
3. **Processing**: Celery Worker processa com NLP + IA
4. **Classification**: Google Gemini classifica e gera resposta
5. **Storage**: Resultado salvo no PostgreSQL
6. **Notification**: Frontend atualiza em tempo real

## Uso da Aplicação

1. **Registre-se** ou faça login
2. **Envie um email** (texto ou arquivo)
3. **Aguarde o processamento** (assíncrono)
4. **Visualize o resultado** no dashboard
5. **Analise a classificação** e resposta sugerida

## � Dados de Exemplo

Para facilitar os testes da aplicação, foram incluídos **arquivos de exemplo** na pasta `data/` que demonstram diferentes tipos de emails:

### **📁 Estrutura dos Exemplos**

```
data/
├── 📈 productive_1.pdf      # Email com entregáveis (PDF)
├── 📈 productive_2.txt      # Relatório de progresso (TXT)
├── 📈 productive_3.pdf      # Documentação técnica (PDF)
├── 📈 productive_4.txt      # Atualização de projeto (TXT)
├── 📈 productive_5.pdf      # Comunicação de trabalho (PDF)
├── 📭 unproductive_1.txt    # Conteúdo de entretenimento (TXT)
├── 📭 unproductive_2.pdf    # Mensagem casual (PDF)
├── 📭 unproductive_3.txt    # Piadas e humor (TXT)
├── 📭 unproductive_4.pdf    # Conversa informal (PDF)
└── 📭 unproductive_5.txt    # Assuntos pessoais (TXT)
```

### **🎯 Tipos de Exemplos Incluídos**

#### **📈 Emails Produtivos (5 arquivos)**

- ✅ **Relatórios de progresso** com status de projetos
- ✅ **Documentações técnicas** concluídas
- ✅ **Atualizações de trabalho** com informações relevantes
- ✅ **Comunicações formais** que requerem ação
- ✅ **Entregáveis** com anexos e instruções

#### **📭 Emails Improdutivos (5 arquivos)**

- ❌ **Conteúdo de entretenimento** (vídeos, memes)
- ❌ **Mensagens casuais** sem relevância profissional
- ❌ **Piadas e humor** compartilhado entre colegas
- ❌ **Conversas informais** sobre assuntos pessoais
- ❌ **Convites sociais** não relacionados ao trabalho

### **🚀 Como Usar os Exemplos**

1. **Upload via Interface**: Acesse http://localhost:80 e faça upload dos arquivos
2. **Teste Variado**: Experimente tanto PDFs quanto TXTs
3. **Compare Resultados**: Observe como a IA classifica cada tipo
4. **Analise Respostas**: Veja as sugestões geradas para cada categoria

> 💡 **Dica**: Use esses exemplos para testar a precisão da classificação e entender como a IA diferencia conteúdo produtivo de improdutivo.

## �📚 Documentação Detalhada

Este projeto possui documentação específica para cada componente:

### **📂 Documentação por Módulo**

| Pasta                             | README                               | Descrição                                                                                                                              |
| --------------------------------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| **[`/back-end/`](./back-end/)**   | [`README.md`](./back-end/README.md)  | 🔥 **Backend FastAPI completo**<br/>• Endpoints e schemas<br/>• Configuração local<br/>• Variáveis de ambiente<br/>• Pipeline NLP + IA |
| **[`/front-end/`](./front-end/)** | [`README.md`](./front-end/README.md) | ⚡ **Frontend React moderno**<br/>• Componentes e hooks<br/>• Autenticação JWT<br/>• Interface responsiva<br/>• Integração com API     |

**Link Para Os Repositórios:**

1. [Backend FastAPI](https://github.com/ViniciusLugli/AutoU-Email-Back)
2. [Frontend React](https://github.com/ViniciusLugli/AutoU-Email-Front)

> 💡 **Dica**: Cada pasta contém documentação específica com exemplos, configurações e guias detalhados para aquela tecnologia.

## 🛠️ Instalação com Docker (Recomendado)

### **🏗️ Serviços Incluídos**

| Serviço              | Tecnologia           | Porta  | Descrição                      |
| -------------------- | -------------------- | ------ | ------------------------------ |
| **🌐 Frontend**      | React + Vite + Nginx | 80     | Interface web responsiva       |
| **🔥 Backend**       | FastAPI + SQLModel   | 8000   | API REST com autenticação JWT  |
| **🗄️ PostgreSQL**    | PostgreSQL 15        | 5433\* | Banco de dados relacional      |
| **📦 Redis**         | Redis 7              | 6380\* | Cache e broker de mensagens    |
| **⚡ Celery Worker** | Python + Celery      | -      | Processamento assíncrono de IA |

> **\* Portas modificadas** para evitar conflitos com serviços locais

### **📋 Pré-requisitos Docker**

- **Docker** 20.10+
- **Docker Compose** 2.0+
- **Chave da Google AI Studio** (para funcionalidade de IA)

### **🚀 Setup Completo com Docker**

#### **Passo 1: Preparar o Ambiente**

```bash
# Clone o repositório
git clone <repository-url>
cd autou-build

# Configure as variáveis de ambiente
cp .env.example .env.docker
# Edite .env.docker com sua GENAI_API_KEY
```

#### **Passo 2: Iniciar os Serviços**

```bash
# 🔧 Construir e iniciar todos os serviços
docker-compose up --build -d

# ✅ Verificar status dos containers
docker-compose ps

# 📋 Verificar logs (opcional)
docker-compose logs -f
```

#### **Passo 3: Acessar a Aplicação**

| Serviço              | URL                                | Descrição                        |
| -------------------- | ---------------------------------- | -------------------------------- |
| **🌐 Frontend**      | http://localhost                   | Interface principal da aplicação |
| **🔥 API Backend**   | http://localhost:8000              | Endpoints REST da API            |
| **�📚 Documentação** | http://localhost:8000/docs         | Swagger UI interativo            |
| **🔍 OpenAPI**       | http://localhost:8000/openapi.json | Especificação da API             |

#### **Passo 4: Primeira Configuração (Automática)**

As migrações do banco são executadas automaticamente na inicialização do backend. Se necessário, execute manualmente:

```bash
# 🔄 Executar migrações do Alembic
docker-compose exec backend alembic upgrade head

# ✅ Verificar status das migrações
docker-compose exec backend alembic current
```

### **🛠️ Comandos Docker Úteis**

#### **📊 Monitoramento e Logs**

```bash
# 📋 Status de todos os containers
docker-compose ps

# 📝 Logs de todos os serviços
docker-compose logs -f

# 🔍 Logs de serviço específico
docker-compose logs -f backend
docker-compose logs -f celery_worker
docker-compose logs -f frontend

# 📈 Logs das últimas 50 linhas
docker-compose logs --tail=50 backend
```

#### **🔄 Gerenciamento de Serviços**

```bash
# ⏹️ Parar todos os serviços
docker-compose down

# 🧹 Parar e remover volumes (limpar dados)
docker-compose down -v

# 🔄 Reiniciar serviço específico
docker-compose restart backend

# 🏗️ Reconstruir serviço específico
docker-compose build backend
docker-compose up -d backend

# ⚡ Reconstruir tudo do zero
docker-compose down && docker-compose build --no-cache && docker-compose up -d
```

#### **💻 Executar Comandos nos Containers**

```bash
# 🖥️ Shell interativo no backend
docker-compose exec backend bash

# 🔄 Comandos do Alembic (migrações)
docker-compose exec backend alembic upgrade head
docker-compose exec backend alembic revision --autogenerate -m "nova_migração"
docker-compose exec backend alembic history

# ⚡ Comandos do Celery (workers)
docker-compose exec celery_worker celery -A app.services.celery inspect active
docker-compose exec celery_worker celery -A app.services.celery inspect stats

# 🗄️ Comandos do PostgreSQL
docker-compose exec postgres psql -U autou_user -d autou_db
```

### **💾 Volumes Persistentes**

O Docker Compose cria volumes nomeados para persistir dados importantes:

| Volume              | Localização                | Descrição                                                                    |
| ------------------- | -------------------------- | ---------------------------------------------------------------------------- |
| **`postgres_data`** | `/var/lib/postgresql/data` | 🗄️ Dados do PostgreSQL (usuários, emails, classificações)                    |
| **`redis_data`**    | `/data`                    | 📦 Cache do Redis (sessões, filas Celery)                                    |
| **`upload_data`**   | `/app/data`                | 📁 Arquivos enviados (PDFs, TXTs) - **compartilhado entre backend e worker** |

### **⚙️ Variáveis de Ambiente Docker**

As variáveis estão configuradas no arquivo `.env.docker`. Para modificar:

1. **Recomendado**: Crie o arquivo `.env.docker` na raiz do projeto
2. Use como base o `.env.example` para preparar o `.env.docker`

**Principais variáveis configuráveis:**

- `DATABASE_URL`: Conexão com PostgreSQL
- `CELERY_BROKER_URL` e `CELERY_RESULT_BACKEND`: URLs do Redis
- `GENAI_API_KEY`: Chave da API do Google Generative AI
- `VITE_API_BASE_URL`: URL da API para o frontend

### **🌐 Mapeamento de Portas**

Para evitar conflitos com serviços locais, as portas foram mapeadas da seguinte forma:

| Serviço    | Porto Host | Porto Container | Acesso Local          |
| ---------- | ---------- | --------------- | --------------------- |
| Frontend   | 80         | 80              | http://localhost      |
| Backend    | 8000       | 8000            | http://localhost:8000 |
| PostgreSQL | 5433       | 5432            | localhost:5433        |
| Redis      | 6380       | 6379            | localhost:6380        |

**📝 Notas Importantes:**

- Os containers se comunicam internamente usando os nomes dos serviços e portas padrão (`postgres:5432`, `redis:6379`)
- As portas externas foram modificadas para evitar conflitos com serviços locais
- O health check do PostgreSQL e Redis garante que dependências estejam prontas antes de iniciar outros serviços

## 🛠️ Troubleshooting Docker

### **🔧 Problemas Comuns e Soluções**

#### **🚫 Conflitos de Porta**

**Problema**: Portas já em uso no sistema local.

```bash
# ✅ Solução 1: Verificar processos usando as portas
sudo lsof -i :5433  # PostgreSQL
sudo lsof -i :6380  # Redis

# ✅ Solução 2: Alterar portas no docker-compose.yml
ports:
  - "NOVA_PORTA:PORTA_INTERNA"
```

#### **🗄️ Backend não conecta ao PostgreSQL**

**Sintomas**: Backend fica reiniciando ou erro de conexão com banco.

```bash
# 🔍 Diagnóstico
docker-compose logs postgres  # Verificar se PostgreSQL iniciou
docker-compose logs backend   # Verificar logs de conexão

# ✅ Solução
# Aguarde o health check - backend só inicia após PostgreSQL estar saudável
# Health check leva ~30 segundos na primeira execução
```

#### **⚡ Celery Worker não processa tarefas**

**Sintomas**: Emails ficam com status "Processando" indefinidamente.

```bash
# 🔍 Diagnóstico
docker-compose logs celery_worker  # Verificar logs do worker
docker-compose logs redis          # Verificar se Redis está rodando

# ✅ Verificar se o worker está ativo
docker-compose exec celery_worker celery -A app.services.celery inspect active

# ✅ Reiniciar o worker
docker-compose restart celery_worker
```

#### **🌐 Frontend não carrega ou API não conecta**

**Sintomas**: Página em branco ou erro de conexão.

```bash
# 🔍 Diagnóstico
docker-compose logs frontend  # Verificar logs do Nginx
docker-compose logs backend   # Verificar se API está rodando

# ✅ Verificar se backend responde
curl -f http://localhost:8000/health/

# ✅ Verificar variável de ambiente no frontend
# Deve apontar para: VITE_API_BASE_URL=http://localhost:8000
```

#### **🔄 Problemas com Migrações**

**Sintomas**: Tabelas não existem ou erro de schema.

```bash
# 🔍 Ver status atual das migrações
docker-compose exec backend alembic current

# 🔍 Ver histórico de migrações
docker-compose exec backend alembic history

# ✅ Aplicar migrações pendentes
docker-compose exec backend alembic upgrade head

# ✅ Criar nova migração (se necessário)
docker-compose exec backend alembic revision --autogenerate -m "descrição"

# 🧹 Reset completo do banco (CUIDADO - PERDE DADOS!)
docker-compose down -v
docker-compose up -d postgres
docker-compose exec backend alembic upgrade head
```

#### **🔑 Erro de API Key do Google AI**

**Sintomas**: Erro "GenAI API not configured" nos logs do Celery.

```bash
# ✅ Verificar se a chave está configurada no .env.docker
grep GENAI_API_KEY .env.docker

# ✅ Obter chave em: https://makersuite.google.com/app/apikey
# ✅ Adicionar no .env.docker:
# GENAI_API_KEY=sua_chave_aqui

# ✅ Reiniciar serviços após alteração
docker-compose restart backend celery_worker
```

### **🩺 Comandos de Diagnóstico**

```bash
# 📊 Status de saúde dos containers
docker-compose ps

# 📊 Uso de recursos
docker stats --no-stream

# 🌐 Teste de conectividade
docker-compose exec backend curl -f http://redis:6379
docker-compose exec backend nc -zv postgres 5432

# 📋 Informações do sistema
docker system info
docker system df  # Uso de espaço em disco
```

### **🆘 Reset Completo Docker**

Se tudo mais falhar, você pode resetar completamente:

```bash
# ⚠️ ATENÇÃO: Isso remove TODOS os dados!
docker-compose down -v          # Para tudo e remove volumes
docker system prune -f          # Remove containers/imagens não utilizados
docker-compose build --no-cache # Reconstrói tudo do zero
docker-compose up -d            # Inicia novamente
```

## 📁 Estrutura do Projeto

```
autou-build/
├── 📄 README.md                 # Documentação principal (você está aqui)
├── 🐳 docker-compose.yml        # Orquestração de serviços
├── ⚙️ .env.docker              # Variáveis de ambiente
├── 📋 .env.example             # Exemplo de configuração
│
├── back-end/                   # 🔥 Backend FastAPI
│   ├── 📚 README.md           # Documentação completa do backend
│   ├── 🐳 Dockerfile          # Container Python
│   ├── 📦 requirements.txt    # Dependências Python
│   ├── ⚙️ alembic.ini         # Configuração de migrações
│   │
│   ├── app/                   # Código da aplicação
│   │   ├── 🔧 main.py         # Entrada da aplicação FastAPI
│   │   ├── 🗄️ models.py       # Modelos SQLModel
│   │   ├── 📋 schemas.py      # Schemas Pydantic
│   │   ├── 🔍 crud.py         # Operações CRUD
│   │   ├── 💾 db.py           # Configuração do banco
│   │   │
│   │   ├── core/              # Configurações centrais
│   │   │   ├── ⚙️ config.py   # Configurações gerais
│   │   │   ├── 📊 constants.py # Constantes e variáveis
│   │   │   └── 🔐 security.py # Autenticação JWT
│   │   │
│   │   ├── routes/            # Endpoints da API
│   │   │   ├── 🔐 auth.py     # Autenticação
│   │   │   ├── ❤️ health.py   # Health checks
│   │   │   ├── 📧 texts.py    # Processamento de emails
│   │   │   └── 👤 users.py    # Gerenciamento de usuários
│   │   │
│   │   └── services/          # Serviços e lógica de negócio
│   │       ├── 🔐 auth_service.py # Serviços de autenticação
│   │       ├── ⚡ celery.py    # Configuração Celery
│   │       ├── 🤖 ia.py       # Integração com IA (Gemini)
│   │       ├── 📝 nlp.py      # Processamento de linguagem
│   │       ├── 📂 read_file.py # Leitura de arquivos
│   │       ├── ⚙️ tasks.py     # Tarefas assíncronas
│   │       └── 👤 user_service.py # Serviços de usuário
│   │
│   └── alembic/               # 🔄 Migrações do banco
│       ├── 📚 README          # Documentação Alembic
│       ├── ⚙️ env.py          # Configuração de migração
│       └── versions/          # Histórico de migrações
│
└── front-end/                 # ⚡ Frontend React
    ├── 📚 README.md           # Documentação completa do frontend
    ├── 🐳 Dockerfile          # Container Node.js + Nginx
    ├── 📦 package.json        # Dependências Node.js
    ├── ⚙️ vite.config.js      # Configuração Vite
    ├── 🎨 tailwind.config.js  # Configuração Tailwind
    ├── 🖥️ nginx.conf          # Configuração Nginx
    │
    ├── public/                # Assets estáticos
    │   └── 🖼️ favicon-32x32.png
    │
    └── src/                   # Código da aplicação
        ├── 🚀 main.jsx        # Entrada da aplicação React
        ├── 📱 App.jsx         # Componente raiz
        ├── 🎨 index.css       # Estilos globais
        │
        ├── components/        # Componentes reutilizáveis
        │   ├── ✅ ConfirmModal.jsx     # Modal de confirmação
        │   ├── 📧 EmailResultCard.jsx  # Card de resultado
        │   ├── ⚠️ ErrorBoundary.jsx   # Tratamento de erros
        │   ├── 🖼️ Layout.jsx          # Layout principal
        │   ├── ⏳ Loading.jsx         # Componente de loading
        │   ├── 🔐 ProtectedRoute.jsx  # Rotas protegidas
        │   └── 👤 UserModal.jsx       # Modal de usuário
        │
        ├── pages/             # Páginas da aplicação
        │   ├── 🔐 Login.jsx   # Página de login
        │   ├── 📝 Register.jsx # Página de registro
        │   └── 📊 Dashboard.jsx # Dashboard principal
        │
        ├── services/          # Serviços e APIs
        │   ├── 🌐 api.jsx     # Cliente HTTP
        │   └── 📋 index.jsx   # Configurações de serviços
        │
        ├── hooks/             # React Hooks customizados
        │   └── 🔐 useAuth.jsx # Hook de autenticação
        │
        ├── context/           # Context API do React
        │   ├── 🔐 AuthContext.jsx   # Contexto de autenticação
        │   └── 🔗 AuthProvider.jsx  # Provider de autenticação
        │
        ├── constants/         # Constantes da aplicação
        │   └── 📊 index.js    # Constantes globais
        │
        └── utils/             # Utilitários
            └── 🔧 formatters.jsx # Formatadores de dados
```

## 🌐 APIs e Endpoints

### **Principais Endpoints**

| Método | Endpoint                 | Descrição                | Auth |
| ------ | ------------------------ | ------------------------ | ---- |
| `POST` | `/auth/register`         | Registro de usuário      | ❌   |
| `POST` | `/auth/login`            | Login do usuário         | ❌   |
| `POST` | `/texts/processar_email` | Processar email          | ✅   |
| `GET`  | `/texts/`                | Listar emails do usuário | ✅   |
| `GET`  | `/users/me`              | Perfil do usuário        | ✅   |
| `GET`  | `/health/`               | Health check da API      | ❌   |

### **Exemplo de Uso da API**

```bash
# 1. Registrar usuário
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"username":"user","email":"user@example.com","password":"123456"}'

# 2. Fazer login
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"123456"}'

# 3. Processar email
curl -X POST "http://localhost:8000/texts/processar_email" \
  -H "Authorization: Bearer <token>" \
  -F "text=Finalizei o relatório trimestral. Revisem antes da reunião."
```

## 🚀 Performance e Escalabilidade

### **Otimizações Implementadas**

- ⚡ **Processamento Assíncrono**: Celery para tarefas pesadas
- 🔄 **Connection Pooling**: PostgreSQL otimizado
- 📦 **Containerização**: Docker para isolamento e portabilidade
- 🎯 **Lazy Loading**: Componentes carregados sob demanda
- 🗄️ **Caching**: Redis para cache de sessões

### **Monitoramento**

- 📊 **Health Checks**: Endpoints de saúde para todos os serviços
- 📝 **Logging**: Logs estruturados para debug
- 📈 **Métricas**: Celery worker monitoring

### **🔧 Configurações de Produção Docker**

Para ambiente de produção, considere estas otimizações:

```yaml
# docker-compose.prod.yml (exemplo)
services:
  backend:
    restart: always
    deploy:
      resources:
        limits:
          memory: 512M
        reservations:
          memory: 256M

  celery_worker:
    deploy:
      replicas: 2 # Múltiplos workers
      resources:
        limits:
          memory: 1G
```

### **📊 Monitoramento Docker**

```bash
# 📈 Monitorar recursos em tempo real
docker stats

# 📋 Health checks automáticos
docker-compose exec backend curl -f http://localhost:8000/health/
docker-compose exec postgres pg_isready -U autou_user
```

## 🔒 Segurança

### **Medidas Implementadas**

- 🔐 **JWT Authentication**: Tokens seguros com expiração
- 🛡️ **CORS Configuration**: Proteção contra requisições maliciosas
- 🔍 **Input Validation**: Validação rigorosa de entrada
- 📁 **File Upload Security**: Validação de tipos e tamanhos
- 🔑 **Environment Variables**: Secrets em variáveis de ambiente

## � Recursos Adicionais

### **📖 Documentação Relacionada**

- **🐳 [Docker Compose Reference](https://docs.docker.com/compose/)**
- **🔥 [FastAPI Documentation](https://fastapi.tiangolo.com/)**
- **⚡ [React Documentation](https://react.dev/)**
- **🗄️ [PostgreSQL Docker](https://hub.docker.com/_/postgres)**
- **📦 [Redis Docker](https://hub.docker.com/_/redis)**
- **🤖 [Google AI Studio](https://makersuite.google.com/app/apikey)**

### **🛠️ Ferramentas Úteis**

```bash
# 🔍 Docker Desktop (GUI)
# Facilita visualização de containers, volumes e logs

# 📊 Portainer (Web UI para Docker)
docker run -d -p 9000:9000 --name portainer \
  -v /var/run/docker.sock:/var/run/docker.sock \
  portainer/portainer-ce

# 📝 Dive (Análise de imagens Docker)
dive autou-build-backend
```

## �📄 Licença

Este projeto foi desenvolvido como solução técnica para demonstração de habilidades em desenvolvimento full-stack e integração com IA.

---

<div align="center">

### 🌟 **AutoU Email Classifier**

**Transformando a gestão de emails corporativos com Inteligência Artificial**

[🚀 Começar Agora](#-instalação-com-docker-recomendado) · [📚 Documentação](#-documentação-detalhada) · [🐛 Reportar Bug](issues) · [💡 Sugerir Feature](issues)

</div>
