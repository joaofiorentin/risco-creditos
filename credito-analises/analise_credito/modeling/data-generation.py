from faker import Faker
import pandas as pd

# Inicializando o Faker
fake = Faker()

# Função para gerar um cliente com dados fictícios
def gerar_cliente():
    return {
        'nome': fake.name(),
        'idade': fake.random_int(min=18, max=80),
        'renda': fake.random_int(min=1500, max=10000),
        'historico_credito': fake.random_element(elements=('bom', 'regular', 'ruim')),
        'inadimplente': fake.random_element(elements=(0, 1)),  # 0 = Não, 1 = Sim
        'pontuacao_credito': fake.random_int(min=300, max=850),  # Pontuação de crédito (FICO)
        'tipo_emprego': fake.random_element(elements=('assalariado', 'autônomo', 'empreendedor')),
        'divida_atual': fake.random_int(min=0, max=5000)  # Dívida atual
    }

# Gerar 1000 clientes
clientes = [gerar_cliente() for _ in range(1000)]

# Converter para DataFrame para facilitar análise
df = pd.DataFrame(clientes)

# Exibir as primeiras linhas do DataFrame
print(df.head())

df.to_csv('clientes_credito.csv', index=False)