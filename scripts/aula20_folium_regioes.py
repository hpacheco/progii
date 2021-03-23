import folium
import json

# centrado no Porto
mapa = folium.Map([41.1579,-8.6291],zoom_start=5,tiles='cartodbpositron')

with open('../dados/portugal.geojson','r') as f: geojson = json.load(f)
folium.GeoJson(geojson).add_to(mapa)
mapa.save("mapa.html")