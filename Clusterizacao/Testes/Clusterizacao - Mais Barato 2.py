import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from mpl_toolkits.mplot3d import Axes3D

# Carregar os dados
df = pd.read_csv("../precos_supermercados_4.csv", sep=',', decimal='.')

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
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Carregar os dados
df = pd.read_csv("../precos_supermercados_4.csv")

# Encontrar o supermercado mais barato para cada item
df["Supermercado Mais Barato"] = df.iloc[:, 1:].idxmin(axis=1)

# Contar quantos produtos cada supermercado tem como o mais barato
contagem_supermercado = df["Supermercado Mais Barato"].value_counts()

# Criar o gráfico 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Definir coordenadas
x = np.arange(len(contagem_supermercado))  # Supermercados
y = np.zeros(len(contagem_supermercado))   # Base no eixo Y
z = np.zeros(len(contagem_supermercado))   # Base no eixo Z

# Altura das barras
dx = np.ones(len(contagem_supermercado))  # Largura das barras
dy = np.ones(len(contagem_supermercado))  # Profundidade das barras
dz = contagem_supermercado.values  # Número de produtos mais baratos

# Criar as barras
ax.bar3d(x, y, z, dx, dy, dz, color='b', alpha=0.7)

# Adicionar rótulos
ax.set_xticks(x)
ax.set_xticklabels(contagem_supermercado.index, rotation=45, ha='right')
ax.set_xlabel("Supermercados")
ax.set_ylabel("Eixo Y")
ax.set_zlabel("Quantidade de Produtos Mais Baratos")
ax.set_title("Clusterização dos Supermercados Mais Baratos")

plt.show()

# Mostrar tabela final
df_resultado = df[["Item", "Supermercado Mais Barato"]]
print(df_resultado)
