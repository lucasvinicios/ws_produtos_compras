import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Dados fornecidos (preços dos produtos nos supermercados)
data = {
    'Supermercado': ['BARBOSA', 'CONFIANÇA', 'MERCADO LIVRE', 'COOP SUPERMERCADO', 'TENDA ATACADO'],
    'Arroz 5kg': [23.99, 18.5, 8, 26.99, 20.9],
    'Feijão 1kg': [5.99, 4.95, 6.6, 4.99, 2],
    'Macarrão 500g': [2.79, 2.98, 3.29, 3.69, 2.59],
    'Óleo 900ml': [7.49, 7.59, 7.45, 7.49, 7.25],
    'Açúcar 5kg': [24.95, 17.59, 19.49, 19.99, 17.99]
}

# Criar DataFrame
dados = pd.DataFrame(data)

dados = pd.read_csv('../precos_supermercados_3.csv')

# Definir os dados para o K-means (ignorando a coluna 'Supermercado')
precos = dados.iloc[:, 1:]

#%% Cluster Não Hierárquico K-means

# Considerando 2 clusters: um para os supermercados com menores preços e outro para os demais
kmeans = KMeans(n_clusters=2, init='random', random_state=100).fit(precos)

# Gerando a variável para identificarmos os clusters gerados
kmeans_clusters = kmeans.labels_
dados['cluster_kmeans'] = kmeans_clusters
dados['cluster_kmeans'] = dados['cluster_kmeans'].astype('category')

#%% Identificando as coordenadas centroides dos clusters finais
cent_finais = pd.DataFrame(kmeans.cluster_centers_)
cent_finais.columns = precos.columns
cent_finais.index.name = 'cluster'
print("Centróides dos Clusters:")
print(cent_finais)

#%% Identificando o cluster com os menores preços
# O cluster com os menores preços será aquele com o menor valor médio nos centróides
cluster_menores_precos = cent_finais.mean(axis=1).idxmin()
print(f"\nCluster com os menores preços: {cluster_menores_precos}")

# Filtrando os supermercados do cluster com menores preços
supermercados_menores_precos = dados[dados['cluster_kmeans'] == cluster_menores_precos]['Supermercado']
print("\nSupermercados com os menores preços:")
print(supermercados_menores_precos)

#%% Plotando as observações e seus centroides dos clusters

# Escolhendo duas variáveis para o gráfico (por exemplo, 'Arroz 5kg' e 'Feijão 1kg')
plt.figure(figsize=(8, 8))
sns.scatterplot(data=dados, x='Arroz 5kg', y='Feijão 1kg', hue='cluster_kmeans', palette='viridis', s=100)
sns.scatterplot(data=cent_finais, x='Arroz 5kg', y='Feijão 1kg', c='red', label='Centróides', marker="X", s=200)
plt.title('Clusters e Centroides (K-means)', fontsize=16)
plt.xlabel('Arroz 5kg (Preço)', fontsize=16)
plt.ylabel('Feijão 1kg (Preço)', fontsize=16)
plt.legend()
plt.show()