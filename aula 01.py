# Faz a importação da biblioteca matplotlib e adiciona um alia (apelido)
# Usar linha de comando: python3 -m pip install matplotlib
import matplotlib.pyplot as plt 

def exibirGrafico ():
    # Definição dos grupos e valores 
    grupos = ['A', 'B', 'C']
    valores = [23, 38,12]
    
    # Configura um grafico de barras, onde recebe os grupos, valores
    # E opcionalmente as cores 
    plt.bar(grupos, valores, color =['red', 'blue', 'grey'])

    # Define o titulo do gráfico
    plt.title ('Grafico de Barras Simples')

    # Define o título do eixo X 
    # plt.xlabel ('Grupos')              