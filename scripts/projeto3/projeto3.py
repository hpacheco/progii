
import pandas as pd
import geopandas as gpd
import contextily as ctx
import matplotlib.pyplot as plt
from shapely import *
from shapely.plotting import *
import math
import networkx as nx

# Tarefa 1

# um tuplo (axioma,regras de expansão,ângulo inicial,ângulo de rotação)
lsystem = tuple[str,dict[str,str],float,float]

tree1 : lsystem = ("F",{"F":"F[-F]F[+F][F]"},90,30)
tree2 : lsystem = ("X",{"F":"FF","X":"F-[[X]+X]+F[+FX]-X"},90,22.5)
bush1 : lsystem = ("Y",{"X":"X[-FFF][+FFF]FX","Y":"YFX[+Y][-Y]"},90,25.7)
bush2 : lsystem = ("VZFFF",{"V":"[+++W][---W]YV","W":"+X[-W]Z","X":"-W[+X]Z","Y":"YZ","Z":"[-FFF][+FFF]F"},90,20)
plant1 : lsystem = ("X",{"X":"F+[[X]-X]-F[-FX]+X)","F":"FF"},60,25)

def expandeLSystem(l:lsystem,n:int) -> str:
    return None

def desenhaTurtle(steps:str,start_pos:(float,float),start_angle:float,side:float,theta:float) -> list[(float,float)]:
    pos = start_pos
    angle = start_angle
    lines = [[pos]]
    stack = []
    for s in steps:
        if s=="F":
            pos = (pos[0] + side * math.cos(math.radians(angle)),pos[1] + side * math.sin(math.radians(angle)))
            lines[-1].append(pos)
        elif s=="-": angle = angle-theta
        elif s=="+": angle = angle+theta
        elif s=="[": stack.append((pos,angle))
        elif s=="]": pos,angle = stack.pop() ; lines.append([pos])
    return lines

def desenhaLSystem(l:lsystem,n:int):

    s = expandeLSystem(l,n)

    # falta o código para desenhar

    plt.show()

# Tarefa 2

packaging_waste = pd.read_csv('dados/env_waspac.tsv',na_values=":")
municipal_waste = pd.read_csv('dados/env_wasmun.tsv',na_values=":")

packaging_waste.plot()
plt.show()

def desenhaReciclagemPaisIndice(ax,pais,indice):

    # desenha um gráfico
    # usar o Axes ax recebido como argumento e não fazer plt.show() aqui
    return None

def testeDesenhaReciclagemPaisIndice():
    desenhaReciclagemPaisIndice(plt,'Russia')
    plt.show()

def desenhaReciclagem():
    # cria botões e desenha um gráfico chamando desenhaReciclagemPaisIndice
    return None

# Tarefa 3

listings = pd.read_csv('dados/listings.csv')
neighbourhoods = gpd.read_file("dados/neighbourhoods.geojson")

def desenhaZonas():
    # preencher
    plt.show()

def desenhaZonas():
    # preencher
    plt.show()

def desenhaTop():
    # preencher
    plt.show()

# Tarefa 4

bay = pd.read_csv('dados/bay.csv')

def constroiEcosistema() -> nx.DiGraph:
    return None

def desenhaEcosistema():
    g = constroiEcosistema()
    # desenha o grafo
    plt.show()