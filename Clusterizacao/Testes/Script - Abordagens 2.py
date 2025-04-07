import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from scipy.stats import zscore
from sklearn.cluster import KMeans
import pandas as pd

# 📌 1. Carregar o CSV
file_path = "../../precos_supermercados_4.csv"  # Ajuste o caminho do arquivo se necessário
df = pd.read_csv(file_path)

# Agrupar os preços médios por supermercado
df_mean_prices = df.iloc[:, 1:].mean()

# Aplicar K-Means para classificar supermercados em faixas de preço

df_cluster = pd.DataFrame(df_mean_prices, columns=["Preço Médio"])
df_cluster["Preço Padronizado"] = (df_cluster - df_cluster.mean()) / df_cluster.std()

# Aplicar K-Means
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df_cluster["Cluster"] = kmeans.fit_predict(df_cluster[["Preço Padronizado"]])

# Exibir os grupos de supermercados
print(df_cluster.sort_values("Cluster"))

import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.cluster import KMeans

# Agrupar estatísticas por supermercado
df_numeric = df.iloc[:, 1:]  # Excluir coluna de nomes dos itens
df_mean_prices = df_numeric.mean()  # Média dos preços por supermercado
df_std_prices = df_numeric.std()  # Desvio padrão dos preços
df_median_prices = df_numeric.median()  # Mediana dos preços

# Criar DataFrame para clusterização
df_cluster = pd.DataFrame({
    "Supermercado": df_numeric.columns,
    "Preço Médio": df_mean_prices,
    "Desvio Padrão": df_std_prices,
    "Mediana": df_median_prices
})

# Aplicar padronização (Z-score)
df_cluster_scaled = (df_cluster.iloc[:, 1:] - df_cluster.iloc[:, 1:].mean()) / df_cluster.iloc[:, 1:].std()

# Aplicar K-Means
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df_cluster["Cluster"] = kmeans.fit_predict(df_cluster_scaled)

# Criar gráfico 3D interativo
fig = px.scatter_3d(df_cluster, 
                     x="Preço Médio", 
                     y="Desvio Padrão", 
                     z="Mediana", 
                     color=df_cluster["Cluster"].astype(str),
                     text=df_cluster["Supermercado"],
                     title="Clusters de Supermercados (Preços)",
                     labels={"Cluster": "Grupo"})

fig.update_traces(marker=dict(size=8, opacity=0.8))
fig.show()
