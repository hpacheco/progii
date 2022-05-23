import geopandas as gpd

# carregar ficheiro geojson com as regiões de Portugal
df_map = gpd.read_file("../../dados/portugal.geojson")
print(df_map)
print(df_map.crs)



