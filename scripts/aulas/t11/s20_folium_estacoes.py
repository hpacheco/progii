import folium
import json
import urllib.request
import ssl

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

url = 'https://api.ipma.pt/open-data/observation/meteorology/stations/obs-surface.geojson'
filename = 'obs-surface.geojson'

with urllib.request.urlopen(url, context=context) as response, open(filename, 'wb') as out_file:
    out_file.write(response.read())

# centrado no Porto
mapa = folium.Map([41.1579,-8.6291],zoom_start=6,tiles='OpenStreetMap')

with open('obs-surface.geojson','r') as f: geojson = json.load(f)
folium.GeoJson(geojson).add_to(mapa)
mapa.save("mapa.html")