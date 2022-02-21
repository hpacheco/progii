import folium
import fiona
import geopandas as gpd

gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'

# 7 Lagoas
trilho1 = gpd.read_file('../dados/Trilho-das-7-Lagoas.kml', driver='KML')
xertelo = trilho1['geometry'][0]
lagoasX = float('inf'); lagoasY = float('inf')
for x,y,z in trilho1['geometry'][2].coords:
    if x < lagoasX: lagoasX=x; lagoasY=y
coords1 = [ (y,x) for x,y,z in trilho1['geometry'][2].coords ]

# Fisgas de Ermelo
trilho2 = gpd.read_file('../dados/Fisgas-de-Ermelo.kml', driver='KML')
ermelo = trilho2['geometry'][2]
fisgasX = float('-inf');
fisgasY = float('-inf')
for x, y, z in trilho2['geometry'][0].coords:
    if x > fisgasX: fisgasX = x; fisgasY = y
coords2 = [ (y,x) for x,y,z in trilho2['geometry'][0].coords ]

# ponto médio
y = (xertelo.y + ermelo.y) / 2
x = (xertelo.x + ermelo.x) / 2

# criar mapa

mapa = folium.Map([y,x],zoom_start=10)

folium.Marker(location=(xertelo.y,xertelo.x),icon=folium.Icon(color='green'),tooltip='Xertelo',popup='Aldeia do Xertelo').add_to(mapa)
folium.Marker(location=(lagoasY,lagoasX),icon=folium.Icon(color='green'),tooltip='7 Lagoas',popup='Cascatas das 7 Lagoas').add_to(mapa)
folium.Marker(location=(ermelo.y,ermelo.x),icon=folium.Icon(color='blue'),tooltip='Ermelo',popup='Aldeia do Ermelo').add_to(mapa)
folium.Marker(location=(fisgasY,fisgasX),icon=folium.Icon(color='blue'),tooltip='Fisgas de Ermelo',popup='Cascatas das Fisgas de Ermelo').add_to(mapa)

folium.vector_layers.PolyLine(coords1,popup='Xertelo <-> 7 Lagoas',tooltip='Trilho das 7 Lagoas',color='green',weight=5).add_to(mapa)
folium.vector_layers.PolyLine(coords2,popup='Ermelo <-> Fisgas',tooltip='Trilho das Fisgas de Ermelo',color='blue',weight=5).add_to(mapa)

mapa.save("mapa.html")