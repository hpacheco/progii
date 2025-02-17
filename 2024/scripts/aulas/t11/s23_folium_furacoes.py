import pandas as pd
import urllib.request
import folium
from folium import plugins

#url = 'https://raw.githubusercontent.com/ResidentMario/hurdat2/master/data/atlantic_storms.csv'
#urllib.request.urlretrieve(url,'atlantic_storms.csv')

data = pd.read_csv('atlantic_storms.csv',usecols=['date','name','latitude','longitude','maximum_sustained_wind_knots'])
data['date'] = pd.to_datetime(data['date'])
data['year'] = data['date'].dt.year

# por causa dum bug nas datas do folium: https://github.com/python-visualization/folium/issues/1268
data = data[data['year'] >= 2002]

print(data)
print(data.info())


mapa = folium.Map([35,-55],zoom_start=3,tiles='cartodbpositron')

features = [
    {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [row['longitude'],row['latitude']],
        },
        "properties": {
            "times": [str(row['date'])],
            'style': {'color': 'red'},
            'icon': 'circle',
            'iconstyle': {
                    'fillOpacity': 0.8,
                    'stroke': 'true',
                    'radius': row['maximum_sustained_wind_knots']/5
            }
        },
    }
    for i,row in data.iterrows()
]

plugins.TimestampedGeoJson(
    { "type": "FeatureCollection", "features": features,},
    period="P1D",duration="P5D"
).add_to(mapa)

mapa.save("mapa.html")