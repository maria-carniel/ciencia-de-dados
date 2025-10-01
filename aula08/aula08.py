import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Faz a leitura do arquivo CSV a partir de uma URL ou Arquivo
dados = pd.read_csv('./aula08/desmatamento_prodes.csv')

#Exibe os dados
print(dados)

print('-+-' * 50)

#Exibindo a matriz de correlação de pearson
#Fornecendo um pré-análise dos dados para encontrar
#correlações fortes positivas/negativas ou sem correlação
print(dados.corr().round(2))