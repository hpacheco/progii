import matplotlib.pyplot as plt
import contextily as ctx

# Porto alargado
fig,ax = plt.subplots(figsize=(10,10))
ax.set_xlim(-8.9,-7.9)
ax.set_ylim(40.7,41.7)
ax.axis('off')

# múltiplos mapas
colors = ctx.providers.CartoDB.VoyagerNoLabels
labels = ctx.providers.CartoDB.PositronOnlyLabels
ctx.add_basemap(ax,crs=4326,source=colors)
ctx.add_basemap(ax,crs=4326,source=labels)

plt.show()