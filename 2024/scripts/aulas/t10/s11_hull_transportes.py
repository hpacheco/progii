import matplotlib.pyplot as plt
import contextily as ctx
import geopandas as gpd
import pandas as pd
import urllib.request
import zipfile

#url = 'https://dados.gov.pt/en/datasets/r/7f2ee8cf-63d8-4b74-b1c2-f4b016963611'
#urllib.request.urlretrieve(url,'stops-porto.zip')
with zipfile.ZipFile('stops-porto.zip', 'r') as r: r.extractall(".")

df = pd.read_csv('stops.txt')
gdf = gpd.GeoDataFrame(df,geometry=gpd.points_from_xy(df['stop_lon'],df['stop_lat']))

fig,ax = plt.subplots(figsize=(15,15))
gdf.plot(ax=ax,markersize=1,color='red')

hull = gdf.unary_union.convex_hull
print(hull)
hulls = gpd.GeoSeries([hull])
hulls.plot(ax=ax,alpha=0.5)

ctx.add_basemap(ax,zoom=10,crs=4326,source=ctx.providers.OpenStreetMap.HOT)

plt.savefig('paragens.png')