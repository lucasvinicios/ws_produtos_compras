from scipy.spatial.distance import pdist, squareform
from scipy.stats import zscore
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#%% Importando o banco de dados
file_path = "../precos_supermercados.csv"  # Ajuste o caminho conforme necessário
df = pd.read_csv(file_path, sep=',', decimal=',')

#%% Transformação dos dados
df_melted = df.melt(id_vars=["Item"], var_name="Supermercado", value_name="Preço")
df_melted["Preço"] = pd.to_numeric(df_melted["Preço"], errors="coerce")
df_melted.dropna(inplace=True)

# Criando uma tabela pivot para clusterização
df_pivot = df_melted.pivot(index="Item", columns="Supermercado", values="Preço")

# Preenchendo valores ausentes com a média do produto, se a média for NaN, preenche com 0
df_pivot = df_pivot.apply(lambda x: x.fillna(x.mean()) if x.mean() is not np.nan else x.fillna(0), axis=1)

#%% Padronização dos dados (Z-score)
df_scaled = df_pivot.apply(zscore)

# Calculando a matriz de distâncias euclidianas
dist_matrix = squareform(pdist(df_scaled, metric="euclidean"))

# Elevando ao quadrado para obter a distância euclidiana quadrática
dist_matrix_squared = dist_matrix ** 2

# Criando um DataFrame com nomes dos produtos nas colunas e linhas
df_dist_squared = pd.DataFrame(dist_matrix_squared, index=df_pivot.index, columns=df_pivot.index)
df_dist_squared.to_csv("./Resultados/distancia_euclidiana_quadratica.csv", sep=",", decimal=",")
# Exibindo a matriz de distâncias quadráticas
print(df_dist_squared)

# Plotando um heatmap para melhor visualização
plt.figure(figsize=(10, 8))
sns.heatmap(df_dist_squared, cmap="coolwarm", annot=True, fmt=".2f")
plt.title("Matriz de Distâncias Euclidianas Quadráticas entre Produtos")
plt.show()
