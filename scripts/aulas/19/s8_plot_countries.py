import geopandas as gpd
import matplotlib.pyplot as plt
import urllib.request

url = 'https://datahub.io/core/geo-countries/r/countries.geojson'
urllib.request.urlretrieve(url,'countries.geojson')

gdf = gpd.read_file("countries.geojson")

ax = gdf.plot(cmap='viridis')
ax.axis('off')
plt.show()