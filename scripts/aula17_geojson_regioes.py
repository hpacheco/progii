import geopandas as gpd

# carregar ficheiro geojson com as regiões de Portugal
df_map = gpd.read_file("../dados/portugal.geojson")
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

