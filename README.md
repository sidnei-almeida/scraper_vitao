# 🌱 Scraper Vitao - Coleta de Dados Nutricionais

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)](https://github.com/sidnei-almeida/scraper_mae_terra)

> Sistema completo para coleta automatizada de dados nutricionais dos produtos da Vitao disponíveis no site FatSecret Brasil.

## 📋 Índice

- [🎯 Sobre o Projeto](#-sobre-o-projeto)
- [✨ Funcionalidades](#-funcionalidades)
- [🚀 Como Usar](#-como-usar)
- [📦 Instalação](#-instalação)
- [🛠️ Tecnologias](#️-tecnologias)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
- [📊 Exemplos de Uso](#-exemplos-de-uso)
- [🤝 Contribuindo](#-contribuindo)
- [📄 Licença](#-licença)

## 🎯 Sobre o Projeto

O **Scraper Vitao** é uma ferramenta desenvolvida em Python para automatizar a coleta de dados nutricionais dos produtos da Vitao disponíveis no site FatSecret Brasil. O sistema oferece uma interface interativa e amigável para extrair informações como calorias, carboidratos, proteínas, gorduras e outros nutrientes de todos os produtos da marca.

### 🎯 Objetivos

- **Automatizar** a coleta de dados nutricionais
- **Padronizar** informações em formato estruturado
- **Facilitar** análises nutricionais e pesquisas
- **Fornecer** dados confiáveis e atualizados

## ✨ Funcionalidades

### 🔍 Coleta Inteligente de URLs
- Navegação automática pelas páginas de busca
- Detecção automática de fim de resultados
- Coleta de URLs únicas sem duplicatas
- Salvamento em formato JSON estruturado

### 📊 Extração de Dados Nutricionais
- Coleta completa de informações nutricionais
- Tratamento de dados ausentes (valor 0)
- Suporte a diferentes tipos de porção (ml, unidades, etc.)
- Exportação em formato CSV padronizado

### ⚡ Interface Interativa
- Menu CLI bonito e intuitivo
- Barras de progresso animadas
- Confirmações antes de operações críticas
- Tratamento robusto de erros

### 📁 Gerenciamento de Arquivos
- Visualização de arquivos gerados
- Limpeza automática de dados antigos
- Organização em estrutura de pastas

## 🚀 Como Usar

### Interface Principal

```bash
# Execute o menu interativo
python main.py
```

### Opções Disponíveis

1. **🔍 Coletar URLs** - Extrai URLs dos produtos da Vitao
2. **📊 Coletar Dados** - Extrai dados nutricionais dos produtos
3. **⚡ Coleta Completa** - Executa URLs + Dados automaticamente
4. **📋 Ver Arquivos** - Lista arquivos gerados
5. **🗑️ Limpar Dados** - Remove arquivos antigos
6. **📖 Sobre o Programa** - Informações detalhadas
7. **❌ Sair** - Encerrar programa

### Uso Direto dos Scripts

```bash
# Coletar apenas URLs
python config/url_collector.py

# Coletar apenas dados nutricionais
python config/scraper.py
```

## 📦 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos de Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/sidnei-almeida/scraper_vitao.git
cd scraper_vitao
```

2. **Crie um ambiente virtual (recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Execute o programa**
```bash
python main.py
```

## 🛠️ Tecnologias

### Linguagem e Frameworks
- **Python 3.8+** - Linguagem principal
- **Requests** - Requisições HTTP
- **BeautifulSoup4** - Parsing HTML
- **LXML** - Parser XML/HTML rápido

### Bibliotecas Auxiliares
- **CSV** - Manipulação de arquivos CSV
- **JSON** - Manipulação de dados JSON
- **OS** - Operações do sistema
- **Time** - Controle de tempo e pausas

## 📁 Estrutura do Projeto

```
scraper_vitao/
├── 📁 config/                    # Scripts de configuração
│   ├── 🐍 url_collector.py      # Coletor de URLs
│   └── 🐍 scraper.py            # Scraper de dados nutricionais
├── 📁 dados/                     # Arquivos gerados
│   ├── 📄 vitao_urls.json       # URLs coletadas
│   └── 📊 vitao_nutricional.csv # Dados nutricionais
├── 📁 html/                      # Arquivos HTML (se necessário)
├── 📄 main.py                    # Interface principal
├── 📄 requirements.txt           # Dependências
├── 📄 README.md                  # Este arquivo
└── 📄 .gitattributes            # Configurações Git
```

## 📊 Exemplos de Uso

### Coleta Completa Automática

```bash
# Execute o menu principal
python main.py

# Escolha a opção 3 (Coleta Completa)
# O sistema irá:
# 1. Coletar todas as URLs dos produtos
# 2. Extrair dados nutricionais
# 3. Gerar arquivos JSON e CSV
```

### Arquivo CSV Gerado

O sistema gera um arquivo CSV com as seguintes colunas:

| Coluna | Descrição | Exemplo |
|--------|-----------|---------|
| `nome_produto` | Nome completo do produto | "Vitao Psyllium" |
| `url` | Link do produto no FatSecret | `https://...` |
| `categoria` | Categoria do produto | "Produto Vitao" |
| `porcao` | Quantidade da porção | 700 |
| `calorias` | Calorias em kcal | 551 |
| `carboidratos` | Carboidratos em gramas | 74.0 |
| `proteinas` | Proteínas em gramas | 12.0 |
| `gorduras_totais` | Gorduras totais em gramas | 23.0 |
| `gorduras_saturadas` | Gorduras saturadas em gramas | 11.0 |
| `fibras` | Fibras em gramas | 0.0 |
| `acucares` | Açúcares em gramas | 115.0 |
| `sodio` | Sódio em miligramas | 530 |

### Arquivo JSON Gerado

```json
[
  "https://www.fatsecret.com.br/calorias-nutrição/vitao/produto1/1-porção",
  "https://www.fatsecret.com.br/calorias-nutrição/vitao/produto2/1-porção",
  "https://www.fatsecret.com.br/calorias-nutrição/vitao/produto3/1-porção"
]
```

## 🤝 Contribuindo

Contribuições são sempre bem-vindas! Para contribuir:

1. **Fork** o projeto
2. **Crie** uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. **Push** para a branch (`git push origin feature/AmazingFeature`)
5. **Abra** um Pull Request

### 🐛 Reportando Bugs

Se encontrar algum bug, por favor:

1. Verifique se o bug já foi reportado
2. Crie uma issue com descrição detalhada
3. Inclua passos para reproduzir o problema
4. Adicione informações do seu ambiente (OS, Python version, etc.)

### 💡 Sugestões de Melhorias

Para sugerir melhorias:

1. Abra uma issue com a tag `enhancement`
2. Descreva a funcionalidade desejada
3. Explique como isso beneficiaria o projeto
4. Se possível, forneça exemplos de implementação

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 📞 Contato

- **Desenvolvedor**: Sidnei Almeida
- **GitHub**: [@sidnei-almeida](https://github.com/sidnei-almeida)
- **Repositório**: [scraper_vitao](https://github.com/sidnei-almeida/scraper_vitao)

## 🙏 Agradecimentos

- **FatSecret Brasil** - Fonte dos dados nutricionais
- **Vitao** - Produtos analisados
- **Comunidade Python** - Bibliotecas e ferramentas utilizadas

---

<div align="center">

**⭐ Se este projeto foi útil para você, considere dar uma estrela! ⭐**

</div>
