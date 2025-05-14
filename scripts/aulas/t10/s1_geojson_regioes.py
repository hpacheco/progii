import geopandas as gpd
import urllib.request
import ssl

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

url = 'https://raw.githubusercontent.com/dssg-pt/covid19pt-data/master/extra/mapas/portugal.geojson'
filename = 'portugal.geojson'

#with urllib.request.urlopen(url, context=context) as response, open(filename, 'wb') as out_file:
#    out_file.write(response.read())

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

