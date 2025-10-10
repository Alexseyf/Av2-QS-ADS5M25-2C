# Projeto de Testes Automatizados

Este projeto contém testes unitários automatizados para um sistema de gerenciamento de usuários.

## Estrutura do Projeto

```
atividade_avaliativa_2/
├── src/                   # Código-fonte da aplicação
│   ├── user_management.py # Sistema de gerenciamento de usuários
│   └── inventory_system.py # Sistema de gerenciamento de inventário
├── tests/                 # Diretório de testes
│   ├── unit/              # Testes unitários
│   │   ├── test_user_management.py     # Testes do sistema de usuários
│   │   └── test_inventory_system.py    # Testes do sistema de inventário
│   └── conftest.py        # Configurações compartilhadas para pytest
├── evidence/              # Diretório para evidências dos testes
├── README.md              # Este arquivo
├── requirements.txt       # Dependências do projeto
├── pytest.ini             # Configuração do pytest
├── run_tests.sh           # Script para execução dos testes
└── PROJECT_STRUCTURE.md   # Detalhamento da estrutura do projeto
```

## Requisitos

- Python 3.8+
- pytest
- pytest-html

## Instalação

É recomendado usar um ambiente virtual para instalar as dependências:

```bash
# Certifique-se de ter o pacote python3-venv instalado
sudo apt install python3-venv

# Crie um ambiente virtual
python3 -m venv venv

# Ative o ambiente virtual
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

Quando terminar de usar o ambiente virtual, você pode desativá-lo com:
```bash
deactivate
```

## Execução dos Testes

### Utilizando o script automatizado

Primeiro, ative o ambiente virtual:
```bash
source venv/bin/activate
```

Em seguida, execute o script:
```bash
./run_tests.sh
```
Este script executará todos os testes unitários.

### Execução manual

Lembre-se de ativar o ambiente virtual antes de executar os testes manualmente:
```bash
source venv/bin/activate
```

Executar todos os testes unitários:
```bash
pytest tests/unit
```

Executar apenas os testes do sistema de usuários:
```bash
pytest tests/unit/test_user_management.py
```

Executar apenas os testes do sistema de inventário:
```bash
pytest tests/unit/test_inventory_system.py
```

#### Com geração de relatório HTML
```bash
pytest tests/unit --html=evidence/report.html --self-contained-html
```

## Detalhes dos Testes

### Testes do Sistema de Usuários (21 testes)
- Validação de criação de usuários
- Validação de emails em diferentes formatos
- Validação de senhas (comprimento, caracteres especiais, etc.)
- Autenticação de usuários
- Desativação de usuários
- Gerenciamento de múltiplos usuários

### Testes do Sistema de Inventário (22 testes)
- Validação de criação de produtos
- Verificação de disponibilidade de produtos
- Atualização de quantidades em estoque
- Adição e remoção de produtos do inventário
- Listagem de produtos disponíveis
- Cálculo do valor total do inventário

## Integrantes do Grupo
- ![Alexandre Seyffert](https://avatars.githubusercontent.com/u/79027790?v=4&s=50) [Alexandre Seyffert](https://github.com/Alexseyf)
- ![Wagner Vieira](https://avatars.githubusercontent.com/u/165597457?v=4&s=50) [Wagner Vieira](https://github.com/Wagner-V1eira)
- ![Laura Ortiz](https://avatars.githubusercontent.com/u/173370106?v=4&s=50) [Laura Ortiz](https://github.com/OrtizLaura)
