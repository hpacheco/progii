
import numpy as np
import pandas as pd
import geopandas as geopd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import folium
import glob
import os
import pygame
from pygame.transform import *

import datetime

# Tarefa 1

def desenhaPrecos():

    brent = pd.read_csv('dados/brent.csv')
    gasolina = pd.read_csv('dados/gasolina.csv', delimiter=';')

    # falta o código para desenhar

    plt.show()

# Tarefa 2

def desenhaRefugiadosDia(ax,dia):
    dados_dia = pd.read_csv('dados/ukraine-refugees/'+dia+'.csv')

    # desenha um gráfico pie

def testeDesenhaRefugiadosDia():
    desenhaRefugiadosDia(plt,'2022-03-15')
    plt.show()

def desenhaRefugiadosDias():
    ficheiros = glob.glob('dados/ukraine-refugees/*.csv')
    dias = list(map(lambda x : os.path.basename(x)[0:10],ficheiros))
    # cria um slider e desenha cada gráfico pie chamando desenhaRefugiadosDia

# Tarefa 3

def populacaoUcrania():
    regioes = geopd.read_file("dados/Ukraine-regions.geojson")
    regioes.set_crs(epsg=4326, inplace=True)
    populacao = pd.read_csv('dados/ukraine-population.csv')
    # deve retornar um GeoDataFrame combinado
    return regioes

def desenhaRegioesUcrania(mapa,gdf):
    # cria regiões invisíveis
    #gjson = folium.GeoJson(gdf,style_function=lambda x: {'opacity': 0,'fillOpacity':0}).add_to(mapa)
    # adiciona uma tooltip a cada região de acordo com a coluna 'descricao' no GeoDataFrame
    #folium.features.GeoJsonTooltip(fields=['descricao'],labels=False).add_to(gjson)
    # adiciona um popup a cada região de acordo com a coluna 'descricao' no GeoDataFrame
    #folium.features.GeoJsonPopup(fields=['descricao'],labels=False).add_to(gjson)
    return None

def desenhaPopulacaoUcrania():
    gdf = populacaoUcrania()
    lat = 0 # change
    lon = 0 # change
    mapa = folium.Map([lat,lon],zoom_start=2)
    folium.Choropleth(
        geo_data=gdf,
        data=gdf,
        columns=["regiao","densidade"],
        key_on="feature.properties.regiao",
        fill_color="YlGnBu",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Densidade Populacional",
    ).add_to(mapa)

    desenhaRegioesUcrania(mapa,gdf)

    mapa.save("mapa.html")

# Tarefa 4

event_a = ['ukr','rus','other']

def processaEventos():
    df = pd.read_csv('dados/events_latest.csv')
    # alterar o dataframe
    return df

class Animacao:

    def __init__(self, date, height=None):
        """inicializa uma nova animação (altura da janela opcional)"""
        pygame.init()
        if height:
            self.height = height
        else:
            monitor = pygame.display.Info()
            self.height = monitor.current_h

        # inicializa o pygame
        pygame.font.init()
        self.font = pygame.font.SysFont('timesnewromanbold', 40)
        self.clock = pygame.time.Clock()

        # map and screen sizes; maps have fixed top borders and sizes
        self.crop_top = 635; self.map_width = 2550; self.map_height = 2720
        self.proportion = self.height / self.map_height
        self.width = self.map_width * self.proportion  # calculate screen width to keep map proportion

        # load map and resize it to screen
        img = pygame.image.load('mapas/' + str(date) + '.png')
        self.map = pygame.Surface((self.map_width, self.map_height))
        self.map.blit(img, (0, 0), (0, self.crop_top, self.map_width, self.crop_top + self.map_height))
        self.map = smoothscale(self.map, (self.width, self.height))

        self.df = processaEventos()  # carrega dados de eventos
        self.df = self.df[self.df['date'] == np.datetime64(date)]  # seleciona dados do dia da animação

        # coordenadas gps fixas para a projeção do mapa
        self.min_lon = 21.5; self.max_lon = 42.55
        self.min_lat = 39.26; self.max_lat = 54.20
        self.dif_lon = self.max_lon - self.min_lon
        self.dif_lat = self.max_lat - self.min_lat

    # traduz coordenadas GPS do mapa em píxeis (aproximado, não tem em consideração curvatura da Terra)
    def toX(self,lon): return (lon - self.min_lon) * (self.width / self.dif_lon)
    def toY(self,lat): return (self.dif_lat - (lat - self.min_lat)) * (self.height / self.dif_lat)

    def desenhaFrame(self,screen,minute):
        """desenha um frame, correspondente a um minuto nos eventos"""
        """recebe um ecrâ e um minuto"""
        return None

    def run(self,fps):
        """recebe frames por segundo e uma lista de mapas opcional"""

        screen = pygame.display.set_mode((self.width,self.height))
        # desenha o mapa
        screen.blit(self.map, (0, 0))

        done = False; minutes = 0; day_minutes = 24 * 60
        while not done:
            # responde a eventos (fechar)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            # desenha e atualiza o frame da animação
            self.desenhaFrame(screen,minutes)
            pygame.display.update()

            self.clock.tick(fps)
            # 1 frame a cada tick
            minutes += 1
            # acaba a animação quando chega ao fim do dia
            if minutes >= day_minutes: done = True