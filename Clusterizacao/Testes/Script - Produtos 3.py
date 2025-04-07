import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.cluster.hierarchy as sch
from scipy.spatial.distance import pdist
from sklearn.cluster import AgglomerativeClustering, KMeans
import pingouin as pg
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from scipy.stats import zscore

pio.renderers.default = 'browser'

# Carregar os dados do arquivo CSV
dados = pd.read_csv('../precos_supermercados_4.csv')
precos = dados.set_index('Item').T

# Exibir os dados
print(dados)

# Remover a coluna "Item" (não é numérica)
# precos = dados.drop(columns=['Item'])

# Estatísticas descritivas
tab_desc = precos.describe()
print(tab_desc)

# Matriz de correlações de Pearson
matriz_corr = pg.rcorr(precos, method='pearson', upper='pval', decimals=4, pval_stars={0.01: '***', 0.05: '**', 0.10: '*'})
print(matriz_corr)

# Mapa de calor da matriz de correlações
corr = precos.corr()

fig = go.Figure()
fig.add_trace(
    go.Heatmap(
        x=corr.columns,
        y=corr.index,
        z=np.array(corr),
        text=corr.values,
        texttemplate='%{text:.2f}',
        colorscale='viridis'
    )
)
fig.update_layout(height=600, width=600)
# fig.show()

# Aplicando o Z-score para padronizar as variáveis
precos_pad = precos.apply(zscore, ddof=1)
print(precos_pad)

plt.figure(figsize=(16, 8))
dend_sing = sch.linkage(precos_pad, method='single', metric='euclidean')
sch.dendrogram(dend_sing)
plt.title('Dendrograma Single Linkage', fontsize=16)
plt.xlabel('Supermercados', fontsize=16)
plt.ylabel('Distância Euclidiana', fontsize=16)
# plt.show()

# ANOVA para cada variável
for coluna in precos.columns:
    print(f"ANOVA para {coluna}:")
    anova_result = pg.anova(dv=coluna, between='cluster_complete', data=precos, detailed=True)
    print(anova_result.T)