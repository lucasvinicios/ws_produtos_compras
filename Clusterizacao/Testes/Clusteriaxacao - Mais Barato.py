# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# from scipy.cluster.hierarchy import linkage, dendrogram, fcluster

# # Carregar os dados
# file_path = "../precos_supermercados_3.csv"
# df = pd.read_csv(file_path, sep=',', decimal='.')

# # Transformação dos dados
# df_melted = df.melt(id_vars=["Item"], var_name="Supermercado", value_name="Preço")
# df_melted["Preço"] = pd.to_numeric(df_melted["Preço"], errors="coerce")
# df_melted.dropna(inplace=True)

# # Criar tabela pivot para clusterização
# df_pivot = df_melted.pivot(index="Supermercado", columns="Item", values="Preço")

# # Preencher valores ausentes com a média do supermercado
# for col in df_pivot.columns:
#     df_pivot[col].fillna(df_pivot[col].mean(), inplace=True)

# # Clusterização hierárquica (método single linkage)
# linkage_matrix = linkage(df_pivot, method='single')
# plt.figure(figsize=(10, 5))
# dendrogram(linkage_matrix, labels=df_pivot.index, leaf_rotation=90)
# plt.title("Dendrograma dos Supermercados")
# plt.xlabel("Supermercado")
# plt.ylabel("Distância")
# plt.show()

# # Determinar o cluster de cada supermercado
# clusters = fcluster(linkage_matrix, t=2, criterion='maxclust')
# df_clusters = pd.DataFrame({'Supermercado': df_pivot.index, 'Cluster': clusters})

# # Identificar o supermercado mais barato
# supermercado_mais_barato = df_pivot.mean(axis=1).idxmin()
# print(f"O supermercado mais barato no geral é: {supermercado_mais_barato}")


# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
# from scipy.spatial.distance import pdist

# # Carregar os dados
# df = pd.read_csv("../precos_supermercados_3.csv", sep=',', decimal='.')
# df.set_index("Item", inplace=True)

# # Normalizar os preços para evitar distorções (Z-score)
# df_normalized = (df - df.mean()) / df.std()

# # Calcular a matriz de distâncias e aplicar o método hierárquico
# linkage_matrix = linkage(pdist(df_normalized.T, metric='euclidean'), method='ward')

# # Plotar o dendrograma
# plt.figure(figsize=(12, 6))
# dendrogram(linkage_matrix, labels=df.columns, leaf_rotation=90, leaf_font_size=10)
# plt.title("Dendrograma dos Supermercados")
# plt.xlabel("Supermercados")
# plt.ylabel("Distância")
# plt.show()

# # Definir o número de clusters
# num_clusters = 3  # Ajuste conforme necessário
# clusters = fcluster(linkage_matrix, num_clusters, criterion='maxclust')

# # Criar um DataFrame para visualizar os grupos
# cluster_df = pd.DataFrame({"Supermercado": df.columns, "Cluster": clusters})
# print(cluster_df.sort_values("Cluster"))

# # Identificar o supermercado mais barato por produto
# supermercado_mais_barato = df.idxmin(axis=1)
# print("Supermercado mais barato por produto:")
# print(supermercado_mais_barato)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from mpl_toolkits.mplot3d import Axes3D

# Carregar os dados
dados = {
    "Item": ["Arroz 5kg", "Feijão 1kg", "Macarrão 500g", "Óleo 900ml", "Açúcar 5kg", "Leite Integral 1L"],
    "TAUSTE": [21.9, 4.89, 2.97, 7.18, 15.95, 4.95],
    "BARBOSA": [23.99, 4.99, 2.79, 7.49, 24.95, 4.79],
    "CONFIANÇA": [21.9, 4.75, 2.98, 7.18, 17.59, 4.95],
    "MERCADO LIVRE": [24.19, 5.99, 4.19, 6.99, 18.9, 6.6],
    "COOP SUPERMERCADO": [24.99, 4.99, 3.59, 7.49, 24.99, 4.99],
    "TENDA ATACADO": [20.9, 2.0, 2.59, 7.25, 16.49, 5.25]
}

df = pd.DataFrame(dados)

# Encontrar o supermercado mais barato para cada item
df["Supermercado Mais Barato"] = df.iloc[:, 1:].idxmin(axis=1)

# Codificar os supermercados para plotagem em 3D
encoder = LabelEncoder()
df["Cluster"] = encoder.fit_transform(df["Supermercado Mais Barato"])

# Gerar os dados para o gráfico 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Criar pontos 3D
x = np.arange(len(df))  # Índices dos produtos
y = df["Cluster"]  # Supermercado mais barato codificado
z = np.zeros(len(df))  # Z para colocar no gráfico

ax.scatter(x, y, z, c=y, cmap='rainbow', s=100)

# Adicionar rótulos
ax.set_xticks(x)
ax.set_xticklabels(df["Item"], rotation=45, ha='right')
ax.set_yticks(range(len(encoder.classes_)))
ax.set_yticklabels(encoder.classes_)
ax.set_xlabel("Produtos")
ax.set_ylabel("Supermercado Mais Barato")
ax.set_zlabel("Cluster")
ax.set_title("Clusterização dos Supermercados Mais Baratos")

plt.show()

# Mostrar tabela final
df_resultado = df[["Item", "Supermercado Mais Barato"]]
print(df_resultado)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
file_path = "../precos_supermercados_3.csv"  # Ajuste o caminho conforme necessário
df = pd.read_csv(file_path, sep=',')

# Identificar o supermercado com menor preço para cada item
supermercado_barato = df.set_index("Item").idxmin(axis=1)

# Criar um DataFrame formatado para visualização
df_cluster = pd.DataFrame({"Produto": supermercado_barato.index, "Supermercado": supermercado_barato.values})

# Criar um gráfico de barras agrupado por supermercado
plt.figure(figsize=(10, 6))
sns.countplot(data=df_cluster, y="Supermercado", palette="viridis", order=df_cluster["Supermercado"].value_counts().index)
plt.xlabel("Quantidade de Produtos Mais Baratos")
plt.ylabel("Supermercado")
plt.title("Clusterização: Produtos com Menores Preços por Supermercado")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()
