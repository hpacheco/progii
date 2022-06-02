import pygame, sys
from pygame.locals import *
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg

import pandas as pd
import contextily as ctx

# cria um axes e um canvas
fig,ax = plt.subplots(figsize=[8,8] # Inches
                     ,dpi=100) # 100 dots per inch, so the resulting buffer is 800x800 pixels
canvas = agg.FigureCanvasAgg(fig)

# converte o canvas de um gráfico matplotlib numa superfície pygame
def draw_canvas():
   canvas.draw()
   renderer = canvas.get_renderer()
   raw_data = renderer.tostring_rgb()
   size = canvas.get_width_height()
   return pygame.image.fromstring(raw_data,size,"RGB")

# inicializa o pygame
black = (0,0,0)
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('timesnewromanbold',40)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,800))

# carrega e desenha o basemap estático

data = pd.read_csv('../../dados/atlantic_storms.csv',usecols=['date','name','latitude','longitude','maximum_sustained_wind_knots'])
data = data [ data['name'] != 'UNNAMED' ]
data['date'] = pd.to_datetime(data['date'])
data['year'] = data['date'].dt.year

min_lon = -110; max_lon = 0
min_lat = -30; max_lat = 80
dif_max = 110
ax.set_xlim(min_lon,max_lon)
ax.set_ylim(min_lat,max_lat)

# reduz as margens
ax.axis('off')
plt.subplots_adjust(top=1,bottom=0,right=1,left=0,hspace=0,wspace=0)

mapnik = ctx.providers.OpenStreetMap.Mapnik
ctx.add_basemap(ax,crs=4326,source=mapnik)
background = draw_canvas()
screen.blit(background,(0,0))

# atualiza janela
pygame.display.update()

# traduz coordenada GPS em píxeis
def toX(lon): return (lon-min_lon) * (800/dif_max)
def toY(lat): return (dif_max-(lat-min_lat)) * (800/dif_max)

done = False; frame = 0; name=''
while not done:
    # responde a eventos (fechar)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if frame < len(data):
        row = data.iloc[frame]
        newname = row['name']
        year = row['year']
        if newname != name:
            # desenha nome + ano no topo do ecrã
            screen.blit(background,(0,0))
            text = font.render(newname + ' ' + str(year),False,black)
            screen.blit(text,(screen.get_width()/2-text.get_width()/2,30))
        name = newname
        # desenha posição atual no mapa
        lat = row['latitude']
        lon = row['longitude']
        wind = row['maximum_sustained_wind_knots']
        pygame.draw.circle(screen,(min(255,wind*2),50,50),(toX(lon),toY(lat)),wind/5)
        pygame.display.update()
    clock.tick(10); frame +=1
