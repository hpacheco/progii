import folium
import pandas as pd
import geopandas as gpd

mapa = folium.Map([41.1579,-8.6291],zoom_start=8,tiles='stamenterrain')

gdf = gpd.read_file('../dados/obs-surface.geojson')
gdf['time'] = pd.to_datetime(gdf['time'])

latest_time = gdf['time'].max()
gdf = gdf[gdf['time'] == latest_time]

for i,row in gdf.iterrows():
     if row['temperatura'] >= 20: co='red';
     elif row['temperatura'] >= 10: co='orange';
     elif row['temperatura'] >= 0: co='blue'
     else: co='other';
     icn = folium.Icon(color=co, icon='glyphicon-cloud')
     folium.Marker(location=(row['geometry'].y,row['geometry'].x) \
                  ,icon=icn \
                  ,tooltip=row['localEstacao'] \
                  ,popup=str(row)
                  ).add_to(mapa)
mapa.save("mapa.html")