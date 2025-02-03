import json
import pandas as pd
import os

# Define o caminho do arquivo corretamente para rodar no Streamlit Cloud
file_path = os.path.join("dados", "vendas.json")

# Verifica se o arquivo existe antes de tentar abri-lo
if os.path.exists(file_path):
    with open(file_path, encoding="utf-8") as file:
        data = json.load(file)  # Carrega os dados corretamente
else:
    raise FileNotFoundError(f"Erro: O arquivo '{file_path}' não foi encontrado.")

# Converte o JSON para DataFrame
df = pd.DataFrame.from_dict(data)

# Converte a coluna 'Data da Compra' para datetime
if 'Data da Compra' in df.columns:
    df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')

# Exibe as 5 primeiras linhas para debug (opcional)
print(df.head())
