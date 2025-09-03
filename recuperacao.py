import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Conjunto de dados exemplo 
dados = [120, 150, 170, 160, 180, 200, 210, 190, 220, 250, 240, 230]
df = pd.DataFrame({
        "Meses" : ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez'],
        "Vendas" : [120, 150, 170, 160, 180, 200, 210, 190, 220, 250, 240, 230]
    })

# Calcular quartis
quartis = np.percentile(df['Vendas'], [25, 50, 75])
print(f'Quartis: Q1={quartis[0]}, Q2={quartis[1]}, Q3={quartis[2]}')




# Vizualização por BoxPlot
plt.boxplot('vendas', vert=False)
plt.title('Boxplot das Notas')
plt.xlabel('Notas')
plt.show()
plt.savefig('chart5.png')