# Star Wars API - PowerOfData

Uma API RESTful para consultar dados do universo Star Wars, construída com FastAPI com deploy no Google Cloud Platform.

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Executando Localmente](#executando-localmente)
- [Documentação da API (Swagger)](#documentação-da-api-swagger)
- [Sistema de Ordenação](#sistema-de-ordenação)
- [Endpoints Disponíveis](#endpoints-disponíveis)
- [Deploy no GCP](#deploy-no-gcp)

## 🚀 Sobre o Projeto

Esta API fornece acesso a dados do universo Star Wars, incluindo personagens, planetas, filmes, espécies, naves e veículos. Os dados são obtidos da [SWAPI](https://swapi.dev/) (Star Wars API) e enriquecidos com funcionalidades adicionais como filtros personalizados e ordenação flexível.

## 🛠️ Tecnologias Utilizadas

- **Python 3.11**
- **FastAPI** - Framework web moderno e de alta performance
- **Uvicorn** - Servidor ASGI para execução local
- **Google Cloud Functions** - Hospedagem serverless
- **Google Cloud API Gateway** - Gerenciamento de API
- **Pydantic** - Validação de dados

## 📦 Instalação

### Pré-requisitos

- Python 3.11 ou superior
- pip (gerenciador de pacotes do Python)
- Git

### Passo a Passo

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/starwars-api.git
cd starwars-api
```

2. **Crie um ambiente virtual:**
```bash
python -m venv venv
```

3. **Ative o ambiente virtual:**

   - **Linux/macOS:**
   ```bash
   source venv/bin/activate
   ```

   - **Windows:**
   ```bash
   .\venv\Scripts\activate
   ```

4. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

## ▶️ Executando Localmente

1. **Certifique-se de que o ambiente virtual está ativado**

2. **Execute o servidor de desenvolvimento:**
```bash
python main.py
```

3. **Acesse a API:**
   - API: `http://localhost:8000`
   - A API estará disponível em `http://localhost:8000`

## 📖 Documentação da API (Swagger)

O FastAPI gera automaticamente uma documentação interativa da API usando Swagger UI.

### Acessar a Documentação

Após iniciar o servidor, acesse:

- **Swagger UI (Interativo):** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc (Alternativo):** [http://localhost:8000/redoc](http://localhost:8000/redoc)
- **OpenAPI JSON:** [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

Na documentação Swagger você pode:
- Visualizar todos os endpoints disponíveis
- Testar as requisições diretamente na interface
- Ver os parâmetros aceitos por cada endpoint
- Verificar os formatos de resposta

## 🔄 Sistema de Ordenação

A API implementa um sistema de ordenação flexível que permite aos usuários ordenar os resultados por qualquer campo disponível nos dados retornados.

### Como Funciona

O sistema de ordenação foi projetado seguindo o mesmo padrão arquitetural dos filtros existentes, mantendo a separação de responsabilidades entre camadas:

```
Router (recebe parâmetros) → Service (orquestra) → Ordering (aplica ordenação)
```

### Parâmetros de Ordenação

Todos os endpoints de listagem aceitam dois parâmetros opcionais:

| Parâmetro | Tipo | Padrão | Descrição |
|-----------|------|--------|-----------|
| `order_by` | string | `null` | Campo pelo qual ordenar os resultados |
| `order_direction` | string | `asc` | Direção da ordenação: `asc` (crescente) ou `desc` (decrescente) |

### Exemplos de Uso

```bash
# Ordenar pessoas por nome (A-Z)
GET /people?order_by=name&order_direction=asc

# Ordenar pessoas por altura (maior para menor)
GET /people?order_by=height&order_direction=desc

# Ordenar planetas por população (menor para maior)
GET /planets?order_by=population&order_direction=asc

# Ordenar filmes por data de lançamento (mais recente primeiro)
GET /films?order_by=release_date&order_direction=desc

# Ordenar naves por custo (mais caras primeiro)
GET /starships?order_by=cost_in_credits&order_direction=desc
```

### Características Técnicas

- **Ordenação Inteligente:** Strings numéricas (como "182" para altura) são convertidas automaticamente para números, garantindo ordenação numérica correta
- **Tratamento de Valores Especiais:** Valores como `unknown`, `n/a` e `none` são automaticamente movidos para o final da lista
- **Aplicação Pós-Filtros:** A ordenação é sempre aplicada após os filtros personalizados, garantindo que apenas os dados filtrados sejam ordenados
- **Case Insensitive:** Ordenação textual não diferencia maiúsculas de minúsculas

### Arquitetura

O sistema de ordenação está implementado em:

```
app/
├── utils/
│   └── ordering.py          # Classe Ordering com lógica reutilizável
├── services/
│   ├── people_service.py    # Integração com ordenação
│   ├── films_service.py
│   ├── planets_service.py
│   ├── species_service.py
│   ├── starships_service.py
│   └── vehicles_service.py
└── routers/
    ├── people.py            # Parâmetros order_by e order_direction
    ├── films.py
    ├── planets.py
    ├── species.py
    ├── starships.py
    └── vehicles.py
```

## 🌐 Endpoints Disponíveis

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/people` | Lista personagens |
| GET | `/people/{id}` | Detalhes de um personagem |
| GET | `/planets` | Lista planetas |
| GET | `/planets/{id}` | Detalhes de um planeta |
| GET | `/films` | Lista filmes |
| GET | `/films/{id}` | Detalhes de um filme |
| GET | `/species` | Lista espécies |
| GET | `/species/{id}` | Detalhes de uma espécie |
| GET | `/starships` | Lista naves |
| GET | `/starships/{id}` | Detalhes de uma nave |
| GET | `/vehicles` | Lista veículos |
| GET | `/vehicles/{id}` | Detalhes de um veículo |

### Parâmetros Comuns

Todos os endpoints de listagem suportam:

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| `page` | int | Número da página (padrão: 1) |
| `search` | string | Busca por nome/título |
| `order_by` | string | Campo para ordenação |
| `order_direction` | string | Direção: `asc` ou `desc` |

### Filtros Específicos

- **`/people`:** `gender` - Filtrar por gênero (male, female, etc.)
- **`/starships`:** `max_speed` - Filtrar por velocidade máxima

## ☁️ Deploy no GCP

O projeto está configurado para deploy automático via Cloud Build. O arquivo `cloudbuild.yaml` contém os passos para:

1. Deploy da Cloud Function
2. Criação da configuração do API Gateway
3. Atualização do Gateway

Para fazer deploy manualmente:

```bash
gcloud builds submit --config=cloudbuild.yaml
```

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Desenvolvido o desafio PowerOfData
