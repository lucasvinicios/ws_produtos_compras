# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from scipy.stats import zscore
# from sklearn.cluster import KMeans
# from sklearn.metrics import silhouette_score
# import plotly.express as px

# #%% Importando o banco de dados
# file_path = "../precos_supermercados.csv"  # Ajuste o caminho conforme necessário
# df = pd.read_csv(file_path, sep=',', decimal=',')

# #%% Transformação dos dados
# df_melted = df.melt(id_vars=["Item"], var_name="Supermercado", value_name="Preço")
# df_melted["Preço"] = pd.to_numeric(df_melted["Preço"], errors="coerce")
# df_melted.dropna(inplace=True)

# # Criando uma tabela pivot para clusterização
# df_pivot = df_melted.pivot(index="Item", columns="Supermercado", values="Preço")

# # Preenchendo valores ausentes com a média do produto
# df_pivot = df_pivot.apply(lambda x: x.fillna(x.mean()), axis=1)

# #%% Padronização dos dados (Z-score)
# df_scaled = df_pivot.apply(zscore)

# #%% Identificação da quantidade de clusters (Método Elbow)
# max_clusters = min(10, df_scaled.shape[0])
# K = range(1, max_clusters + 1)
# wcss = []

# for k in K:
#     kmeans = KMeans(n_clusters=k, init="random", random_state=100, n_init=10)
#     kmeans.fit(df_scaled)
#     wcss.append(kmeans.inertia_)

# plt.figure(figsize=(10, 5))
# plt.plot(K, wcss, marker="o")
# plt.xlabel("Número de Clusters")
# plt.ylabel("WCSS (Within-Cluster Sum of Squares)")
# plt.title("Método Elbow")
# plt.show()

# #%% Identificação da quantidade de clusters (Método da Silhueta)
# silhouette = []
# if max_clusters > 2:  # Método da Silhueta requer pelo menos 2 clusters
#     I = range(2, max_clusters + 1)
#     for i in I:
#         kmeans = KMeans(n_clusters=i, init="random", random_state=100, n_init=10)
#         labels = kmeans.fit_predict(df_scaled)
#         silhouette.append(silhouette_score(df_scaled, labels))

#     plt.figure(figsize=(10, 5))
#     plt.plot(range(2, max_clusters + 1), silhouette, marker="o", color="purple")
#     plt.xlabel("Número de Clusters")
#     plt.ylabel("Silhueta Média")
#     plt.title("Método da Silhueta")
#     plt.axvline(x=silhouette.index(max(silhouette)) + 2, linestyle="dotted", color="red")
#     plt.show()

# #%% Clusterização com K-Means
# n_clusters = 3  # Ajuste conforme a análise do Elbow/Silhueta
# kmeans_final = KMeans(n_clusters=n_clusters, init="random", random_state=100, n_init=10)
# df_pivot["cluster_kmeans"] = kmeans_final.fit_predict(df_scaled)

# #%% Visualização dos clusters
# df_pivot["cluster_kmeans"] = df_pivot["cluster_kmeans"].astype("category")

# fig = px.scatter_3d(df_pivot,
#                     x=df_pivot.columns[0],
#                     y=df_pivot.columns[1],
#                     z=df_pivot.columns[2],
#                     color=df_pivot["cluster_kmeans"].astype(str),
#                     title="Clusters dos Produtos")
# fig.show()

# #%% Estatísticas descritivas por cluster
# cluster_summary = df_pivot.groupby("cluster_kmeans").describe()
# print(cluster_summary)

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

#%% Identificação da quantidade de clusters (Método Elbow)
max_clusters = min(10, df_scaled.shape[0])
print(max_clusters)
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
plt.show()


silhouette = []
n_samples = df_scaled.shape[0]

# O método da Silhueta requer pelo menos 2 clusters e pelo menos 3 amostras
if n_samples > 2:
    max_silhouette_clusters = min(n_samples - 1, max_clusters)  # Garante clusters < n_samples
    I = range(2, max_silhouette_clusters + 1)  
    for i in I:
        kmeans = KMeans(n_clusters=i, init="random", random_state=100, n_init=10)
        labels = kmeans.fit_predict(df_scaled)

        if len(set(labels)) > 1:  # Verifica se há mais de um cluster
            silhouette.append(silhouette_score(df_scaled, labels))
        else:
            silhouette.append(-1)  # Valor inválido para evitar erro

    plt.figure(figsize=(10, 5))
    plt.plot(range(2, max_silhouette_clusters + 1), silhouette, marker="o", color="purple")
    plt.xlabel("Número de Clusters")
    plt.ylabel("Silhueta Média")
    plt.title("Método da Silhueta")

    best_k = silhouette.index(max(silhouette)) + 2  # Melhor k
    plt.axvline(x=best_k, linestyle="dotted", color="red")
    plt.show()
else:
    print("Amostras insuficientes para calcular a Silhueta.")



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
    # fig.show()
else:
    print("Número insuficiente de supermercados para visualização 3D.")



#%% Estatísticas descritivas por cluster
cluster_summary = df_pivot.groupby("cluster_kmeans").describe()
print(cluster_summary)

# Restaurando "Item" como coluna para facilitar a identificação nos gráficos
df_pivot.reset_index(inplace=True)

# Convertendo cluster para string para evitar problemas na visualização
df_pivot["cluster_kmeans"] = df_pivot["cluster_kmeans"].astype(str)

# Visualização 3D apenas se houver pelo menos 3 supermercados
if df_pivot.shape[1] >= 4:  # Precisamos de pelo menos 3 colunas + "Item"
    fig = px.scatter_3d(df_pivot,
                        x=df_pivot.columns[1],  # Primeira coluna de preços
                        y=df_pivot.columns[2],  # Segunda coluna de preços
                        z=df_pivot.columns[3],  # Terceira coluna de preços
                        color="cluster_kmeans",
                        title="Clusters dos Produtos",
                        hover_name="Item")  # Exibir nome do produto no hover
    # fig.show()
else:
    print("Número insuficiente de supermercados para visualização 3D.")

# Criar um DataFrame associando os produtos aos clusters
df_clusters = df_pivot.copy()
df_clusters["Produto"] = df_clusters.index  # Adiciona os produtos
df_clusters = df_clusters[["Produto", "cluster_kmeans"]]  # Mantém apenas essas colunas

# Ordenar os produtos dentro de cada cluster para melhor visualização
df_clusters = df_clusters.sort_values(by="cluster_kmeans")

# Exibir os primeiros produtos de cada cluster
print(df_clusters.head(20))  # Altere o número para ver mais produtos


# Calcula a matriz de distâncias euclidianas
dist_matrix = pdist(df_scaled, metric="euclidean")
dist_matrix = squareform(dist_matrix)  # Converte para matriz quadrada

# Cria um DataFrame para visualização
df_dist = pd.DataFrame(dist_matrix, index=df_pivot.index, columns=df_pivot.index)

df_dist.to_csv("distancias.csv", sep=",", decimal=",")
# Exibir as 10 primeiras distâncias
print(df_dist.head(10))  # Mostra a matriz de distâncias entre os produtos

# Calculando a distância euclidiana entre os produtos
dist_matrix = squareform(pdist(df_scaled, metric="euclidean"))

# Convertendo para um DataFrame para manter os nomes dos produtos
df_dist = pd.DataFrame(dist_matrix, index=df_pivot.index, columns=df_pivot.index)

df_dist.to_csv("distancias_2.csv", sep=",", decimal=",")
# Exibindo a matriz de distâncias
print(df_dist)


plt.figure(figsize=(10, 8))
sns.heatmap(df_dist, cmap="coolwarm", annot=True, fmt=".2f")
plt.title("Matriz de Distâncias Euclidianas entre Produtos")
plt.show()