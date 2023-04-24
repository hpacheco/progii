import pandas as pd
import geopandas as gpd
import contextily as ctx
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
from matplotlib.widgets import Slider
import networkx as nx
import plotly.express as px

# Tarefa 1

def desenhaDiagnostico():

    breast_cancer = pd.read_csv('dados/breast_cancer.csv')

    # falta o código para desenhar

    plt.show()

# Tarefa 2

nuclear_forces = pd.read_csv('dados/nuclear_forces.csv',on_bad_lines='skip',delimiter='\t')

def desenhaNuclearPais(ax,pais):

    # desenha um gráfico pie
    # usar o Axes ax recebido como argumento e não fazer plt.show() aqui
    return None

def testeDesenhaNuclearPais():
    desenhaNuclearPais(plt,'Russia')
    plt.show()

def desenhaNuclearCategoria(ax,categoria):

    # desenha um gráfico pie
    # usar o Axes ax recebido como argumento e não fazer plt.show() aqui
    return None

def testeDesenhaNuclearCategoria():
    desenhaNuclearCategoria(plt,'Retired')
    plt.show()

def desenhaNuclear():
    # cria radiobuttons e desenha um gráfico pie chamando testeDesenhaNuclearPais e testeDesenhaNuclearCategoria
    return None

# Tarefa 3

def leWasteGeo():
    data = pd.read_csv('dados/wastewaterData.csv')
    sites = pd.read_csv('dados/wastewaterSites.csv')
    gdf = None # construir o GeoDataFrame
    return gdf

def desenhaMetabolitoAno(ax,gdf,metabolito,ano):
    return None

def testeDesenhaMetabolitoAno():
    desenhaMetabolitoAno(plt,leWasteGeo(),'amphetamine',2022)
    plt.show()

def desenhaMapa():
    gdf = leWasteGeo()
    _, ax = plt.subplots(figsize=(10, 10)) # pode ajustar dimensões

    metabolitos = [] # criar uma lista de metabolitos existentes a partir do GeoDataFrame
    metabolito_selecionado = metabolitos[0] # por defeito o primeiro metabolito da lista
    # constroi um Radio Button para seleção de metabolitos
    button = RadioButtons(plt.axes([0.1, 0.8, 0.8, 0.15]), metabolitos, active=0)

    min_ano = 0; max_ano = 0 # determinar ano mínimo e máximo a partir do GeoDataFrame
    ano_selecionado = 0  # escolher um ano para estar selecionado por defeito
    slider = Slider(plt.axes([0.1, 0.7, 0.8, 0.1]), 'Ano', min_ano, max_ano, valinit=ano_selecionado, valstep=1)

    desenhaMetabolitoAno(ax, gdf, metabolito_selecionado, ano_selecionado)

    def reageMetabolito(metabolito):
        metabolito_selecionado = metabolito
        ax.clear()
        desenhaMetabolitoAno(ax, gdf, metabolito_selecionado, ano_selecionado)
        plt.draw()

    def reageAno(ano):
        ano_selecionado = ano
        ax.clear()
        desenhaMetabolitoAno(ax, gdf, metabolito_selecionado, ano_selecionado)
        plt.draw()

    button.on_clicked(reageMetabolito)
    slider.on_changed(reageAno)
    plt.show()

def testeDesenhaMapa():
    desenhaMapa()

# Tarefa 4

genes = pd.read_csv('dados/genes.txt',sep="\t")
genes.set_index('Input',inplace=True)
genes.drop(columns=set(genes.columns).difference({'Chr','Term'}),inplace=True)
genes.dropna(inplace=True)
genes.sort_values(by=['Chr'],inplace=True)

def identificaGenes(subtermo):
    g = nx.Graph()
    # preencher o grafo `g`
    return g

def desenhaGenes(subtermo):
    g = identificaGenes(subtermo)
    # desenhar o grafo `g`
    plt.show()

# Tarefa 5

def analizaTemperaturas():
    dfs = pd.read_excel("dados/PT100-tx-tn-prec.xlsx", sheet_name=['tmin', 'tmax'])
    tmin = dfs['tmin']
    tmax = dfs['tmax']
    return None # criar e retornar um dataframe

def desenhaTemperaturas():
    df = analizaTemperaturas()
    fig = px.scatter(df) # acrescentar outros parâmetros para configurar o gráfico
    fig.write_html("ipma.html")