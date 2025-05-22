import json
import folium
import urllib.request
import ssl

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

url = 'https://raw.githubusercontent.com/dssg-pt/covid19pt-data/master/extra/mapas/portugal.geojson'
filename = 'portugal.geojson'

#with urllib.request.urlopen(url, context=context) as response, open(filename, 'wb') as out_file:
#    out_file.write(response.read())

# como criar um ficheiro HTML que visualiza um ficheiro geojson similarmente ao que faz o geojson.io
mapa = folium.Map()
with open('portugal.geojson','r') as f: geojson = json.load(f)
folium.GeoJson(geojson).add_to(mapa)
mapa.save("portugal.html")