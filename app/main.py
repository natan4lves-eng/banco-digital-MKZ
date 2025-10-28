"""
MKZ BANK - Credit Score Inteligente
Pipeline ETL para Análise de Crédito e Geração de Score

Autor: Equipe MKZ
Data: Outubro 2025
Versão: 1.0
"""

# ============================================================================
# IMPORTS E CONFIGURAÇÕES
# ============================================================================

import pandas as pd
import numpy as np
import warnings
from datetime import datetime
from typing import Dict, Tuple

warnings.filterwarnings('ignore')

# Configurações globais
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: f'{x:.2f}')

# Constantes do projeto
MAX_SCORE = 1000
MIN_SCORE = 0
SCORE_WEIGHTS = {
    'income': 0.25,
    'balance': 0.20,
    'payment_history': 0.30,
    'transaction_frequency': 0.15,
    'account_age': 0.10
}

# ============================================================================
# ETAPA 1: PLANEJAMENTO
# ============================================================================

print("="*80)
print("PROJETO MKZ - CREDIT SCORE INTELIGENTE")
print("="*80)
print("\nOBJETIVO:")
print("Desenvolver sistema de análise de crédito para oferecer produtos")
print("financeiros personalizados baseados em comportamento do cliente\n")

print("INDICADORES:")
print("- Score de crédito (0-1000)")
print("- Categoria do cliente (Premium/Gold/Standard/Risk)")
print("- Limite de crédito sugerido")
print("- Taxa de juros personalizada")
print("="*80 + "\n")

# ============================================================================
# ETAPA 2: ANÁLISE (DATAOPS) - GERANDO DADOS SIMULADOS
# ============================================================================

print("ETAPA 2: ANÁLISE DE DADOS (DataOps)")
print("-" * 80)

# Como não temos um CSV real, vamos criar dados simulados
np.random.seed(42)
n_clientes = 500

# Gerando dataset simulado de clientes bancários
df = pd.DataFrame({
    'customer_id': [f'CLI{str(i).zfill(5)}' for i in range(1, n_clientes + 1)],
    'idade': np.random.randint(18, 70, n_clientes),
    'renda_mensal': np.random.choice(
        [2000, 3500, 5000, 8000, 12000, 20000, 35000], 
        n_clientes, 
        p=[0.15, 0.25, 0.20, 0.15, 0.12, 0.08, 0.05]
    ),
    'saldo_medio': np.random.uniform(100, 50000, n_clientes),
    'num_transacoes_mes': np.random.poisson(25, n_clientes),
    'atrasos_ultimos_12_meses': np.random.choice([0, 1, 2, 3, 5, 8], n_clientes, p=[0.5, 0.25, 0.12, 0.08, 0.03, 0.02]),
    'tempo_cliente_meses': np.random.randint(1, 120, n_clientes),
    'usa_cheque_especial': np.random.choice([0, 1], n_clientes, p=[0.7, 0.3]),
    'limite_atual': np.random.choice([0, 1000, 3000, 5000, 10000], n_clientes, p=[0.2, 0.3, 0.25, 0.15, 0.1])
})

print("Dataset gerado com sucesso!")
print(f"Total de clientes: {len(df)}")
print(f"\nPrimeiras linhas do dataset:")
print(df.head(10))
print(f"\nInformações do dataset:")
print(df.info())
print(f"\nEstatísticas descritivas:")
print(df.describe())

# Verificando dados ausentes
print(f"\n📊 Análise de Qualidade:")
print(f"Valores ausentes: {df.isnull().sum().sum()}")
print(f"Duplicatas: {df.duplicated().sum()}")

# ============================================================================
# ETAPA 3: DESIGN - MODELAGEM DO PIPELINE ETL
# ============================================================================

print("\n" + "="*80)
print("ETAPA 3: DESIGN - ARQUITETURA DO PIPELINE")
print("="*80)
print("""
PIPELINE ETL PROJETADO:

[EXTRACT] → [TRANSFORM] → [LOAD]
    ↓            ↓           ↓
  CSV File   Limpeza    Relatório
             Cálculos   CSV Output
             Score
             Categorias

MODELO DE SCORE:
- Renda (25%): Capacidade de pagamento
- Saldo (20%): Reservas financeiras
- Histórico (30%): Comportamento de pagamento
- Transações (15%): Atividade bancária
- Tempo de conta (10%): Relacionamento com banco

CATEGORIAS:
- Premium: Score ≥ 800 (Taxa 1.2% a.m., Limite até R$ 50k)
- Gold: Score 600-799 (Taxa 1.8% a.m., Limite até R$ 30k)
- Standard: Score 400-599 (Taxa 2.5% a.m., Limite até R$ 15k)
- Risk: Score < 400 (Taxa 3.5% a.m., Limite até R$ 5k)
""")

# ============================================================================
# ETAPA 4: DESENVOLVIMENTO - IMPLEMENTAÇÃO DO ETL
# ============================================================================

print("="*80)
print("ETAPA 4: DESENVOLVIMENTO - IMPLEMENTAÇÃO")
print("="*80 + "\n")

# --- 4.1 EXTRACT ---
def extract_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Extrai e valida os dados de entrada
    
    Args:
        dataframe: DataFrame com dados brutos
        
    Returns:
        DataFrame validado
    """
    print("📥 EXTRACT: Carregando dados...")
    
    required_columns = [
        'customer_id', 'idade', 'renda_mensal', 'saldo_medio',
        'num_transacoes_mes', 'atrasos_ultimos_12_meses',
        'tempo_cliente_meses'
    ]
    
    # Validar colunas obrigatórias
    missing_cols = set(required_columns) - set(dataframe.columns)
    if missing_cols:
        raise ValueError(f"Colunas ausentes: {missing_cols}")
    
    print(f"✅ Dados extraídos: {len(dataframe)} registros")
    return dataframe.copy()

# --- 4.2 TRANSFORM ---
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpa e trata dados inconsistentes
    
    Args:
        df: DataFrame bruto
        
    Returns:
        DataFrame limpo
    """
    print("\n🧹 TRANSFORM: Limpeza de dados...")
    
    df_clean = df.copy()
    
    # Remover duplicatas
    df_clean = df_clean.drop_duplicates(subset=['customer_id'])
    
    # Tratar valores ausentes
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if df_clean[col].isnull().any():
            df_clean[col].fillna(df_clean[col].median(), inplace=True)
    
    # Validar ranges
    df_clean = df_clean[df_clean['idade'] >= 18]
    df_clean = df_clean[df_clean['renda_mensal'] > 0]
    df_clean['saldo_medio'] = df_clean['saldo_medio'].clip(lower=0)
    df_clean['atrasos_ultimos_12_meses'] = df_clean['atrasos_ultimos_12_meses'].clip(lower=0)
    
    print(f"✅ Dados limpos: {len(df_clean)} registros válidos")
    print(f"   Removidos: {len(df) - len(df_clean)} registros")
    
    return df_clean

def calculate_score_components(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula componentes individuais do score
    
    Args:
        df: DataFrame limpo
        
    Returns:
        DataFrame com componentes de score
    """
    print("\n🔢 TRANSFORM: Calculando componentes do score...")
    
    df_scored = df.copy()
    
    # 1. Score de Renda (0-100)
    df_scored['score_renda'] = np.clip(
        (df_scored['renda_mensal'] / 50000) * 100, 0, 100
    )
    
    # 2. Score de Saldo (0-100)
    df_scored['score_saldo'] = np.clip(
        (df_scored['saldo_medio'] / 100000) * 100, 0, 100
    )
    
    # 3. Score de Histórico de Pagamentos (0-100)
    # Quanto menos atrasos, melhor
    df_scored['score_pagamento'] = np.clip(
        100 - (df_scored['atrasos_ultimos_12_meses'] * 15), 0, 100
    )
    
    # 4. Score de Frequência de Transações (0-100)
    df_scored['score_transacoes'] = np.clip(
        (df_scored['num_transacoes_mes'] / 100) * 100, 0, 100
    )
    
    # 5. Score de Tempo de Cliente (0-100)
    df_scored['score_tempo'] = np.clip(
        (df_scored['tempo_cliente_meses'] / 120) * 100, 0, 100
    )
    
    print("✅ Componentes calculados")
    return df_scored

def calculate_final_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula score final ponderado
    
    Args:
        df: DataFrame com componentes
        
    Returns:
        DataFrame com score final
    """
    print("\n📊 TRANSFORM: Calculando score final...")
    
    df_final = df.copy()
    
    # Score final ponderado (0-1000)
    df_final['credit_score'] = (
        df_final['score_renda'] * SCORE_WEIGHTS['income'] +
        df_final['score_saldo'] * SCORE_WEIGHTS['balance'] +
        df_final['score_pagamento'] * SCORE_WEIGHTS['payment_history'] +
        df_final['score_transacoes'] * SCORE_WEIGHTS['transaction_frequency'] +
        df_final['score_tempo'] * SCORE_WEIGHTS['account_age']
    ) * 10  # Escala para 0-1000
    
    df_final['credit_score'] = df_final['credit_score'].clip(MIN_SCORE, MAX_SCORE).round(0).astype(int)
    
    print(f"✅ Score calculado - Média: {df_final['credit_score'].mean():.0f}")
    
    return df_final

def categorize_customers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Categoriza clientes e define limites/taxas
    
    Args:
        df: DataFrame com score
        
    Returns:
        DataFrame com categorias
    """
    print("\n🏷️  TRANSFORM: Categorizando clientes...")
    
    df_cat = df.copy()
    
    # Definir categorias
    def get_category(score):
        if score >= 800:
            return 'Premium'
        elif score >= 600:
            return 'Gold'
        elif score >= 400:
            return 'Standard'
        else:
            return 'Risk'
    
    df_cat['categoria'] = df_cat['credit_score'].apply(get_category)
    
    # Definir limites de crédito
    limite_map = {
        'Premium': 50000,
        'Gold': 30000,
        'Standard': 15000,
        'Risk': 5000
    }
    df_cat['limite_credito_sugerido'] = df_cat['categoria'].map(limite_map)
    
    # Definir taxas de juros (% ao mês)
    taxa_map = {
        'Premium': 1.2,
        'Gold': 1.8,
        'Standard': 2.5,
        'Risk': 3.5
    }
    df_cat['taxa_juros_mensal'] = df_cat['categoria'].map(taxa_map)
    
    # Calcular potencial de receita
    df_cat['receita_potencial_mensal'] = (
        df_cat['limite_credito_sugerido'] * 
        (df_cat['taxa_juros_mensal'] / 100) * 
        0.6  # Assumindo 60% de utilização média
    )
    
    print("✅ Clientes categorizados:")
    print(df_cat['categoria'].value_counts())
    
    return df_cat

# --- 4.3 LOAD ---
def generate_report(df: pd.DataFrame, output_path: str = 'relatorio_credito_mkz.csv') -> None:
    """
    Gera relatório final em CSV
    
    Args:
        df: DataFrame processado
        output_path: Caminho do arquivo de saída
    """
    print(f"\n💾 LOAD: Gerando relatório...")
    
    # Selecionar colunas para o relatório
    report_cols = [
        'customer_id',
        'idade',
        'renda_mensal',
        'saldo_medio',
        'atrasos_ultimos_12_meses',
        'tempo_cliente_meses',
        'credit_score',
        'categoria',
        'limite_credito_sugerido',
        'taxa_juros_mensal',
        'receita_potencial_mensal'
    ]
    
    df_report = df[report_cols].copy()
    
    # Ordenar por score (maior para menor)
    df_report = df_report.sort_values('credit_score', ascending=False)
    
    # Salvar CSV
    df_report.to_csv(output_path, index=False, encoding='utf-8-sig')
    
    print(f"✅ Relatório salvo: {output_path}")
    print(f"   Total de registros: {len(df_report)}")
    
    return df_report

# ============================================================================
# EXECUTAR PIPELINE COMPLETO
# ============================================================================

def run_etl_pipeline(input_df: pd.DataFrame) -> pd.DataFrame:
    """
    Executa o pipeline ETL completo
    
    Args:
        input_df: DataFrame de entrada
        
    Returns:
        DataFrame processado
    """
    print("\n" + "="*80)
    print("EXECUTANDO PIPELINE ETL COMPLETO")
    print("="*80)
    
    # Extract
    df_extracted = extract_data(input_df)
    
    # Transform
    df_clean = clean_data(df_extracted)
    df_scored = calculate_score_components(df_clean)
    df_final = calculate_final_score(df_scored)
    df_categorized = categorize_customers(df_final)
    
    # Load
    df_report = generate_report(df_categorized)
    
    return df_report

# Executar pipeline
df_final_report = run_etl_pipeline(df)

# ============================================================================
# ETAPA 5: TESTES (SHIFT-LEFT)
# ============================================================================

print("\n" + "="*80)
print("ETAPA 5: TESTES E VALIDAÇÃO (Shift-Left)")
print("="*80 + "\n")

def run_quality_tests(df: pd.DataFrame) -> Dict[str, bool]:
    """
    Executa testes de qualidade nos dados
    
    Args:
        df: DataFrame a ser testado
        
    Returns:
        Dicionário com resultados dos testes
    """
    results = {}
    
    # Teste 1: Verificar valores nulos
    print("✓ Teste 1: Valores nulos")
    results['no_nulls'] = df.isnull().sum().sum() == 0
    print(f"  Resultado: {'PASS' if results['no_nulls'] else 'FAIL'}")
    
    # Teste 2: Score no range correto
    print("\n✓ Teste 2: Range do score (0-1000)")
    results['score_range'] = ((df['credit_score'] >= 0) & (df['credit_score'] <= 1000)).all()
    print(f"  Resultado: {'PASS' if results['score_range'] else 'FAIL'}")
    print(f"  Min: {df['credit_score'].min()}, Max: {df['credit_score'].max()}")
    
    # Teste 3: Todas as categorias presentes
    print("\n✓ Teste 3: Categorias válidas")
    expected_categories = {'Premium', 'Gold', 'Standard', 'Risk'}
    found_categories = set(df['categoria'].unique())
    results['valid_categories'] = found_categories.issubset(expected_categories)
    print(f"  Resultado: {'PASS' if results['valid_categories'] else 'FAIL'}")
    print(f"  Categorias encontradas: {found_categories}")
    
    # Teste 4: Limites de crédito positivos
    print("\n✓ Teste 4: Limites de crédito positivos")
    results['positive_limits'] = (df['limite_credito_sugerido'] > 0).all()
    print(f"  Resultado: {'PASS' if results['positive_limits'] else 'FAIL'}")
    
    # Teste 5: Consistência de dados
    print("\n✓ Teste 5: Customer IDs únicos")
    results['unique_ids'] = df['customer_id'].is_unique
    print(f"  Resultado: {'PASS' if results['unique_ids'] else 'FAIL'}")
    
    # Resumo
    print("\n" + "-"*80)
    total_tests = len(results)
    passed_tests = sum(results.values())
    print(f"RESUMO DOS TESTES: {passed_tests}/{total_tests} testes passaram")
    print("-"*80)
    
    return results

# Executar testes
test_results = run_quality_tests(df_final_report)

# ============================================================================
# ANÁLISE ESTATÍSTICA E INSIGHTS
# ============================================================================

print("\n" + "="*80)
print("ANÁLISE ESTATÍSTICA E INSIGHTS DE NEGÓCIO")
print("="*80 + "\n")

# Distribuição por categoria
print("📊 DISTRIBUIÇÃO POR CATEGORIA:")
category_stats = df_final_report.groupby('categoria').agg({
    'customer_id': 'count',
    'credit_score': 'mean',
    'renda_mensal': 'mean',
    'limite_credito_sugerido': 'mean',
    'receita_potencial_mensal': 'sum'
}).round(2)
category_stats.columns = ['Qtd_Clientes', 'Score_Médio', 'Renda_Média', 'Limite_Médio', 'Receita_Total']
print(category_stats)

# Estatísticas gerais
print(f"\n📈 ESTATÍSTICAS GERAIS:")
print(f"Score Médio Geral: {df_final_report['credit_score'].mean():.0f}")
print(f"Score Mediano: {df_final_report['credit_score'].median():.0f}")
print(f"Desvio Padrão: {df_final_report['credit_score'].std():.2f}")
print(f"\nReceita Potencial Total: R$ {df_final_report['receita_potencial_mensal'].sum():,.2f}/mês")
print(f"Receita Potencial Anual: R$ {df_final_report['receita_potencial_mensal'].sum() * 12:,.2f}")

# Top 10 clientes
print(f"\n🏆 TOP 10 CLIENTES (MAIOR SCORE):")
print(df_final_report.head(10)[['customer_id', 'credit_score', 'categoria', 'limite_credito_sugerido']])

print("\n" + "="*80)
print("PIPELINE ETL CONCLUÍDO COM SUCESSO!")
print("="*80)