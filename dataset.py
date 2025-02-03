import json
import pandas as pd

file = open(r'dados\vendas.json')
data = json.load(file)

print(data)

df = pd.DataFrame.from_dict(data)

print(df)

df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')

file.close()