import matplotlib.pyplot as plt
import contextily as ctx
import geopandas as gpd

# carregar ficheiro geojson com as regiões de Portugal
df_map = gpd.read_file("../../dados/portugal.geojson")
#print(df_map)
print(df_map.crs)

# desenha as regioes
ax = df_map.plot()

# experimentem comentar/descomentar este bloco
# altera os limites (tem que ser antes de desenhar o mapa)
minx, miny, maxx, maxy = df_map.total_bounds
ax.set_xlim(minx,0)
ax.set_ylim(miny,maxy*2)

# experimentem comentar/descomentar este bloco
# acrescenta o mapa
ctx.add_basemap(ax,zoom=5,crs=df_map.crs)

plt.show()