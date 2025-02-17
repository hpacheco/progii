import geopandas as gpd
import urllib.request

#url = 'https://raw.githubusercontent.com/dssg-pt/covid19pt-data/master/extra/mapas/portugal.geojson'
#urllib.request.urlretrieve(url,'portugal.geojson')

# carregar ficheiro geojson com as regiões de Portugal
df_map = gpd.read_file("portugal.geojson")
print(df_map)
print(df_map.crs)

# calcular o centro de cada polígono
df_centros = df_map.copy()
df_centros['geometry'] = df_centros['geometry'].centroid # ignorem o warning
# escrever para ficheiro
df_centros.to_file("centros.geojson",driver='GeoJSON')

# calcular limites
df_lims = df_map.copy()
df_lims['geometry'] = df_lims['geometry'].boundary
# escrever para ficheiro
df_lims.to_file("limites.geojson",driver='GeoJSON')

