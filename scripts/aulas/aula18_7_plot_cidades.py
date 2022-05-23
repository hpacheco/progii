import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import contextily as ctx

# copiado do exemplo anterior aula18_6_geojson_cidades.py
data = pd.read_csv('../../dados/pt.csv')
df = data[['city','population']].copy()
df.fillna(1000,inplace=True)

gdf = gpd.GeoDataFrame(df,geometry=gpd.points_from_xy(data['lng'],data['lat']))

# desenha um plot com tamanho dos marcadores proporcional à população
fig,ax = plt.subplots(figsize=(10,10))
gdf.plot(ax=ax,markersize=df['population']/1000)

# acrescenta mapa
ctx.add_basemap(ax,zoom=6,crs=4326,source=ctx.providers.CartoDB.Voyager)
plt.show()