import pandas as pd

# Carregar o dataset
df = pd.read_csv('C:/Users/joao.fiorentin/Downloads/analise-credito/credito-analises/data/clientes_credito.csv')

# Verificar valores nulos
print(df.isnull().sum())

# Verificar duplicados
print(f'Duplicados: {df.duplicated().sum()}')

# Remover duplicados
df = df.drop_duplicates()

# Preencher ou remover valores nulos (se houver)
df = df.dropna()

# Convertendo variáveis categóricas em variáveis numéricas
df['historico_credito'] = df['historico_credito'].map({'bom': 0, 'regular': 1, 'ruim': 2})
df['tipo_emprego'] = df['tipo_emprego'].map({'assalariado': 0, 'autônomo': 1, 'empreendedor': 2})

# Exibir as primeiras linhas após transformação
print(df.head())
