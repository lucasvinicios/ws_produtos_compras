from scipy.spatial.distance import pdist, squareform
from scipy.stats import zscore
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#%% Importando o banco de dados
file_path = "../precos_supermercados.csv"  # Ajuste o caminho conforme necessário
df = pd.read_csv(file_path, sep=',', decimal=',')

#%% Transformação dos dados
df_melted = df.melt(id_vars=["Item"], var_name="Supermercado", value_name="Preço")
df_melted["Preço"] = pd.to_numeric(df_melted["Preço"], errors="coerce")
df_melted.dropna(inplace=True)

print(df_melted)

# Criando uma tabela pivot para clusterização
df_pivot = df_melted.pivot(index="Item", columns="Supermercado", values="Preço")

print(df_pivot)
# Preenchendo valores ausentes com a média do produto, se a média for NaN, preenche com 0
df_pivot = df_pivot.apply(lambda x: x.fillna(x.mean()) if x.mean() is not np.nan else x.fillna(0), axis=1)

#%% Padronização dos dados (Z-score)
df_scaled = df_pivot.apply(zscore)

print(df_scaled)
exit()


# Calculando a matriz de distâncias euclidianas
dist_matrix = squareform(pdist(df_scaled, metric="euclidean"))

# Garantindo que os nomes dos produtos sejam os índices e colunas corretamente
df_dist = pd.DataFrame(dist_matrix, index=df_pivot.index, columns=df_pivot.index).round(2)
df_dist.to_csv("./Resultados/distancia_euclidiana.csv", sep=",", decimal=",", encoding="utf-8")
# Exibindo a matriz de distâncias
print(df_dist)

# Plotando um heatmap para melhor visualização
plt.figure(figsize=(10, 8))
sns.heatmap(df_dist, cmap="coolwarm", annot=True, fmt=".2f")
plt.title("Matriz de Distâncias Euclidianas entre Produtos")
plt.show()