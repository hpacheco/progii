import folium

# sequencia de lat,lon
mapa = folium.Map([41.1579,-8.6291],zoom_start=5,tiles='cartodbpositron')
mapa.save("mapa.html")