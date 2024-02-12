import matplotlib.pyplot as plt
import contextily as ctx
import geopandas as gpd
import pandas as pd
import fiona
import urllib.request

#url = 'https://www.vagamundos.pt/wp-content/uploads/2019/05/Trilho-das-7-Lagoas.kml'
#urllib.request.urlretrieve(url,'Trilho-das-7-Lagoas.kml')

fiona.drvsupport.supported_drivers['KML'] = 'rw'
trilho1 = gpd.read_file('Trilho-das-7-Lagoas.kml', driver='KML')

print(trilho1)

_,ax = plt.subplots(figsize=(5,7))
trilho1.plot(ax=ax,color='green')

# acrescenta mapa
topo = ctx.providers.OpenTopoMap
ctx.add_basemap(ax,crs=4326,source=topo)

xertelo = trilho1['geometry'][0]
lagoasX = float('inf'); lagoasY = float('inf')
# procura ponto mais à esquerda (longitude menor) no trilho
for x,y,z in trilho1['geometry'][2].coords:
    if x < lagoasX: lagoasX=x; lagoasY: lagoasY=y

ax.text(xertelo.x, xertelo.y, ' Xertelo', fontsize=12, color='green');
ax.text(lagoasX, lagoasY, ' 7 Lagoas', fontsize=12, color='green');

# desenha o gráfico
plt.show()

