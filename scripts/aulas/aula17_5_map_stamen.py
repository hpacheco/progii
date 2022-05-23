import matplotlib.pyplot as plt
import contextily as ctx

# Porto alargado
fig,ax = plt.subplots(figsize=(15,15))
ax.set_xlim(-8.9,-7.9)
ax.set_ylim(40.7,41.7)
ax.axis('off')

# múltiplos mapas
colors = ctx.providers.Stamen.Watercolor
labels = ctx.providers.Stamen.TonerLabels
ctx.add_basemap(ax,crs=4326,source=colors)
ctx.add_basemap(ax,crs=4326,source=labels)

plt.show()