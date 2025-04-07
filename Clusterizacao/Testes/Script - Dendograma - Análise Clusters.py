import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.cluster.hierarchy as sch
from scipy.stats import zscore
from scipy.spatial.distance import pdist
from sklearn.cluster import AgglomerativeClustering
import plotly.express as px 

# Carregar os dados
dados = pd.read_csv('../precos_supermercados.csv')

# Visualizar as primeiras linhas
print(dados.head())

# Remover colunas não numéricas (como nomes de produtos, supermercados, etc.)
dados_numericos = dados.select_dtypes(include=[np.number])

# Padronização dos dados (Z-score)
dados_pad = dados_numericos.apply(zscore, ddof=1)

print(dados_pad.head())

# Cluster hierárquico aglomerativo (método Complete Linkage)
plt.figure(figsize=(16,8))
dend = sch.linkage(dados_pad, method='single', metric='euclidean')
sch.dendrogram(dend, color_threshold=8)
plt.title('Dendrograma - Single Linkage', fontsize=16)
plt.xlabel('Produtos', fontsize=16)
plt.ylabel('Distância Euclidiana', fontsize=16)
plt.axhline(y=8, color='red', linestyle='--')
plt.savefig('./Resultados/Dendrograma.png')
plt.show()

# Criar clusters
n_clusters = 6  # Ajuste conforme necessário
cluster_model = AgglomerativeClustering(n_clusters=n_clusters, metric='euclidean', linkage='single')
dados['cluster'] = cluster_model.fit_predict(dados_pad)
dados['cluster'] = dados['cluster'].astype('category')

# Estatísticas dos clusters
analise_clusters = dados.groupby('cluster').mean(numeric_only=True)
analise_clusters.to_csv('./Resultados/analise_clusters.csv')
print(analise_clusters) 


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist, squareform
from scipy.stats import zscore

# Carregar os dados do arquivo CSV
dados = pd.read_csv("../precos_supermercados.csv")

# Exibir os dados
print("Dados brutos:")
print(dados)

# Extrair os preços dos itens (ignorando a coluna "Item")
precos = dados.iloc[:, 1:].values

# Aplicar Z-score para padronizar os dados
precos_padronizados = zscore(precos, axis=1)

# Calcular a matriz de distâncias (usando distância euclidiana)
distancias = pdist(precos_padronizados, metric='euclidean')
matriz_distancias = squareform(distancias)

# Exibir a matriz de distâncias
print("\nMatriz de distâncias:")
print(matriz_distancias)

# Aplicar o clustering hierárquico com Single Linkage
Z = linkage(distancias, method='single')

# Plotar o dendrograma
plt.figure(figsize=(10, 5))
plt.title("Dendrograma - Single Linkage (Baseado nos Preços Padronizados)")
plt.xlabel("Itens")
plt.ylabel("Distância")
dendrogram(Z, labels=dados["Item"].values, leaf_rotation=90, leaf_font_size=10)
plt.show()