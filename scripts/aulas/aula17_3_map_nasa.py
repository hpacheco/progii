import matplotlib.pyplot as plt
import contextily as ctx

# península ibérica
fig,ax = plt.subplots()
ax.set_xlim(-10,0)
ax.set_ylim(35,45)
ax.axis('off')

night = ctx.providers.NASAGIBS.ViirsEarthAtNight2012
ctx.add_basemap(ax,crs=4326,source=night)
plt.show()