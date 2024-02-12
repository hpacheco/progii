import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons
import contextily as ctx
import geopandas as gpd
import pandas as pd
import fiona

fiona.drvsupport.supported_drivers['KML'] = 'rw'

_,ax = plt.subplots(figsize=(10,8))

# trilho 1

trilho1 = gpd.read_file('Trilho-das-7-Lagoas.kml', driver='KML')
trilho1.plot(ax=ax,color='green')

xertelo = trilho1['geometry'][0]
lagoasX = float('inf'); lagoasY = float('inf')
for x,y,z in trilho1['geometry'][2].coords:
    if x < lagoasX: lagoasX=x; lagoasY=y

plt.text(xertelo.x, xertelo.y, ' Xertelo', fontsize=12, color='green');
plt.text(lagoasX, lagoasY, ' 7 Lagoas', fontsize=12, color='green');

# trilho 2

trilho2 = gpd.read_file('Fisgas-de-Ermelo.kml', driver='KML')
trilho2.plot(ax=ax, color='blue')

ermelo = trilho2['geometry'][2]
fisgasX = float('-inf');
fisgasY = float('-inf')
for x, y, z in trilho2['geometry'][0].coords:
    if x > fisgasX: fisgasX = x; fisgasY = y

plt.text(ermelo.x, ermelo.y, ' Ermelo', fontsize=12, color='blue')
plt.text(fisgasX, fisgasY, ' Fisgas de Ermelo', fontsize=12, color='blue')

# botão interativo

lagoas = True
fisgas = True
rect = plt.axes([0.7, 0.9, 0.1, 0.08])
button = CheckButtons(rect,('Lagoas','Fisgas'),(lagoas,fisgas))

trilhos = pd.concat([trilho1,trilho2])
b0 = -7.451, 41.5, -7.452, 41.6
b12 = trilhos.total_bounds
b1 = trilho1.total_bounds
b2 = trilho2.total_bounds

def zoom():
    if lagoas:
        if fisgas: bb = b12
        else: bb = b1
    else:
        if fisgas: bb = b2
        else: bb = b0
    minx, miny, maxx, maxy = bb
    ax.set_xlim(minx,maxx)
    ax.set_ylim(miny,maxy)
    plt.draw()

def reage(label):
    global lagoas, fisgas
    if label == 'Lagoas': lagoas = not lagoas
    elif label == 'Fisgas': fisgas = not fisgas
    zoom()

button.on_clicked(reage)

# acrescenta mapa
topo = ctx.providers.OpenTopoMap

ctx.bounds2raster(*b12,ll=True,source=topo,path='map.tif')

ctx.add_basemap(ax,crs=4326,source='map.tif')

# desenha o gráfico
plt.show()


