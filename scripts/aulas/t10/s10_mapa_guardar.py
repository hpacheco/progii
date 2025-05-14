import matplotlib.pyplot as plt
import contextily as ctx

# Porto
fig,ax = plt.subplots(figsize=(15,15))
west = -8.8
east = -8.3
south = 41
north = 41.5
ax.set_xlim(west,east)
ax.set_ylim(south,north)
ax.axis('off')

mapnik = ctx.providers.OpenStreetMap.Mapnik
# guarda o mapa para ficheiro
ctx.bounds2raster(west,south,east,north,ll=True,source=mapnik,path='map.tif')
# lê o mapa de ficheiro
ctx.add_basemap(ax,crs=4326,source='map.tif')
plt.show()