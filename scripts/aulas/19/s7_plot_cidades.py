import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import contextily as ctx

gdf = gpd.read_file('cidades.geojson')

# desenha um plot com tamanho dos marcadores proporcional à população
fig,ax = plt.subplots(figsize=(10,10))
gdf.plot(ax=ax,markersize=gdf['population']/1000)

# acrescenta mapa
ctx.add_basemap(ax,zoom=6,crs=4326,source=ctx.providers.CartoDB.Voyager)
plt.show()