import json
import pandas as pd
import os

file_path = os.path.join("dados", "vendas.json")
file = open(file_path, encoding="utf-8")

print(data)

df = pd.DataFrame.from_dict(data)

print(df)

df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')

file.close()