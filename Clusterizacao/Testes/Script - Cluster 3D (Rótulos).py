import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import plotly.express as px
from scipy.spatial.distance import pdist, squareform

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

print(df_scaled)

#%% Identificação da quantidade de clusters (Método Elbow)
max_clusters = min(10, df_scaled.shape[0])
K = range(1, max_clusters + 1)
wcss = []

n_clusters = 6  # Ajuste conforme a análise do Elbow/Silhueta
kmeans_final = KMeans(n_clusters=n_clusters, init="random", random_state=100, n_init=10)
df_pivot["cluster_kmeans"] = kmeans_final.fit_predict(df_scaled)

#%% Visualização dos clusters - Ajustando para menos de 3 colunas
df_pivot["cluster_kmeans"] = df_pivot["cluster_kmeans"].astype("category")

#%% Estatísticas descritivas por cluster
cluster_summary = df_pivot.groupby("cluster_kmeans").describe()

# Restaurando "Item" como coluna para facilitar a identificação nos gráficos
df_pivot.reset_index(inplace=True)

# Convertendo cluster para string para evitar problemas na visualização
df_pivot["cluster_kmeans"] = df_pivot["cluster_kmeans"].astype(str)

# Visualização 3D apenas se houver pelo menos 3 supermercados
if df_pivot.shape[1] >= 4:  # Precisamos de pelo menos 3 colunas + "Item"
    fig = px.scatter_3d(df_pivot,
                        x=df_pivot.columns[4],  # Primeira coluna de preços
                        y=df_pivot.columns[2],  # Segunda coluna de preços
                        z=df_pivot.columns[3],  # Terceira coluna de preços
                        color="cluster_kmeans",
                        title="Clusters dos Produtos",
                        hover_name="Item")  # Exibir nome do produto no hover
    fig.write_image(file='./Resultados/Cluster 3D (Rótulos).png', format='png')
    fig.show()
else:
    print("Número insuficiente de supermercados para visualização 3D.")