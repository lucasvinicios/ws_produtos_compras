import pandas as pd

# Carregar os dados do arquivo CSV
data = pd.read_csv('../precos_supermercados_4.csv')

# Identificar o menor preço e o supermercado correspondente para cada item
menores_precos = data.set_index('Item').min(axis=1)
supermercados_menores_precos = data.set_index('Item').idxmin(axis=1)

# Criar uma tabela com os resultados
resultado = pd.DataFrame({
    'Menor Preço': menores_precos,
    'Supermercado': supermercados_menores_precos
})

# Exibir a tabela resultante
print(resultado)

import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

# Carregar os dados do arquivo CSV
data = pd.read_csv('../precos_supermercados_4.csv')

# Definir os itens como índice
data.set_index('Item', inplace=True)

# Transpor os dados para que os supermercados sejam as linhas e os itens as colunas
data_transposed = data.T

# Aplicar K-Means para clustering
kmeans = KMeans(n_clusters=6, random_state=42)  # Escolha o número de clusters
clusters = kmeans.fit_predict(data_transposed)

# Adicionar os clusters ao DataFrame transposto
data_transposed['Cluster'] = clusters

# Função para encontrar o menor preço em cada cluster
def encontrar_menor_preco_por_cluster(df, cluster_label):
    cluster_data = df[df['Cluster'] == cluster_label]
    menores_precos = cluster_data.min()
    return menores_precos

# Encontrar os menores preços em cada cluster
menores_precos_clusters = []
for cluster in np.unique(clusters):
    menores_precos_clusters.append(encontrar_menor_preco_por_cluster(data_transposed, cluster))

# Combinar os resultados em um DataFrame
resultado_clusters = pd.concat(menores_precos_clusters, axis=1).T
resultado_clusters.index = [f'Cluster {i}' for i in range(len(resultado_clusters))]

# Exibir os menores preços por cluster
print(resultado_clusters)

import pandas as pd
from sklearn.cluster import KMeans

# Carregar os dados do arquivo CSV
data = pd.read_csv('../precos_supermercados_4.csv')

# Definir os itens como índice
data.set_index('Item', inplace=True)

# Transpor os dados para que os supermercados sejam as linhas e os itens as colunas
data_transposed = data.T

# Aplicar K-Means para clustering
kmeans = KMeans(n_clusters=3, random_state=42)  # Escolha o número de clusters
clusters = kmeans.fit_predict(data_transposed)

# Adicionar os clusters ao DataFrame transposto
data_transposed['Cluster'] = clusters

# Função para encontrar o supermercado com o menor preço em cada cluster
def encontrar_supermercado_menor_preco(df, cluster_label):
    cluster_data = df[df['Cluster'] == cluster_label]
    menores_precos = cluster_data.min()
    supermercado_menor_preco = cluster_data.idxmin()
    return supermercado_menor_preco, menores_precos

# Encontrar o supermercado com o menor preço em cada cluster
resultados = []
for cluster in data_transposed['Cluster'].unique():
    supermercado_menor, menores_precos = encontrar_supermercado_menor_preco(data_transposed, cluster)
    resultados.append((supermercado_menor, menores_precos))

# Criar um DataFrame com os resultados
resultado_final = pd.DataFrame()
for supermercado, menores_precos in resultados:
    menores_precos['Supermercado'] = supermercado
    resultado_final = pd.concat([resultado_final, menores_precos.to_frame().T])

# Reorganizar as colunas para que 'Supermercado' seja a primeira coluna
resultado_final = resultado_final.reset_index(drop=True)
resultado_final = resultado_final[['Supermercado'] + [col for col in resultado_final.columns if col != 'Supermercado']]



import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados do arquivo CSV
data = pd.read_csv('../precos_supermercados_4.csv')

# Definir os itens como índice
data.set_index('Item', inplace=True)

# Transpor os dados para que os supermercados sejam as linhas e os itens as colunas
data_transposed = data.T

# Aplicar K-Means para clustering
kmeans = KMeans(n_clusters=3, random_state=42)  # Escolha o número de clusters
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

# Plotar os clusters em um gráfico 2D
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='Componente 1', 
    y='Componente 2', 
    hue='Cluster', 
    data=reduced_df, 
    palette='viridis', 
    s=100, 
    legend='full'
)

# Adicionar rótulos dos supermercados no gráfico
for i, row in reduced_df.iterrows():
    plt.text(row['Componente 1'] + 0.1, row['Componente 2'], row['Supermercado'], fontsize=9)

plt.title('Clusterização de Supermercados com Base nos Preços dos Produtos (PCA)')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.legend(title='Cluster')
plt.grid(True)
plt.show()

import pandas as pd
from sklearn.cluster import KMeans

# Carregar os dados do arquivo CSV
data = pd.read_csv('../precos_supermercados_4.csv')

# Definir os itens como índice
data.set_index('Item', inplace=True)

# Transpor os dados para que os supermercados sejam as linhas e os itens as colunas
data_transposed = data.T

# Aplicar K-Means para clustering
kmeans = KMeans(n_clusters=3, random_state=42)  # Escolha o número de clusters
clusters = kmeans.fit_predict(data_transposed)

# Adicionar os clusters ao DataFrame transposto
data_transposed['Cluster'] = clusters

# Adicionar o nome do supermercado como uma coluna
data_transposed['Supermercado'] = data_transposed.index

# Reorganizar as colunas para que 'Supermercado' e 'Cluster' sejam as primeiras colunas
colunas = ['Supermercado', 'Cluster'] + [col for col in data_transposed.columns if col not in ['Supermercado', 'Cluster']]
data_transposed = data_transposed[colunas]

# Exibir o DataFrame com supermercados e clusters
print(data_transposed)

# Salvar o DataFrame em Excel
data_transposed.to_excel('supermercados_com_clusters.xlsx', index=False)

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados do arquivo CSV
data = pd.read_csv('../precos_supermercados_4.csv')

# Definir os itens como índice
data.set_index('Item', inplace=True)

# Transpor os dados para que os supermercados sejam as linhas e os itens as colunas
data_transposed = data.T

# Aplicar K-Means para clustering
kmeans = KMeans(n_clusters=3, random_state=42)  # Escolha o número de clusters
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

# Plotar os clusters em um gráfico de dispersão 2D
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='Componente 1', 
    y='Componente 2', 
    hue='Cluster', 
    data=reduced_df, 
    palette='viridis', 
    s=100, 
    legend='full'
)

# Adicionar rótulos dos supermercados no gráfico
for i, row in reduced_df.iterrows():
    plt.text(row['Componente 1'] + 0.1, row['Componente 2'], row['Supermercado'], fontsize=9)

plt.title('Clusterização de Supermercados com Base nos Preços dos Produtos (PCA)')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.legend(title='Cluster')
plt.grid(True)
plt.show()

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados do arquivo CSV
data = pd.read_csv('../precos_supermercados_4.csv')

# Definir os itens como índice
data.set_index('Item', inplace=True)

# Transpor os dados para que os supermercados sejam as linhas e os itens as colunas
data_transposed = data.T

# Aplicar K-Means para clustering
kmeans = KMeans(n_clusters=3, random_state=42)  # Escolha o número de clusters
clusters = kmeans.fit_predict(data_transposed)

# Adicionar os clusters ao DataFrame transposto
data_transposed['Cluster'] = clusters

# Calcular a média dos preços por cluster
cluster_means = data_transposed.groupby('Cluster').mean()

# Transformar o DataFrame para o formato longo (melhor para Seaborn)
cluster_means_long = cluster_means.reset_index().melt(id_vars=['Cluster'], var_name='Item', value_name='Preço Médio')

# Plotar o gráfico de barras agrupadas
plt.figure(figsize=(12, 6))
sns.barplot(x='Item', y='Preço Médio', hue='Cluster', data=cluster_means_long, palette='viridis')
plt.title('Preço Médio dos Produtos por Cluster')
plt.xlabel('Item')
plt.ylabel('Preço Médio')
plt.xticks(rotation=45)
plt.legend(title='Cluster')
plt.grid(True)
plt.show()

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Carregar os dados do arquivo CSV
data = pd.read_csv('../precos_supermercados_4.csv')

# Definir os itens como índice
data.set_index('Item', inplace=True)

# Transpor os dados para que os supermercados sejam as linhas e os itens as colunas
data_transposed = data.T

# Aplicar K-Means para clustering
kmeans = KMeans(n_clusters=3, random_state=42)  # Escolha o número de clusters
clusters = kmeans.fit_predict(data_transposed)

# Adicionar os clusters ao DataFrame transposto
data_transposed['Cluster'] = clusters

# Reduzir a dimensionalidade dos dados para 3D usando PCA
pca = PCA(n_components=3)
reduced_data = pca.fit_transform(data_transposed.drop(columns=['Cluster']))

# Criar um DataFrame com os dados reduzidos e os clusters
reduced_df = pd.DataFrame(reduced_data, columns=['Preços Altos', 'Preços Médios', 'Preços Baixos'])
reduced_df['Cluster'] = clusters
reduced_df['Supermercado'] = data_transposed.index

# Plotar os clusters em um gráfico de dispersão 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Definir cores para cada cluster
colors = ['red', 'blue', 'green']
for cluster, color in zip(reduced_df['Cluster'].unique(), colors):
    cluster_data = reduced_df[reduced_df['Cluster'] == cluster]
    ax.scatter(
        cluster_data['Preços Altos'], 
        cluster_data['Preços Médios'], 
        cluster_data['Preços Baixos'], 
        c=color, 
        label=f'Cluster {cluster}', 
        s=100
    )

# Adicionar rótulos dos supermercados no gráfico
for i, row in reduced_df.iterrows():
    ax.text(row['Preços Altos'], row['Preços Médios'], row['Preços Baixos'], row['Supermercado'], fontsize=9)

# Configurações do gráfico
ax.set_title('Clusterização de Supermercados com Base nos Preços dos Produtos (PCA 3D)')
ax.set_xlabel('Preços Altos (Componente 1)')
ax.set_ylabel('Preços Médios (Componente 2)')
ax.set_zlabel('Preços Baixos (Componente 3)')
ax.legend(title='Cluster')
plt.show()

import plotly.express as px

# Criar um gráfico 3D interativo com Plotly
fig = px.scatter_3d(
    reduced_df, 
    x='Preços Altos', 
    y='Preços Médios', 
    z='Preços Baixos', 
    color='Cluster', 
    hover_name='Supermercado', 
    title='Clusterização de Supermercados (PCA 3D)'
)

# Exibir o gráfico
fig.show()