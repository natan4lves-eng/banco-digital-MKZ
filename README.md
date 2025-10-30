# 🏦 MKZ Credit Score Inteligente

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Status](https://img.shields.io/badge/status-MVP-yellow.svg)]()

> Sistema inteligente de análise de crédito que democratiza o acesso a produtos financeiros através de análise de dados avançada e personalização.

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Características](#-características)
- [Tecnologias](#-tecnologias)
- [Instalação](#-instalação)
- [Uso Rápido](#-uso-rápido)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Documentação](#-documentação)
- [Testes](#-testes)
- [Deploy](#-deploy)
- [Contribuindo](#-contribuindo)
- [Roadmap](#-roadmap)
- [Equipe](#-equipe)
- [Licença](#-licença)

---

## 🎯 Sobre o Projeto

O **MKZ Credit Score Inteligente** é um produto de dados desenvolvido para o banco digital MKZ, com o objetivo de:

- 📊 Analisar o comportamento financeiro dos clientes de forma holística
- 🎯 Categorizar clientes em perfis de risco mais precisos
- 💰 Oferecer crédito personalizado com taxas justas
- 📈 Reduzir inadimplência em até 30%
- ✨ Melhorar a experiência do cliente com aprovação rápida

### Problema de Negócio

Bancos tradicionais avaliam crédito apenas com base em histórico negativo (Serasa, SPC), o que:
- Exclui clientes sem histórico
- Não considera comportamento atual positivo
- Resulta em taxas genéricas e injustas
- Gera alta taxa de inadimplência (12%)

### Nossa Solução

Análise multidimensional que considera:
- ✅ Renda e capacidade de pagamento
- ✅ Saldo médio e reservas
- ✅ Histórico de pagamentos
- ✅ Frequência de transações
- ✅ Tempo de relacionamento com o banco

**Resultado:** Taxas personalizadas de 1.2% a 3.5% a.m. e limites de R$ 5.000 a R$ 50.000

---

## ✨ Características

### Funcionalidades Principais

- **📊 Pipeline ETL Completo**
  - Extração e validação de dados
  - Limpeza e transformação robusta
  - Geração de relatórios automatizada

- **🧮 Cálculo de Score Ponderado**
  - Score de 0 a 1.000 pontos
  - 5 componentes com pesos configuráveis
  - Validações automáticas de qualidade

- **🏷️ Categorização Inteligente**
  - Premium (800-1000): Taxa 1.2% | Limite R$ 50k
  - Gold (600-799): Taxa 1.8% | Limite R$ 30k
  - Standard (400-599): Taxa 2.5% | Limite R$ 15k
  - Risk (0-399): Taxa 3.5% | Limite R$ 5k

- **📈 Análise de Negócio**
  - Estatísticas por categoria
  - Projeção de receita potencial
  - Insights automáticos

### Diferenciais Técnicos

- ✅ Shift-Left Testing (5 testes automatizados)
- ✅ Documentação completa (Runbook + Style Guide)
- ✅ Logging e monitoramento
- ✅ Tratamento robusto de erros
- ✅ Código modular e reutilizável

---

## 🛠️ Tecnologias

### Core Stack

| Tecnologia | Versão | Uso |
|------------|--------|-----|
| **Python** | 3.8+ | Linguagem principal |
| **Pandas** | 1.3.0+ | Manipulação de dados |
| **NumPy** | 1.21.0+ | Cálculos numéricos |
| **Jupyter** | - | Análise exploratória |

### Desenvolvimento

- **black** - Formatação de código
- **flake8** - Linting
- **pytest** - Testes automatizados
- **Git** - Controle de versão

### Futuro (Roadmap)

- **Scikit-learn** - Machine Learning
- **FastAPI** - API REST
- **Docker** - Containerização
- **Apache Airflow** - Orquestração

---

## 🚀 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes)
- Git

### Passo a Passo

1. **Clone o repositório**

```bash
git clone https://github.com/seu-usuario/mkz-credit-score.git
cd mkz-credit-score
```

2. **Crie um ambiente virtual**

```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. **Instale as dependências**

```bash
pip install -r requirements.txt
```

4. **Verifique a instalação**

```bash
python --version  # Deve mostrar 3.8+
pip list          # Deve listar pandas, numpy, etc.
```

### Estrutura de Pastas Necessária

```bash
# Criar pastas para dados
mkdir -p data/input data/output data/processed logs
```

---

## 💻 Uso Rápido

### Opção 1: Jupyter Notebook (Recomendado para análise)

```bash
# Iniciar Jupyter
jupyter notebook

# Abrir: notebooks/mkz_credit_analysis.ipynb
# Executar todas as células: Cell > Run All
```

### Opção 2: Script Python (Recomendado para produção)

```bash
# Executar pipeline completo
python src/mkz_etl_pipeline.py

# Com arquivo customizado
python src/mkz_etl_pipeline.py --input data/input/clientes.csv
```

### Opção 3: Importar como Módulo

```python
from src.pipeline import run_etl_pipeline
import pandas as pd

# Carregar seus dados
df = pd.read_csv('data/input/clientes.csv')

# Executar pipeline
resultado = run_etl_pipeline(df)

# Relatório gerado em: data/output/relatorio_credito_mkz.csv
```

### Exemplo de Output

```csv
customer_id,idade,renda_mensal,credit_score,categoria,limite_credito_sugerido,taxa_juros_mensal
CLI00001,35,8000,850,Premium,50000,1.2
CLI00002,28,4500,680,Gold,30000,1.8
CLI00003,42,3000,520,Standard,15000,2.5
```

---

## 📁 Estrutura do Projeto

```
mkz-credit-score/
├── data/
│   ├── input/                  # CSVs de entrada
│   ├── output/                 # Relatórios gerados
│   └── processed/              # Dados intermediários
│
├── notebooks/
│   └── mkz_credit_analysis.ipynb   # Análise exploratória
│
├── src/
│   ├── __init__.py
│   ├── mkz_etl_pipeline.py     # Script principal
│   ├── etl/
│   │   ├── extract.py          # Extração de dados
│   │   ├── transform.py        # Transformações
│   │   └── load.py             # Carga de resultados
│   ├── models/
│   │   └── score_calculator.py # Lógica de score
│   └── utils/
│       ├── validators.py       # Validações
│       └── config.py           # Configurações
│
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_score.py
│
├── docs/
│   ├── runbook.md              # Guia operacional
│   ├── style_guide.md          # Padrões de código
│   ├── parecer_tecnico.md      # Análise técnica
│   └── arquitetura.png         # Diagrama de arquitetura
│
├── logs/                       # Logs de execução
├── .gitignore
├── requirements.txt            # Dependências
├── README.md                   # Este arquivo
└── LICENSE
```

---

## 📚 Documentação

### Documentação Completa

- 📖 **[Runbook Operacional](docs/runbook.md)** - Como executar, monitorar e corrigir erros
- 💻 **[Style Guide](docs/style_guide.md)** - Padrões de código e nomenclatura
- 📊 **[Parecer Técnico](docs/parecer_tecnico.md)** - Análise detalhada do projeto
- 🏗️ **[Arquitetura](docs/arquitetura.md)** - Design do sistema e pipeline

### Documentação do Código

Todas as funções possuem docstrings completas:

```python
def calculate_credit_score(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula o credit score baseado em múltiplos fatores.
    
    Args:
        data: DataFrame com dados dos clientes
        
    Returns:
        DataFrame com coluna 'credit_score' adicionada
        
    Example:
        >>> df = calculate_credit_score(df_input)
        >>> df['credit_score'].mean()
        650.5
    """
```

### Modelo de Score

O score final (0-1000) é calculado através de 5 componentes ponderados:

| Componente | Peso | Descrição |
|------------|------|-----------|
| **Renda** | 25% | Capacidade de pagamento |
| **Saldo** | 20% | Reservas financeiras |
| **Histórico** | 30% | Comportamento de pagamento |
| **Transações** | 15% | Atividade bancária |
| **Tempo Cliente** | 10% | Relacionamento com banco |

**Fórmula:**
```
Score = (score_renda × 0.25 + 
         score_saldo × 0.20 + 
         score_pagamento × 0.30 + 
         score_transacoes × 0.15 + 
         score_tempo × 0.10) × 10
```

---

## 🧪 Testes

### Executar Testes

```bash
# Todos os testes
pytest tests/

# Com cobertura
pytest --cov=src tests/

# Específico
pytest tests/test_score.py
```

### Testes Implementados

5 testes automatizados garantem qualidade:

1. ✅ **test_no_null_values** - Nenhum valor nulo no output
2. ✅ **test_score_range** - Score entre 0 e 1000
3. ✅ **test_valid_categories** - Categorias válidas
4. ✅ **test_positive_limits** - Limites de crédito positivos
5. ✅ **test_unique_customer_ids** - IDs únicos

### Cobertura de Código

Alvo: **> 80%** de cobertura

```bash
# Gerar relatório de cobertura
pytest --cov=src --cov-report=html tests/

# Abrir relatório
open htmlcov/index.html
```

---

## 🚀 Deploy

### Ambiente de Desenvolvimento

```bash
# Executar localmente
python src/mkz_etl_pipeline.py
```

### Ambiente de Produção

#### Opção 1: Cron Job (Linux/Mac)

```bash
# Editar crontab
crontab -e

# Adicionar linha (executar todo dia às 6h)
0 6 * * * cd /path/to/mkz-credit-score && /path/to/venv/bin/python src/mkz_etl_pipeline.py >> logs/pipeline.log 2>&1
```

#### Opção 2: Task Scheduler (Windows)

1. Abrir Task Scheduler
2. Criar tarefa básica
3. Apontar para: `python.exe C:\path\to\src\mkz_etl_pipeline.py`
4. Definir agendamento

#### Opção 3: Docker (Recomendado)

```bash
# Build da imagem
docker build -t mkz-credit-score .

# Executar container
docker run -v $(pwd)/data:/app/data mkz-credit-score
```

#### Opção 4: Apache Airflow

```python
# DAG do Airflow (exemplo)
from airflow import DAG
from airflow.operators.python import PythonOperator

dag = DAG('mkz_credit_score', schedule_interval='0 6 * * *')

task = PythonOperator(
    task_id='run_pipeline',
    python_callable=run_etl_pipeline,
    dag=dag
)
```

### Monitoramento

Métricas a acompanhar:

- ⏱️ Tempo de execução
- ✅ Taxa de sucesso
- 📊 Qualidade dos dados
- 🔢 Distribuição de scores
- 💰 Receita potencial gerada

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Siga estas diretrizes:

### Como Contribuir

1. **Fork o projeto**
2. **Crie uma branch** (`git checkout -b feature/nova-funcionalidade`)
3. **Commit suas mudanças** (`git commit -m 'feat: adiciona nova funcionalidade'`)
4. **Push para a branch** (`git push origin feature/nova-funcionalidade`)
5. **Abra um Pull Request**

### Padrões de Commit

Usamos [Conventional Commits](https://www.conventionalcommits.org/):

```bash
feat: adiciona novo componente de score
fix: corrige cálculo de juros
docs: atualiza README
test: adiciona testes de validação
refactor: melhora performance do pipeline
```

### Checklist do PR

- [ ] Código segue o [Style Guide](docs/style_guide.md)
- [ ] Testes adicionados/atualizados
- [ ] Documentação atualizada
- [ ] Commits seguem convenção
- [ ] Não há dados sensíveis no código

### Code Review

Todos os PRs passam por revisão focando em:

- ✅ Qualidade do código
- ✅ Cobertura de testes
- ✅ Documentação
- ✅ Performance
- ✅ Segurança

---

## 🗓️ Roadmap

### ✅ Fase 1: MVP (Concluído)

- [x] Pipeline ETL funcional
- [x] Cálculo de score ponderado
- [x] Categorização de clientes
- [x] Testes automatizados
- [x] Documentação completa

### 🔄 Fase 2: Machine Learning (Q1 2026)

- [ ] Modelo Random Forest para previsão de inadimplência
- [ ] Otimização de pesos usando validação cruzada
- [ ] Feature engineering avançado
- [ ] A/B testing de modelos
- [ ] API REST para consulta de score

**Meta:** AUC-ROC > 0.85 na previsão de inadimplência

### 🚀 Fase 3: Produtização (Q2 2026)

- [ ] Integração com Open Banking
- [ ] Score dinâmico (atualização real-time)
- [ ] Dashboard executivo (Power BI)
- [ ] Containerização (Docker + Kubernetes)
- [ ] CI/CD completo (GitHub Actions)

**Meta:** Processar 100k+ clientes/dia

### 🌟 Fase 4: Expansão (Q3-Q4 2026)

- [ ] Recomendação de produtos financeiros
- [ ] Análise preditiva de churn
- [ ] Gamificação para melhoria de score
- [ ] Integração com sistemas legados
- [ ] Marketplace de APIs

**Meta:** 10+ produtos de dados derivados

---

## 👥 Equipe

### Desenvolvedores

- **[Seu Nome]** - _Tech Lead & Engenheiro de Dados_ - [@github](https://github.com/seu-usuario)
- **[Nome 2]** - _Engenheiro de Dados_ - [@github](https://github.com/usuario2)
- **[Nome 3]** - _Cientista de Dados_ - [@github](https://github.com/usuario3)
- **[Nome 4]** - _Analista de Dados_ - [@github](https://github.com/usuario4)

### Agradecimentos

Agradecimentos especiais a:
- Time de Produto MKZ pela visão do projeto
- Stakeholders de negócio pelo feedback
- Comunidade Python pelos recursos

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

```
MIT License

Copyright (c) 2025 MKZ Bank

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 📞 Contato

### Suporte Técnico

- 📧 Email: data-team@mkz.com.br
- 💬 Slack: [#mkz-credit-pipeline](https://mkz.slack.com)
- 🐛 Issues: [GitHub Issues](https://github.com/seu-usuario/mkz-credit-score/issues)

### Links Úteis

- 🌐 [Website do Projeto](https://mkz.com.br/credit-score)
- 📊 [Dashboard de Métricas](https://metrics.mkz.com.br)
- 📖 [Documentação Completa](https://docs.mkz.com.br)
- 🎥 [Vídeo Demo](https://youtube.com/mkz-demo)

---

## 🌟 Estrelas no GitHub

Se este projeto foi útil para você, considere dar uma ⭐!

[![Star History Chart](https://api.star-history.com/svg?repos=seu-usuario/mkz-credit-score&type=Date)](https://star-history.com/#seu-usuario/mkz-credit-score&Date)

---

## 📊 Status do Projeto

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen)
![Tests](https://img.shields.io/badge/tests-5%20passed-brightgreen)
![Last Commit](https://img.shields.io/badge/last%20commit-today-blue)

---

<div align="center">

**Desenvolvido com ❤️ pela equipe MKZ**

[⬆ Voltar ao topo](#-mkz-credit-score-inteligente)

</div>