# Projeto Robô de Captura de Dados - Pokémon

Este projeto consiste em um robô (RPA) desenvolvido em Python para automatizar a coleta de dados e imagens de Pokémons. A aplicação consome a [PokéAPI](https://pokeapi.co/docs/v2), sorteia IDs de Pokémons aleatoriamente, busca informações detalhadas sobre eles, baixa suas imagens a partir do Google Imagens e, por fim, consolida todos os dados em uma planilha Excel.

## Funcionalidades
 - **Sorteio Aleatório**: Seleciona 3 IDs de Pokémon de forma aleatória a cada execução.

 - **Coleta de Dados**: Busca informações detalhadas dos Pokémons sorteados via API, como nome, tipo, status e dimensões.

 - **Download de Imagens**: Pesquisa pelo nome do Pokémon no Google e baixa 3 imagens correspondentes.

 - **Consolidação em Excel**: Salva todos os dados coletados e os caminhos das imagens salvas em um único arquivo `.xlsx` com abas separadas.

 - **Logging Completo**: Registra todas as etapas da execução e possíveis erros em um arquivo de log diário.

## Arquitetura de Pastas

```
.
├── data
│   ├── excel/                          # Dados consolidados
│   │   └── pokemon_YYYYMMDD.xlsx       
│   ├── images/                         # Armazenamento de imagens
│   │   └── pokemon_name_1.jpg
│   │   └── pokemon_name_2.jpg
│   └── logs/                           # Logs da aplicação
│       └── log_YYYYMMDD.log
├── services                            # Script de serviço
│   ├── api.py
│   ├── image_getter.py
│   ├── image_saver.py
│   └── spreadsheet_saver.py
├── utils                               # Utilitários
│   └── logger.py
├── config.py                           # Variáveis de configuração
├── main.py                             # Script principal
├── Dockerfile                          # Arquivo Docker
├── docker-compose.yml                  # Arquivo Compose
└── requirements.txt                    # Dependências do projeto
```

## Como Rodar a Aplicação

### Configuração
Você pode customizar o comportamento do robô alterando as variáveis no arquivo `config.py`:

`QUANTITY_IDS`: Altere para definir quantos Pokémons serão sorteados por execução.
`QUANTITY_IMAGES`: Altere para definir quantas imagens serão baixadas para cada Pokémon.

> Você pode executar o projeto de duas maneiras: usando Docker (recomendado para maior praticidade) ou um ambiente virtual Python.

### Opção 1: Usando Docker (Recomendado)

### Pré-requisitos:
 - [Docker](https://docs.docker.com/desktop/setup/install/windows-install/) instalado e em execução na sua máquina.

### Guia:

1. Clone o Repositório:
   ```Bash
   git clone https://github.com/lucasaguiar-la/case-pokeAPI.git
   ```

2. Navegue até o diretório do projeto:
    ```Bash
    cd case-pokeAPI
    ```

3. Construa e execute o contêiner Docker:
   ```Bash
    docker-compose up --build
   ```

O processo será iniciado, e ao final, os arquivos estarão na pasta `data/`.

---

### Opção 2: Usando Ambiente Virtual Python (venv)

### Pré-requisitos:
 - [Python 3.11](https://www.python.org/downloads/) ou superior instalado.

### Guia:

1. Clone o Repositório e navegue até o diretório:
   ```Bash
   git clone https://github.com/lucasaguiar-la/case-pokeAPI.git
   cd case-pokeAPI
   ```

2.  Crie o ambiente virtual:
    ```Bash
    python -m venv venv
    ```

3. Ative o ambiente virtual:
   - No Windows:
        ```Bash
        .\venv\Scripts\activate
        ```
    - No macOS ou Linux:
        ```Bash
        source venv/bin/activate
        ```

4.  Instale as dependências do projeto:
    ```Bash
    pip install -r requirements.txt
    ```

5.  Execute a aplicação:
    ```Bash
    python main.py
    ```

O processo será iniciado, e ao final, os arquivos estarão na pasta `data/`.


## Requisitos do case técnico

- [x] Consumir a API pública do Pokémon

- [x] Sortear 3 IDs aleatórios por rodada, sem repetição.

- [x] Gerar Excel consolidado com dados gerais dos pokémons.

- [x] Acessar o Google, pesquisar pelo nome do Pokémon e baixar 3 imagens por Pokémon.

- [x]  Salvar as imagens em `./data/images///` e referenciar no Excel.

- [x] Tratar exceções de API, download e navegação, garantindo continuidade do fluxo

- [x] README.md com instruções

- [x] Pasta `data/` organizada

- [x] Logs completos de execução