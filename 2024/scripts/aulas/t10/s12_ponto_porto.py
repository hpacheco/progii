import matplotlib.pyplot as plt
import contextily as ctx
import geopandas as gpd
import pandas as pd

# Porto
fig,ax = plt.subplots()
ax.set_xlim(-8.8,-8.3)
ax.set_ylim(41,41.5)
ax.axis('off')

#cidade Porto
y = 41.1647; x = -8.6308

topo = ctx.providers.CartoDB.PositronNoLabels
ctx.add_basemap(ax,crs=4326,source=topo)

ax.plot(x,y,'ok',markersize=5)
ax.text(x,y,' Porto',fontsize=12);

plt.show()