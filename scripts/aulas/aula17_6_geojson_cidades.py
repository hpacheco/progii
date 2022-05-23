import geopandas as gpd
import pandas as pd

data = pd.read_csv('../../dados/pt.csv')
df = data[['city','population']].copy()
df.fillna(1000,inplace=True)
# cria um ponto por coordenada
gdf = gpd.GeoDataFrame(df,geometry=gpd.points_from_xy(data['lng'],data['lat']))
# escrever para ficheiro
gdf.to_file("cidades.geojson",driver='GeoJSON')