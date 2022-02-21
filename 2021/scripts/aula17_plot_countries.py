import geopandas as gpd
import matplotlib.pyplot as plt

gdf = gpd.read_file("../dados/countries.geojson")

ax = gdf.plot(cmap='viridis')
ax.axis('off')
plt.show()