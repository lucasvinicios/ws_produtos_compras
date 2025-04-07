import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px

# Carregar os dados do arquivo CSV
data = pd.read_csv('../precos_supermercados_4.csv')

# Definir os itens como índice
data.set_index('Item', inplace=True)

# Converter os dados para um array numpy (produtos são linhas, supermercados são colunas)
X = data.values

# Nomes dos produtos
produtos = data.index

# Nomes dos supermercados
supermercados = data.columns

# Aplicar K-means
kmeans = KMeans(n_clusters=len(supermercados), random_state=42)  # Número de clusters = número de supermercados
kmeans.fit(X)

# Reduzir a dimensionalidade para 3D usando PCA
pca = PCA(n_components=3)
X_reduced = pca.fit_transform(X)

# Criar um DataFrame com os dados reduzidos e os clusters
reduced_df = pd.DataFrame(X_reduced, columns=['Componente 1', 'Componente 2', 'Componente 3'])
reduced_df['Cluster'] = kmeans.labels_
reduced_df['Produto'] = produtos

# Adicionar os centroides ao DataFrame
centroids_reduced = pca.transform(kmeans.cluster_centers_)
centroids_df = pd.DataFrame(centroids_reduced, columns=['Componente 1', 'Componente 2', 'Componente 3'])
centroids_df['Supermercado'] = supermercados

# Plotar os clusters em um gráfico de dispersão 3D (Matplotlib)
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Definir cores para cada cluster
colors = plt.cm.get_cmap('viridis', len(supermercados))

# Plotar os produtos (pontos)
for i, produto in enumerate(produtos):
    ax.scatter(
        reduced_df.loc[i, 'Componente 1'], 
        reduced_df.loc[i, 'Componente 2'], 
        reduced_df.loc[i, 'Componente 3'], 
        c=colors(kmeans.labels_[i]), 
        s=50
    )

# Plotar os supermercados (centroides)
for i, supermercado in enumerate(supermercados):
    ax.scatter(
        centroids_df.loc[i, 'Componente 1'], 
        centroids_df.loc[i, 'Componente 2'], 
        centroids_df.loc[i, 'Componente 3'], 
        c=colors(i), 
        marker='X', 
        s=200, 
        label=supermercado
    )

# Configurações do gráfico
ax.set_title('Agrupamento de Produtos por Supermercado (K-means com PCA 3D)')
ax.set_xlabel('Componente 1')
ax.set_ylabel('Componente 2')
ax.set_zlabel('Componente 3')
ax.legend(title='Supermercados', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Criar um gráfico 3D interativo com Plotly
fig = px.scatter_3d(
    reduced_df, 
    x='Componente 1', 
    y='Componente 2', 
    z='Componente 3', 
    color='Cluster', 
    hover_name='Produto', 
    title='Agrupamento de Produtos por Supermercado (K-means com PCA 3D)'
)

# Adicionar os centroides ao gráfico Plotly
for i, supermercado in enumerate(supermercados):
    fig.add_scatter3d(
        x=[centroids_df.loc[i, 'Componente 1']],
        y=[centroids_df.loc[i, 'Componente 2']],
        z=[centroids_df.loc[i, 'Componente 3']],
        mode='markers',
        marker=dict(size=10, symbol='x', color=colors(i)),
        name=supermercado
    )

# Exibir o gráfico
fig.show()

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
data = pd.read_csv('../precos_supermercados_4.csv')

# Definir os itens como índice
data.set_index('Item', inplace=True)

# Transpor os dados para que os supermercados sejam as linhas e os itens as colunas
data_transposed = data.T

# Aplicar K-Means para clustering
kmeans = KMeans(n_clusters=3, random_state=42)  # Número de clusters
clusters = kmeans.fit_predict(data_transposed)

# Adicionar os clusters ao DataFrame transposto
data_transposed['Cluster'] = clusters

# Reduzir a dimensionalidade dos dados para 2D usando PCA
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(data_transposed.drop(columns=['Cluster']))

# Criar um DataFrame com os dados reduzidos e os clusters
reduced_df = pd.DataFrame(reduced_data, columns=['Componente 1', 'Componente 2'])
reduced_df['Cluster'] = clusters
reduced_df['Supermercado'] = data_transposed.index

# Adicionar os centroides ao DataFrame
centroids_reduced = pca.transform(kmeans.cluster_centers_)
centroids_df = pd.DataFrame(centroids_reduced, columns=['Componente 1', 'Componente 2'])
centroids_df['Cluster'] = range(kmeans.n_clusters)

# Plotar os clusters em um gráfico de dispersão 2D
plt.figure(figsize=(10, 8))

# Cores para os clusters
cores = plt.cm.get_cmap('viridis', kmeans.n_clusters)

# Plotar os supermercados (pontos)
for i, row in reduced_df.iterrows():
    plt.scatter(
        row['Componente 1'], 
        row['Componente 2'], 
        color=cores(row['Cluster']), 
        s=50
    )
    plt.text(row['Componente 1'], row['Componente 2'], row['Supermercado'], fontsize=9, ha='right')

    # Conectar o ponto ao centroide do cluster ao qual pertence
    centroid = centroids_df.loc[row['Cluster']]
    plt.plot(
        [row['Componente 1'], centroid['Componente 1']],
        [row['Componente 2'], centroid['Componente 2']],
        'k--',  # Linha tracejada preta
        linewidth=0.5
    )

# Plotar os centroides
for i, row in centroids_df.iterrows():
    plt.scatter(
        row['Componente 1'], 
        row['Componente 2'], 
        color=cores(i), 
        marker='X', 
        s=200, 
        label=f'Centroide {i}'
    )

# Adicionar legenda
plt.legend(title='Centroides', bbox_to_anchor=(1.05, 1), loc='upper left')

# Configurações do gráfico
plt.title('Clusterização de Supermercados com Base nos Preços dos Produtos (PCA 2D)')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.tight_layout()  # Ajustar layout para evitar cortes
plt.show()


