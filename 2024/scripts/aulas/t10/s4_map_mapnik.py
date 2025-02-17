import matplotlib.pyplot as plt
import contextily as ctx

# Porto
fig,ax = plt.subplots(figsize=(15,15))
ax.set_xlim(-8.8,-8.3)
ax.set_ylim(41,41.5)
ax.axis('off')

mapnik = ctx.providers.OpenStreetMap.Mapnik
ctx.add_basemap(ax,crs=4326,source=mapnik)

plt.show()