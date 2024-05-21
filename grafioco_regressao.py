import pandas as pd
import numpy as np

df_cidades = pd.read_excel("grafico_dispersao.ods")

print(type(df_cidades))

df_cidades.head(21)

print(df_cidades.dtypes)

print(df_cidades[df_cidades["Y"] > 300])

df_cidades.plot.scatter(x="X", y="Y")

df_cidades["Y"].mean()

df_cidades["Y"].describe()

