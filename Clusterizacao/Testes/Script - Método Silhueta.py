import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

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
    plt.savefig("./Resultados/Metodo Silhueta.png")
    plt.show()
else:
    print("Amostras insuficientes para calcular a Silhueta.")