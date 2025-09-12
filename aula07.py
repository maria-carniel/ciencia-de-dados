import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

# Criação de um dataset fictício
np.random.seed(42)

dados = pd.DataFrame({ 
    "Orçamento_Campanha": np.random.randint(1000, 5000, size=100),
    "Visualizacoes_Anuncio": np.random.randint(2000, 20000, size=100),
    "Vendas": np.random.randint(100, 20000, size=100),
    "Cliques": np.random.randint(100, 20000, size=100)
})

# Pairplot: Vizualizar todas as relações
sns.pairplot(dados)
plt.show()
plt.savefig('pairplot7.png')

#Jointplot/; Explorar a relação entre duas variáveis específicoas
sns.jointplot(x='Visualizacoes_Anuncio', y='Vendas', data=dados, kind="reg")
plt.show()
plt.savefig('jointplot7.png')

#Lmplot: Visualizar a linha de regressão 
sns.jointplot(x='Visualizacoes_Anuncio', y='Vendas', data=dados, kind="reg")
plt.show()
plt.savefig('implot7.png')
