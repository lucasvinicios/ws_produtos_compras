# import numpy as np
# import matplotlib.pyplot as plt

# class KMeans:
#     def __init__(self, k=3, max_iter=100, tol=1e-4):
#         self.k = k  # Número de clusters
#         self.max_iter = max_iter  # Número máximo de iterações
#         self.tol = tol  # Tolerância para convergência

#     def fit(self, X):
#         # Inicialização dos centroides aleatórios
#         self.centroids = X[np.random.choice(X.shape[0], self.k, replace=False)]
        
#         for _ in range(self.max_iter):
#             # Atribuição: cada ponto ao cluster mais próximo
#             labels = self._assign_clusters(X)
            
#             # Atualização: recalcular os centroides
#             new_centroids = self._update_centroids(X, labels)
            
#             # Verificar convergência
#             if np.allclose(self.centroids, new_centroids, atol=self.tol):
#                 break
            
#             self.centroids = new_centroids

#         self.labels_ = labels
#         return self

#     def _assign_clusters(self, X):
#         # Calcular a distância de cada ponto para cada centroide
#         distances = np.sqrt(((X[:, np.newaxis] - self.centroids) ** 2).sum(axis=2))
#         # Atribuir cada ponto ao cluster mais próximo
#         return np.argmin(distances, axis=1)

#     def _update_centroids(self, X, labels):
#         # Calcular a média dos pontos em cada cluster
#         new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(self.k)])
#         return new_centroids

#     def predict(self, X):
#         # Prever os clusters para novos dados
#         return self._assign_clusters(X)

# # Exemplo de uso
# if __name__ == "__main__":
#     # Dados de exemplo
#     np.random.seed(42)
#     X = np.vstack([
#         np.random.normal(loc=[0, 0], scale=1, size=(50, 2)),
#         np.random.normal(loc=[5, 5], scale=1, size=(50, 2)),
#         np.random.normal(loc=[10, 10], scale=1, size=(50, 2))
#     ])

#     # Aplicar K-means
#     kmeans = KMeans(k=3)
#     kmeans.fit(X)

#     # Visualizar os clusters
#     plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis', s=50)
#     plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:, 1], c='red', marker='X', s=200, label='Centroids')
#     plt.title('K-means Clustering')
#     plt.legend()
#     plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class KMeans:
    def __init__(self, k=3, max_iter=100, tol=1e-4):
        self.k = k  # Número de clusters
        self.max_iter = max_iter  # Número máximo de iterações
        self.tol = tol  # Tolerância para convergência

    def fit(self, X):
        # Inicialização dos centroides aleatórios
        self.centroids = X[np.random.choice(X.shape[0], self.k, replace=False)]
        
        for _ in range(self.max_iter):
            # Atribuição: cada ponto ao cluster mais próximo
            labels = self._assign_clusters(X)
            
            # Atualização: recalcular os centroides
            new_centroids = self._update_centroids(X, labels)
            
            # Verificar convergência
            if np.allclose(self.centroids, new_centroids, atol=self.tol):
                break
            
            self.centroids = new_centroids

        self.labels_ = labels
        return self

    def _assign_clusters(self, X):
        # Calcular a distância de cada ponto para cada centroide
        distances = np.sqrt(((X[:, np.newaxis] - self.centroids) ** 2).sum(axis=2))
        # Atribuir cada ponto ao cluster mais próximo
        return np.argmin(distances, axis=1)

    def _update_centroids(self, X, labels):
        # Calcular a média dos pontos em cada cluster
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(self.k)])
        return new_centroids

    def predict(self, X):
        # Prever os clusters para novos dados
        return self._assign_clusters(X)

# Carregar os dados do arquivo CSV
data = pd.read_csv('../precos_supermercados_4.csv')

# Definir os itens como índice
data.set_index('Item', inplace=True)

# Transpor os dados para que os supermercados sejam as linhas e os itens as colunas
data_transposed = data.T

# Converter os dados para um array numpy
X = data_transposed.values

# Nomes dos supermercados (serão os centroides)
supermercados = data_transposed.index

# Nomes dos produtos
produtos = data.index

print(produtos)

# Aplicar K-means
kmeans = KMeans(k=len(supermercados))  # Número de clusters = número de supermercados
kmeans.fit(X)

# Reduzir a dimensionalidade para 2D usando PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

# Aplicar K-means aos dados reduzidos
kmeans.fit(X_reduced)

# Visualizar os clusters
plt.figure(figsize=(10, 6))

# Plotar os produtos (pontos)
# for i, produto in enumerate(produtos):
#     plt.scatter(X_reduced[i, 0], X_reduced[i, 1], c=kmeans.labels_[i], cmap='viridis', s=50)
#     plt.text(X_reduced[i, 0], X_reduced[i, 1], produto, fontsize=9, ha='right')

# Plotar os supermercados (centroides)
plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:, 1], c='red', marker='X', s=200, label='Supermercados')
for i, supermercado in enumerate(supermercados):
    plt.text(kmeans.centroids[i, 0], kmeans.centroids[i, 1], supermercado, fontsize=12, ha='right', color='red')

plt.title('Agrupamento de Produtos por Supermercado (K-means com PCA)')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.legend()
plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class KMeans:
    def __init__(self, k=3, max_iter=100, tol=1e-4):
        self.k = k  # Número de clusters
        self.max_iter = max_iter  # Número máximo de iterações
        self.tol = tol  # Tolerância para convergência

    def fit(self, X):
        # Inicialização dos centroides aleatórios
        self.centroids = X[np.random.choice(X.shape[0], self.k, replace=False)]
        
        for _ in range(self.max_iter):
            # Atribuição: cada ponto ao cluster mais próximo
            labels = self._assign_clusters(X)
            
            # Atualização: recalcular os centroides
            new_centroids = self._update_centroids(X, labels)
            
            # Verificar convergência
            if np.allclose(self.centroids, new_centroids, atol=self.tol):
                break
            
            self.centroids = new_centroids

        self.labels_ = labels
        return self

    def _assign_clusters(self, X):
        # Calcular a distância de cada ponto para cada centroide
        distances = np.sqrt(((X[:, np.newaxis] - self.centroids) ** 2).sum(axis=2))
        # Atribuir cada ponto ao cluster mais próximo
        return np.argmin(distances, axis=1)

    def _update_centroids(self, X, labels):
        # Calcular a média dos pontos em cada cluster
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(self.k)])
        return new_centroids

    def predict(self, X):
        # Prever os clusters para novos dados
        return self._assign_clusters(X)

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
kmeans = KMeans(k=len(supermercados))  # Número de clusters = número de supermercados
kmeans.fit(X)

# Reduzir a dimensionalidade para 2D usando PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

# Aplicar K-means aos dados reduzidos
kmeans.fit(X_reduced)

# Visualizar os clusters
plt.figure(figsize=(10, 6))

# Plotar os produtos (pontos)
for i, produto in enumerate(produtos):
    plt.scatter(X_reduced[i, 0], X_reduced[i, 1], c=kmeans.labels_[i], cmap='viridis', s=50)
    plt.text(X_reduced[i, 0], X_reduced[i, 1], produto, fontsize=9, ha='right')

# Plotar os supermercados (centroides)
plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:, 1], c='red', marker='X', s=200, label='Supermercados')
for i, supermercado in enumerate(supermercados):
    plt.text(kmeans.centroids[i, 0], kmeans.centroids[i, 1], supermercado, fontsize=12, ha='right', color='red')

plt.title('Agrupamento de Produtos por Supermercado (K-means com PCA)')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.legend()
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class KMeans:
    def __init__(self, k=3, max_iter=100, tol=1e-4):
        self.k = k  # Número de clusters
        self.max_iter = max_iter  # Número máximo de iterações
        self.tol = tol  # Tolerância para convergência

    def fit(self, X):
        # Inicialização dos centroides aleatórios
        self.centroids = X[np.random.choice(X.shape[0], self.k, replace=False)]
        
        for _ in range(self.max_iter):
            # Atribuição: cada ponto ao cluster mais próximo
            labels = self._assign_clusters(X)
            
            # Atualização: recalcular os centroides
            new_centroids = self._update_centroids(X, labels)
            
            # Verificar convergência
            if np.allclose(self.centroids, new_centroids, atol=self.tol):
                break
            
            self.centroids = new_centroids

        self.labels_ = labels
        return self

    def _assign_clusters(self, X):
        # Calcular a distância de cada ponto para cada centroide
        distances = np.sqrt(((X[:, np.newaxis] - self.centroids) ** 2).sum(axis=2))
        # Atribuir cada ponto ao cluster mais próximo
        return np.argmin(distances, axis=1)

    def _update_centroids(self, X, labels):
        # Calcular a média dos pontos em cada cluster
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(self.k)])
        return new_centroids

    def predict(self, X):
        # Prever os clusters para novos dados
        return self._assign_clusters(X)

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
kmeans = KMeans(k=len(supermercados))  # Número de clusters = número de supermercados
kmeans.fit(X)

# Reduzir a dimensionalidade para 2D usando PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

# Aplicar K-means aos dados reduzidos
kmeans.fit(X_reduced)

# Visualizar os clusters
plt.figure(figsize=(10, 6))

# Plotar os produtos (pontos)
for i, produto in enumerate(produtos):
    plt.scatter(X_reduced[i, 0], X_reduced[i, 1], c=kmeans.labels_[i], cmap='viridis', s=50)
    plt.text(X_reduced[i, 0], X_reduced[i, 1], produto, fontsize=9, ha='right')

    # Conectar o ponto ao centroide do cluster ao qual pertence
    centroid = kmeans.centroids[kmeans.labels_[i]]
    plt.plot([X_reduced[i, 0], centroid[0]], [X_reduced[i, 1], centroid[1]], 'k--', linewidth=0.5)

# Plotar os supermercados (centroides)
plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:, 1], c='red', marker='X', s=200, label='Supermercados')
for i, supermercado in enumerate(supermercados):
    plt.text(kmeans.centroids[i, 0], kmeans.centroids[i, 1], supermercado, fontsize=12, ha='right', color='red')

plt.title('Agrupamento de Produtos por Supermercado (K-means com PCA)')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.legend()
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class KMeans:
    def __init__(self, k=3, max_iter=100, tol=1e-4):
        self.k = k  # Número de clusters
        self.max_iter = max_iter  # Número máximo de iterações
        self.tol = tol  # Tolerância para convergência

    def fit(self, X):
        # Inicialização dos centroides aleatórios
        self.centroids = X[np.random.choice(X.shape[0], self.k, replace=False)]
        
        for _ in range(self.max_iter):
            # Atribuição: cada ponto ao cluster mais próximo
            labels = self._assign_clusters(X)
            
            # Atualização: recalcular os centroides
            new_centroids = self._update_centroids(X, labels)
            
            # Verificar convergência
            if np.allclose(self.centroids, new_centroids, atol=self.tol):
                break
            
            self.centroids = new_centroids

        self.labels_ = labels
        return self

    def _assign_clusters(self, X):
        # Calcular a distância de cada ponto para cada centroide
        distances = np.sqrt(((X[:, np.newaxis] - self.centroids) ** 2).sum(axis=2))
        # Atribuir cada ponto ao cluster mais próximo
        return np.argmin(distances, axis=1)

    def _update_centroids(self, X, labels):
        # Calcular a média dos pontos em cada cluster
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(self.k)])
        return new_centroids

    def predict(self, X):
        # Prever os clusters para novos dados
        return self._assign_clusters(X)

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
kmeans = KMeans(k=len(supermercados))  # Número de clusters = número de supermercados
kmeans.fit(X)

# Reduzir a dimensionalidade para 2D usando PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

# Aplicar K-means aos dados reduzidos
kmeans.fit(X_reduced)

# Visualizar os clusters
plt.figure(figsize=(12, 8))

# Cores para os clusters
cores = plt.cm.get_cmap('viridis', len(supermercados))

# Plotar os produtos (pontos pequenos)
for i, produto in enumerate(produtos):
    plt.scatter(X_reduced[i, 0], X_reduced[i, 1], color=cores(kmeans.labels_[i]), s=30)  # Pontos pequenos
    # Conectar o ponto ao centroide do cluster ao qual pertence
    centroid = kmeans.centroids[kmeans.labels_[i]]
    plt.plot([X_reduced[i, 0], centroid[0]], [X_reduced[i, 1], centroid[1]], 'k--', linewidth=0.5)

# Plotar os supermercados (centroides)
for i, supermercado in enumerate(supermercados):
    plt.scatter(kmeans.centroids[i, 0], kmeans.centroids[i, 1], color=cores(i), marker='X', s=200, label=supermercado)

# Adicionar legenda
plt.legend(title='Supermercados', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.title('Agrupamento de Produtos por Supermercado (K-means com PCA)')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.tight_layout()  # Ajustar layout para evitar cortes
plt.show()