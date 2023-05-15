import geopandas as gpd
import pandas as pd
import urllib.request

url = 'https://simplemaps.com/static/data/country-cities/pt/pt.csv'
urllib.request.urlretrieve(url,'pt.csv')

data = pd.read_csv('pt.csv')
df = data[['city','population']].copy()
df.fillna(1000,inplace=True)
# cria um ponto por coordenada
gdf = gpd.GeoDataFrame(df,geometry=gpd.points_from_xy(data['lng'],data['lat']))
# escrever para ficheiro
gdf.to_file("cidades.geojson",driver='GeoJSON')