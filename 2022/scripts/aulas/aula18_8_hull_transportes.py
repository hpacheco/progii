import matplotlib.pyplot as plt
import contextily as ctx
import geopandas as gpd
import pandas as pd

df = pd.read_csv('../../dados/stops.txt')
gdf = gpd.GeoDataFrame(df,geometry=gpd.points_from_xy(df['stop_lon'],df['stop_lat']))

fig,ax = plt.subplots(figsize=(15,15))
gdf.plot(ax=ax,markersize=1,color='red')

hull = gdf.unary_union.convex_hull
hulls = gpd.GeoSeries([hull])
hulls.plot(ax=ax,alpha=0.5)

ctx.add_basemap(ax,zoom=10,crs=4326,source=ctx.providers.OpenStreetMap.HOT)

plt.savefig('paragens.png')