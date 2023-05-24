import folium
import json
import urllib.request

url = 'https://api.ipma.pt/open-data/observation/meteorology/stations/obs-surface.geojson'
urllib.request.urlretrieve(url,'obs-surface.geojson')

# centrado no Porto
mapa = folium.Map([41.1579,-8.6291],zoom_start=6,tiles='stamenterrain')

with open('obs-surface.geojson','r') as f: geojson = json.load(f)
folium.GeoJson(geojson).add_to(mapa)
mapa.save("mapa.html")