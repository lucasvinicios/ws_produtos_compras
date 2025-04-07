import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.cluster import KMeans
import plotly.express as px

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
print(max_clusters)
K = range(1, max_clusters + 1)
wcss = []

#%% Clusterização com K-Means
n_clusters = 6  # Ajuste conforme a análise do Elbow/Silhueta
kmeans_final = KMeans(n_clusters=n_clusters, init="random", random_state=100, n_init=10)
df_pivot["cluster_kmeans"] = kmeans_final.fit_predict(df_scaled)

#%% Visualização dos clusters - Ajustando para menos de 3 colunas
df_pivot["cluster_kmeans"] = df_pivot["cluster_kmeans"].astype("category")

if df_pivot.shape[1] >= 3:  # Se houver pelo menos 3 supermercados
    fig = px.scatter_3d(df_pivot,
                        x=df_pivot.columns[0],
                        y=df_pivot.columns[1],
                        z=df_pivot.columns[2],
                        color=df_pivot["cluster_kmeans"].astype(str),
                        title="Clusters dos Produtos")
    fig.write_image(file='./Resultados/Cluster 3D.png', format='png')
    fig.show()
else:
    print("Número insuficiente de supermercados para visualização 3D.")