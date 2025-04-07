# import matplotlib.pyplot as plt
# import numpy as np

# # Dados dos supermercados e seus produtos mais baratos
# supermercados = {
#     "CONFIANÇA": ["Detergente Líquido 500ml"],
#     "MERCADO LIVRE": ["Óleo 900ml", "Café 500g"],
#     "TENDA ATACADO": [
#         "Arroz 5kg", "Feijão 1kg", "Macarrão 500g", "Açúcar 5kg",
#         "Leite Integral 1L", "Pão de Forma 500g", "Sabão em Pó 1kg"
#     ]
# }

# # Configurações do gráfico
# plt.figure(figsize=(10, 8))

# # Função para plotar os clusters
# def plot_cluster(supermercado, produtos, angle_offset):
#     # Posição do supermercado (centro)
#     x_center, y_center = np.cos(angle_offset), np.sin(angle_offset)
#     plt.scatter(x_center, y_center, s=200, label=supermercado, alpha=0.6)

#     # Posição dos produtos ao redor
#     num_produtos = len(produtos)
#     angles = np.linspace(0, 2 * np.pi, num_produtos, endpoint=False)
#     radius = 0.2  # Distância dos produtos ao centro

#     for i, produto in enumerate(produtos):
#         x = x_center + radius * np.cos(angles[i])
#         y = y_center + radius * np.sin(angles[i])
#         plt.scatter(x, y, label=produto)
#         plt.text(x, y, produto, fontsize=8, ha='center', va='bottom')

# # Plotar cada supermercado e seus produtos
# angles = np.linspace(0, 2 * np.pi, len(supermercados), endpoint=False)
# for i, (supermercado, produtos) in enumerate(supermercados.items()):
#     plot_cluster(supermercado, produtos, angles[i])

# # Ajustes do gráfico
# plt.xticks([])
# plt.yticks([])
# plt.title("Produtos mais baratos por supermercado", fontsize=14)
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
# plt.grid(True, alpha=0.2)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# # Dados dos supermercados e seus produtos mais baratos
# supermercados = {
#     "CONFIANÇA": ["Detergente Líquido 500ml"],
#     "MERCADO LIVRE": ["Óleo 900ml", "Café 500g"],
#     "TENDA ATACADO": [
#         "Arroz 5kg", "Feijão 1kg", "Macarrão 500g", "Açúcar 5kg",
#         "Leite Integral 1L", "Pão de Forma 500g", "Sabão em Pó 1kg"
#     ]
# }

# # Configurações do gráfico
# plt.figure(figsize=(10, 8))

# # Função para plotar os clusters
# def plot_cluster(supermercado, produtos, angle_offset):
#     # Posição do supermercado (centro)
#     x_center, y_center = np.cos(angle_offset), np.sin(angle_offset)
#     plt.scatter(x_center, y_center, s=200, label=supermercado, alpha=0.6)

#     # Posição dos produtos ao redor
#     num_produtos = len(produtos)
#     angles = np.linspace(0, 2 * np.pi, num_produtos, endpoint=False)
#     radius = 0.2  # Distância dos produtos ao centro

#     for i, produto in enumerate(produtos):
#         x = x_center + radius * np.cos(angles[i])
#         y = y_center + radius * np.sin(angles[i])
#         plt.scatter(x, y, label=produto)
#         plt.text(x, y, produto, fontsize=8, ha='center', va='bottom')
        
#         # Linha conectando o produto ao supermercado
#         plt.plot([x_center, x], [y_center, y], 'k--', alpha=0.3)  # 'k--' = linha tracejada preta

# # Plotar cada supermercado e seus produtos
# angles = np.linspace(0, 2 * np.pi, len(supermercados), endpoint=False)
# for i, (supermercado, produtos) in enumerate(supermercados.items()):
#     plot_cluster(supermercado, produtos, angles[i])

# # Ajustes do gráfico
# plt.xticks([])
# plt.yticks([])
# plt.title("Produtos mais baratos por supermercado", fontsize=14)
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
# plt.grid(True, alpha=0.2)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# # Dados dos supermercados e seus produtos mais baratos
# supermercados = {
#     "CONFIANÇA": ["Detergente Líquido 500ml"],
#     "MERCADO LIVRE": ["Óleo 900ml", "Café 500g"],
#     "TENDA ATACADO": [
#         "Arroz 5kg", "Feijão 1kg", "Macarrão 500g", "Açúcar 5kg",
#         "Leite Integral 1L", "Pão de Forma 500g", "Sabão em Pó 1kg"
#     ]
# }

# # Configurações do gráfico
# plt.figure(figsize=(10, 8))

# # Função para plotar os clusters
# def plot_cluster(supermercado, produtos, angle_offset):
#     # Posição do supermercado (centro)
#     x_center, y_center = np.cos(angle_offset), np.sin(angle_offset)
#     plt.scatter(x_center, y_center, s=200, label=supermercado, alpha=0.6)

#     # Posição dos produtos ao redor
#     num_produtos = len(produtos)
#     angles = np.linspace(0, 2 * np.pi, num_produtos, endpoint=False)
#     radius = 0.4  # Distância dos produtos ao centro

#     for i, produto in enumerate(produtos):
#         x = x_center + radius * np.cos(angles[i])
#         y = y_center + radius * np.sin(angles[i])
#         plt.scatter(x, y, alpha=0.8)  # Plotar os pontos dos produtos
#         plt.text(x, y, produto, fontsize=8, ha='center', va='bottom')  # Rótulo do produto
        
#         # Linha conectando o produto ao supermercado
#         plt.plot([x_center, x], [y_center, y], 'k--', alpha=0.3)  # 'k--' = linha tracejada preta

# # Plotar cada supermercado e seus produtos
# angles = np.linspace(0, 2 * np.pi, len(supermercados), endpoint=False)
# for i, (supermercado, produtos) in enumerate(supermercados.items()):
#     plot_cluster(supermercado, produtos, angles[i])

# # Ajustes do gráfico
# plt.xticks([])
# plt.yticks([])
# plt.title("Produtos mais baratos por supermercado", fontsize=14)
# plt.legend(loc='upper right')  # Legenda apenas para os supermercados
# plt.grid(True, alpha=0.2)
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Ler o arquivo CSV
file_path = "../precos_supermercados_4.csv"  # Substitua pelo caminho correto do arquivo
data = pd.read_csv(file_path)

# Identificar os produtos mais baratos em cada supermercado
supermercados = {}
for supermercado in data.columns[1:]:  # Ignorar a coluna "Item"
    produtos_mais_baratos = []
    for index, row in data.iterrows():
        produto = row["Item"]
        preco = row[supermercado]
        # Verificar se o preço é o menor entre todos os supermercados
        if preco == data.loc[index, data.columns[1:]].min():
            produtos_mais_baratos.append(produto)
    supermercados[supermercado] = produtos_mais_baratos

# Exibir o dicionário gerado
print("Supermercados e seus produtos mais baratos:")
print(supermercados)

# Configurações do gráfico
plt.figure(figsize=(10, 8))

# Função para plotar os clusters
def plot_cluster(supermercado, produtos, angle_offset):
    # Posição do supermercado (centro)
    x_center, y_center = np.cos(angle_offset), np.sin(angle_offset)
    plt.scatter(x_center, y_center, s=200, label=supermercado, alpha=0.6)

    # Posição dos produtos ao redor
    num_produtos = len(produtos)
    angles = np.linspace(0, 2 * np.pi, num_produtos, endpoint=False)
    radius = 0.4  # Distância dos produtos ao centro

    for i, produto in enumerate(produtos):
        x = x_center + radius * np.cos(angles[i])
        y = y_center + radius * np.sin(angles[i])
        plt.scatter(x, y, alpha=0.8)  # Plotar os pontos dos produtos
        plt.text(x, y, produto, fontsize=8, ha='center', va='bottom')  # Rótulo do produto
        
        # Linha conectando o produto ao supermercado
        plt.plot([x_center, x], [y_center, y], 'k--', alpha=0.3)  # 'k--' = linha tracejada preta

# Plotar cada supermercado e seus produtos
angles = np.linspace(0, 2 * np.pi, len(supermercados), endpoint=False)
for i, (supermercado, produtos) in enumerate(supermercados.items()):
    plot_cluster(supermercado, produtos, angles[i])

# Ajustes do gráfico
plt.xticks([])
plt.yticks([])
plt.title("Produtos mais baratos por supermercado", fontsize=14)
plt.legend(loc='upper right')  # Legenda apenas para os supermercados
plt.grid(True, alpha=0.2)
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Ler o arquivo CSV
file_path = "../precos_supermercados_4.csv"  # Substitua pelo caminho correto do arquivo
data = pd.read_csv(file_path)

# Identificar os produtos mais baratos em cada supermercado
supermercados = {}
for supermercado in data.columns[1:]:  # Ignorar a coluna "Item"
    produtos_mais_baratos = []
    for index, row in data.iterrows():
        produto = row["Item"]
        preco = row[supermercado]
        # Verificar se o preço é o menor entre todos os supermercados
        if preco == data.loc[index, data.columns[1:]].min():
            produtos_mais_baratos.append(produto)
    supermercados[supermercado] = produtos_mais_baratos

# Exibir o dicionário gerado
print("Supermercados e seus produtos mais baratos:")
print(supermercados)

# Exportar tabelas para cada supermercado
for supermercado, produtos in supermercados.items():
    # Criar um DataFrame com os produtos mais baratos
    df = pd.DataFrame(produtos, columns=["Produto"])
    # Exportar para CSV
    df.to_csv(f"{supermercado}_produtos_mais_baratos.csv", index=False)
    print(f"Tabela exportada para {supermercado}_produtos_mais_baratos.csv")

# Configurações do gráfico
plt.figure(figsize=(10, 8))

# Função para plotar os clusters
def plot_cluster(supermercado, produtos, angle_offset):
    # Posição do supermercado (centro)
    x_center, y_center = np.cos(angle_offset), np.sin(angle_offset)
    plt.scatter(x_center, y_center, s=200, label=supermercado, alpha=0.6)

    # Posição dos produtos ao redor
    num_produtos = len(produtos)
    angles = np.linspace(0, 2 * np.pi, num_produtos, endpoint=False)
    radius = 0.4  # Distância dos produtos ao centro

    for i, produto in enumerate(produtos):
        x = x_center + radius * np.cos(angles[i])
        y = y_center + radius * np.sin(angles[i])
        plt.scatter(x, y, alpha=0.8)  # Plotar os pontos dos produtos
        plt.text(x, y, produto, fontsize=8, ha='center', va='bottom')  # Rótulo do produto
        
        # Linha conectando o produto ao supermercado
        plt.plot([x_center, x], [y_center, y], 'k--', alpha=0.3)  # 'k--' = linha tracejada preta

# Plotar cada supermercado e seus produtos
angles = np.linspace(0, 2 * np.pi, len(supermercados), endpoint=False)
for i, (supermercado, produtos) in enumerate(supermercados.items()):
    plot_cluster(supermercado, produtos, angles[i])

# Ajustes do gráfico
plt.xticks([])
plt.yticks([])
plt.title("Produtos mais baratos por supermercado", fontsize=14)
plt.legend(loc='upper right')  # Legenda apenas para os supermercados
plt.grid(True, alpha=0.2)
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA  # Para reduzir a dimensionalidade

# Ler o arquivo CSV
file_path = "../precos_supermercados_4.csv"  # Substitua pelo caminho correto do arquivo
data = pd.read_csv(file_path)

# Preparar os dados (preços dos produtos)
X = data.iloc[:, 1:].values  # Ignorar a coluna "Item" (usamos apenas os preços)

# Reduzir a dimensionalidade para visualização (usando PCA)
pca = PCA(n_components=2)  # Reduzir para 2 dimensões para facilitar a visualização
X_reduced = pca.fit_transform(X)  # Transforma os dados em 2 componentes principais

# Aplicar o K-Means para agrupar os produtos
n_clusters = 3  # Defina o número de clusters (ajuste conforme necessário)
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(X_reduced)  # Aplica o K-Means aos dados reduzidos

# Adicionar os rótulos dos clusters ao DataFrame
data['Cluster'] = kmeans.labels_

# Exibir os clusters
print("Clusters encontrados pelo K-Means:")
print(data[['Item', 'Cluster']])

# Função para calcular a distância entre dois pontos
def calcular_distancia(ponto1, ponto2):
    return np.sqrt(np.sum((ponto1 - ponto2) ** 2))

# Função para plotar os clusters
def plot_clusters(X, labels, centros):
    plt.figure(figsize=(12, 8))
    
    # Plotar os produtos
    for i in range(n_clusters):
        # Pontos do cluster
        pontos_cluster = X[labels == i]
        plt.scatter(pontos_cluster[:, 0], pontos_cluster[:, 1], label=f'Cluster {i}', alpha=0.6)
        
        # Adicionar rótulos aos pontos próximos ao centroide
        for j, ponto in enumerate(pontos_cluster):
            distancia_centroide = calcular_distancia(ponto, centros[i])
            if distancia_centroide < 10:  # Ajuste o limite de distância conforme necessário
                produto = data[labels == i]['Item'].iloc[j]
                plt.text(ponto[0], ponto[1], produto, fontsize=8, ha='center', va='bottom')
    
    # Plotar os centros dos clusters
    plt.scatter(centros[:, 0], centros[:, 1], s=200, c='red', marker='X', label='Centros dos Clusters')
    
    # Ajustes do gráfico
    plt.title("Clusterização de Produtos por Preço (K-Means)", fontsize=14)
    plt.xlabel("Componente Principal 1 (PCA)")
    plt.ylabel("Componente Principal 2 (PCA)")
    plt.legend()
    plt.grid(True, alpha=0.2)
    plt.show()

# Plotar os clusters
plot_clusters(X_reduced, kmeans.labels_, kmeans.cluster_centers_)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Ler o arquivo CSV
file_path = "../precos_supermercados_4.csv"  # Substitua pelo caminho correto do arquivo
data = pd.read_csv(file_path)

# Preparar os dados (preços dos produtos)
X = data.iloc[:, 1:].values  # Ignorar a coluna "Item" (usamos apenas os preços)

# Aplicar o K-Means para agrupar os produtos
n_clusters = 3  # Defina o número de clusters (ajuste conforme necessário)
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(X)  # Aplica o K-Means aos dados

# Adicionar os rótulos dos clusters ao DataFrame
data['Cluster'] = kmeans.labels_

# Exibir os clusters
print("Clusters encontrados pelo K-Means:")
print(data[['Item', 'Cluster']])

# Função para calcular a distância entre dois pontos
def calcular_distancia(ponto1, ponto2):
    return np.sqrt(np.sum((ponto1 - ponto2) ** 2))

# Função para plotar os clusters
def plot_clusters(X, labels, centros):
    plt.figure(figsize=(12, 8))
    
    # Plotar os produtos
    for i in range(n_clusters):
        # Pontos do cluster
        pontos_cluster = X[labels == i]
        plt.scatter(pontos_cluster[:, 0], pontos_cluster[:, 1], label=f'Cluster {i}', alpha=0.6)
        
        # Adicionar rótulos aos pontos
        for j, ponto in enumerate(pontos_cluster):
            produto = data[labels == i]['Item'].iloc[j]
            plt.text(ponto[0], ponto[1], produto, fontsize=8, ha='center', va='bottom')
    
    # Plotar os centros dos clusters
    plt.scatter(centros[:, 0], centros[:, 1], s=200, c='red', marker='X', label='Centros dos Clusters')
    
    # Ajustes do gráfico
    plt.title("Clusterização de Produtos por Preço (K-Means)", fontsize=14)
    plt.xlabel("Preço no Supermercado 1")
    plt.ylabel("Preço no Supermercado 2")
    plt.legend()
    plt.grid(True, alpha=0.2)
    plt.show()

# Reduzir a dimensionalidade para visualização (usando apenas 2 supermercados)
plot_clusters(X[:, :2], kmeans.labels_, kmeans.cluster_centers_[:, :2])

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

# Ler o arquivo CSV
file_path = "../precos_supermercados_4.csv"
data = pd.read_csv(file_path)

# Preparar os dados (preços dos produtos)
X = data.iloc[:, 1:].values  # Ignorar a coluna "Item"

# Aplicar o DBSCAN
dbscan = DBSCAN(eps=2.0, min_samples=2)  # Ajuste eps e min_samples conforme necessário
dbscan.fit(X.T)  # Transpor para agrupar supermercados em vez de produtos

# Adicionar os rótulos dos clusters ao DataFrame
supermercados = data.columns[1:]
clusters_supermercados = pd.DataFrame({'Supermercado': supermercados, 'Cluster': dbscan.labels_})

# Exibir os clusters
print("Clusters encontrados pelo DBSCAN:")
print(clusters_supermercados)

# Função para plotar os clusters
def plot_clusters(X, labels):
    plt.figure(figsize=(10, 8))
    
    # Plotar os supermercados
    unique_labels = set(labels)
    for label in unique_labels:
        if label == -1:
            # Ruído (pontos não atribuídos a nenhum cluster)
            plt.scatter(X[labels == label, 0], X[labels == label, 1], c='gray', label='Ruído', alpha=0.6)
        else:
            plt.scatter(X[labels == label, 0], X[labels == label, 1], label=f'Cluster {label}', alpha=0.6)
    
    # Ajustes do gráfico
    plt.title("Clusterização de Supermercados por Preço (DBSCAN)", fontsize=14)
    plt.xlabel("Preço do Produto 1")
    plt.ylabel("Preço do Produto 2")
    plt.legend()
    plt.grid(True, alpha=0.2)
    plt.show()

# Reduzir a dimensionalidade para visualização (usando apenas 2 produtos)
plot_clusters(X.T[:, :2], dbscan.labels_)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Ler o arquivo CSV
file_path = "../precos_supermercados_4.csv"
data = pd.read_csv(file_path)

# Preparar os dados (preços dos produtos)
X = data.iloc[:, 1:].values  # Ignorar a coluna "Item"

# Calcular a matriz de ligação
Z = linkage(X, method='ward')

# Plotar o dendrograma
plt.figure(figsize=(10, 8))
dendrogram(Z, labels=data['Item'].values, leaf_rotation=90)
plt.title("Dendrograma de Produtos por Variação de Preço", fontsize=14)
plt.xlabel("Produtos")
plt.ylabel("Distância")
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Ler o arquivo CSV
file_path = "../precos_supermercados_4.csv"
data = pd.read_csv(file_path)

# Preparar os dados (preços dos produtos)
X = data.iloc[:, 1:].values  # Ignorar a coluna "Item"

# Reduzir a dimensionalidade com PCA
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X.T)  # Transpor para agrupar supermercados

# Aplicar o K-Means
n_clusters = 3  # Defina o número de clusters
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(X_reduced)

# Adicionar os rótulos dos clusters ao DataFrame
supermercados = data.columns[1:]
clusters_supermercados = pd.DataFrame({'Supermercado': supermercados, 'Cluster': kmeans.labels_})

# Exibir os clusters
print("Clusters encontrados pelo K-Means:")
print(clusters_supermercados)

# Função para plotar os clusters
def plot_clusters(X, labels):
    plt.figure(figsize=(10, 8))
    
    # Plotar os supermercados
    for i in range(n_clusters):
        plt.scatter(X[labels == i, 0], X[labels == i, 1], label=f'Cluster {i}', alpha=0.6)
    
    # Plotar os centros dos clusters
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', marker='X', label='Centros')
    
    # Ajustes do gráfico
    plt.title("Segmentação de Supermercados por Perfil de Preços (PCA + K-Means)", fontsize=14)
    plt.xlabel("Componente Principal 1")
    plt.ylabel("Componente Principal 2")
    plt.legend()
    plt.grid(True, alpha=0.2)
    plt.show()

# Plotar os clusters
plot_clusters(X_reduced, kmeans.labels_)

