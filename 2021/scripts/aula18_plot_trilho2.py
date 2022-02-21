import matplotlib.pyplot as plt
import contextily as ctx
import geopandas as gpd
import pandas as pd
import fiona

gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'
trilho2 = gpd.read_file('../dados/Fisgas-de-Ermelo.kml', driver='KML')

_,ax = plt.subplots(figsize=(8,5))
trilho2.plot(ax=ax, color='blue')

# acrescenta mapa
topo = ctx.providers.OpenTopoMap
ctx.add_basemap(ax,crs=4326,source=topo)

ermelo = trilho2['geometry'][2]
fisgasX = float('-inf');
fisgasY = float('-inf')
for x, y, z in trilho2['geometry'][0].coords:
    if x > fisgasX: fisgasX = x; fisgasY = y

plt.text(ermelo.x, ermelo.y, ' Ermelo', fontsize=12, color='blue')
plt.text(fisgasX, fisgasY, ' Fisgas de Ermelo', fontsize=12, color='blue')

# desenha o gráfico
plt.show()


