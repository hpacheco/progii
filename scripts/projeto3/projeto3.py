import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
import networkx as nx
import json
import geopandas as gpd

#T1

def filename(f): return os.path.splitext(os.path.basename(f))[0]
codons = { filename(file) : pd.read_csv(file,index_col="codon") for file in glob.glob("dados/codons/*.csv") }

def constroiMatrix() -> np.array:
    return None

def desenhaHeatMap():

    data = constroiMatrix()

    # falta o código para desenhar

    plt.show()

#T2

df = pd.read_csv('dados/estat_proj_stp24.tsv', sep='\t',index_col="freq,indic_de,projection,geo\\TIME_PERIOD")

def desenhaPopulacaoPaisIndice(ax,pais,indice):

    # desenha um gráfico
    # usar o Axes ax recebido como argumento e não fazer plt.show() aqui
    return None

def testeDesenhaPopulacaoPaisIndice():
    _,ax = plt.subplots()
    desenhaPopulacaoPaisIndice(ax,'AT',"PC_Y15_74")
    plt.show()

def desenhaPopulacao():
    # cria botões e desenha um gráfico chamando desenhaPopulacaoPaisIndice
    return None

#T3

invasoras = pd.read_csv("dados/0008817-250402121839773.csv",sep="\t")
distritos = gpd.read_file("dados/distritos.geojson")

def desenhaInvasoras():
    # desenha o mapa
    plt.show()

def desenhaPorto():
    # desenha o mapa
    plt.show()

#T4

with open("dados/21A.json") as f:
    # a árvore filogenética do vírus Sars-Cov-2 para a variante Delta (21A)
    cov_21A = json.load(f)

def constroiGrafo() -> nx.DiGraph:
    return None

def desenhaFilogenetica():
    g = constroiGrafo()
    # desenha o grafo
    plt.show()
