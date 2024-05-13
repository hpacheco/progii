import json
import folium
import urllib.request

#url = 'https://raw.githubusercontent.com/dssg-pt/covid19pt-data/master/extra/mapas/portugal.geojson'
#urllib.request.urlretrieve(url,'portugal.geojson')

# como criar um ficheiro HTML que visualiza um ficheiro geojson similarmente ao que faz o geojson.io
mapa = folium.Map()
with open('portugal.geojson','r') as f: geojson = json.load(f)
folium.GeoJson(geojson).add_to(mapa)
mapa.save("portugal.html")