import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.cluster.hierarchy as sch
import scipy.stats as stats
from scipy.stats import zscore
from scipy.spatial.distance import pdist
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans
import pingouin as pg
import plotly.express as px 
import plotly.io as pio
pio.renderers.default='browser'

dados_produtos = pd.read_csv('../precos_supermercados_4.csv').round(2)
dados_produtos_transposta = dados_produtos.set_index('Item').T
dados_produtos_transposta.describe()

fig = px.box(dados_produtos_transposta)
fig.show()

dados_produtos_transposta = dados_produtos_transposta.apply(zscore)

fig = px.box(dados_produtos_transposta)
fig.show()

labels = list(dados_produtos.columns)[1:]

'''
Clusterizacao/Script - Dendograma - Análise Clusters.py - Single Linkage
'''
dist_euclidean = pdist(dados_produtos_transposta, metric='euclidean')
plt.figure(figsize=(16,8))
dend = sch.linkage(dist_euclidean, method='single', metric='euclidean')
dendrogram_s = sch.dendrogram(dend, color_threshold=8, labels=labels)
plt.title('Dendrograma - Single Linkage', fontsize=16)
plt.xlabel('Supermercados', fontsize=16)
plt.ylabel('Distâncias', fontsize=16)
plt.show()

cluster_sing = AgglomerativeClustering(n_clusters = 3, metric = 'euclidean', linkage = 'single')
indica_cluster_sing = cluster_sing.fit_predict(dados_produtos_transposta)
dados_produtos_transposta['cluster_single'] = indica_cluster_sing
dados_produtos_transposta['cluster_single'] = dados_produtos_transposta['cluster_single'].astype('category')

# Coeficientes do esquema hierárquico de aglomeração (single)
coef_single = [y[1] for y in dendrogram_s['dcoord']]
print(coef_single)


'''
Clusterizacao/Script - Dendograma - Análise Clusters.py - Complete Linkage
'''
dist_euclidean = pdist(dados_produtos_transposta, metric='euclidean')
plt.figure(figsize=(16,8))
dend = sch.linkage(dist_euclidean, method='complete', metric='euclidean')
sch.dendrogram(dend, color_threshold=8, labels=labels)
plt.title('Dendrograma - Complete Linkage', fontsize=16)
plt.xlabel('Supermercados', fontsize=16)
plt.ylabel('Distâncias', fontsize=16)
plt.show()

cluster_complete = AgglomerativeClustering(n_clusters = 3, metric = 'euclidean', linkage = 'complete')
indica_cluster_complete = cluster_complete.fit_predict(dados_produtos_transposta)
dados_produtos_transposta['cluster_complete'] = indica_cluster_complete
dados_produtos_transposta['cluster_complete'] = dados_produtos_transposta['cluster_complete'].astype('category')

# Coeficientes do esquema hierárquico de aglomeração (complete)
coef_single = [y[1] for y in dendrogram_s['dcoord']]
print(coef_single)


'''
Clusterizacao/Script - Dendograma - Análise Clusters.py - Average Linkage
''' 
dist_euclidean = pdist(dados_produtos_transposta, metric='euclidean')
plt.figure(figsize=(16,8))
dend = sch.linkage(dist_euclidean, method='average', metric='euclidean')
dendrogram_s = sch.dendrogram(dend, color_threshold=8, labels=labels)
plt.title('Dendrograma - Average Linkage', fontsize=16)
plt.xlabel('Supermercados', fontsize=16)
plt.ylabel('Distâncias', fontsize=16)
plt.show()

cluster_average = AgglomerativeClustering(n_clusters = 3, metric = 'euclidean', linkage = 'average')
indica_cluster_average = cluster_average.fit_predict(dados_produtos_transposta)
dados_produtos_transposta['cluster_average'] = indica_cluster_average
dados_produtos_transposta['cluster_average'] = dados_produtos_transposta['cluster_average'].astype('category')

# Coeficientes do esquema hierárquico de aglomeração (average)
coef_single = [y[1] for y in dendrogram_s['dcoord']]
print(coef_single)

'''
Cluster Não Hierárquico K-Means
'''
# Definir os dados para o K-means (ignorando a coluna 'Supermercado')
vest = dados_produtos_transposta.iloc[:, 1:]

#%% Cluster Não Hierárquico K-means

# Considerando que identificamos 3 possíveis clusters
kmeans = KMeans(n_clusters=3, init='random', random_state=100).fit(vest)

# Gerando a variável para identificarmos os clusters gerados
kmeans_clusters = kmeans.labels_
dados_produtos_transposta['cluster_kmeans'] = kmeans_clusters
dados_produtos_transposta['cluster_kmeans'] = dados_produtos_transposta['cluster_kmeans'].astype('category')

#%% Identificando as coordenadas centroides dos clusters finais
cent_finais = pd.DataFrame(kmeans.cluster_centers_)
cent_finais.columns = vest.columns
cent_finais.index.name = 'cluster'
print("Centróides dos Clusters:")
print(cent_finais)

#%% Plotando as observações e seus centroides dos clusters

# Escolhendo duas variáveis para o gráfico (por exemplo, 'Arroz 5kg' e 'Feijão 1kg')
plt.figure(figsize=(8, 8))
sns.scatterplot(data=dados_produtos_transposta, x='Açúcar 5kg', y='Feijão 1kg', hue='cluster_kmeans', palette='viridis', s=100)
sns.scatterplot(data=cent_finais, x='Açúcar 5kg', y='Feijão 1kg', c='red', label='Centróides', marker="X", s=200)
plt.title('Clusters e Centroides (K-means)', fontsize=16)
plt.xlabel('Açúcar 5kg (Z-score)', fontsize=16)
plt.ylabel('Feijão 1kg (Z-score)', fontsize=16)
plt.legend()
plt.show()


#%% Identificação da quantidade de clusters

# Método Elbow para identificação do nº de clusters
## Elaborado com base na "WCSS": distância de cada observação para o centroide de seu cluster
## Quanto mais próximos entre si e do centroide, menores as distâncias internas
## Normalmente, busca-se o "cotovelo", ou seja, o ponto onde a curva "dobra"

elbow = []
K = range(1,5) # ponto de parada pode ser parametrizado manualmente
for k in K:
    kmeanElbow = KMeans(n_clusters=k, init='random', random_state=100).fit(dados_produtos_transposta)
    elbow.append(kmeanElbow.inertia_)
    
plt.figure(figsize=(16,8))
plt.plot(K, elbow, marker='o')
plt.xlabel('Nº Clusters', fontsize=16)
plt.xticks(range(1,5))
plt.ylabel('WCSS', fontsize=16)
plt.title('Método de Elbow', fontsize=16)
plt.show()

#%% Análise de variância de um fator (ANOVA)

# Interpretação do output:

## cluster_kmeans MS: indica a variabilidade entre grupos
## Within MS: indica a variabilidade dentro dos grupos
## F: estatística de teste (cluster_kmeans MS / Within MS)
## p-unc: p-valor da estatística F
## se p-valor < 0.05: pelo menos um cluster apresenta média estatisticamente diferente dos demais

# Açúcar 5k
pg.anova(dv='Açúcar 5kg', 
         between='cluster_kmeans', 
         data=dados_produtos_transposta,
         detailed=True).T

# Feijão 1kg
pg.anova(dv='Feijão 1kg', 
         between='cluster_kmeans', 
         data=dados_produtos_transposta,
         detailed=True).T

# Química
pg.anova(dv='Macarrão 500g', 
         between='cluster_kmeans', 
         data=dados_produtos_transposta,
         detailed=True).T

## A variável mais discriminante contém a maior estatística F (e significativa)
## O valor da estatística F é sensível ao tamanho da amostra

#%% Gráfico 3D dos clusters

fig = px.scatter_3d(dados_produtos_transposta, 
                    x='Açúcar 5kg', 
                    y='Feijão 1kg', 
                    z='Macarrão 500g',
                    color='cluster_kmeans',
                    text=dados_produtos_transposta.index)
fig.show()