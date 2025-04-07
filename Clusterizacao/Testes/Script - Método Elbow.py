import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore
from sklearn.cluster import KMeans


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

#%% Identificação da quantidade de clusters (Método Elbow)
max_clusters = min(10, df_scaled.shape[0])
K = range(1, max_clusters + 1)
wcss = []

for k in K:
    kmeans = KMeans(n_clusters=k, init="random", random_state=100, n_init=10)
    kmeans.fit(df_scaled)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10, 5))
plt.plot(K, wcss, marker="o")
plt.xlabel("Número de Clusters")
plt.ylabel("WCSS (Within-Cluster Sum of Squares)")
plt.title("Método Elbow")
plt.savefig("./Resultados/Método Elbow.png")
plt.show()