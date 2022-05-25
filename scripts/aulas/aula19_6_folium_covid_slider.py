import folium
import folium.plugins
import pandas as pd
import geopandas as gpd
import json

codes = pd.read_csv("../../dados/country-codes.csv",usecols=['ISO3166-1-Alpha-3','ISO3166-1-Alpha-2'])
codes = codes.rename(columns={'ISO3166-1-Alpha-3':'ISO_A3','ISO3166-1-Alpha-2':'ISO_A2'})
df = pd.read_csv("../../dados/WHO-COVID-19-global-data.csv")
df = df.rename(columns={'Country_code':'ISO_A2'})
gdf = pd.merge(codes,df,how='inner')
gdf['Date_reported'] = pd.to_datetime(gdf['Date_reported'])
# data em milésimos de segundo
gdf['Date']=(gdf['Date_reported'].astype(int)// 10**9).astype('U10')
# máximo de mortes diário
gdaily = gdf.groupby(by='Date')[['New_deaths']].max()
gdaily.rename(columns={'New_deaths':'max_deaths'},inplace=True)

# the dictionary for each id shall have the following format
# { data ↦ { ‘color’ ↦ hex, ’opacity’ ↦ [0..1] }
def sort_df(df):
    df = df.set_index('Date')[['New_deaths']]
    df = pd.merge(df,gdaily,on='Date')
    #color from 0 t0 255
    df['color'] = df['New_deaths'] * 255 / df['max_deaths']
    df.fillna(0,inplace=True)
    del df['New_deaths']
    del df['max_deaths']
    df['color'] = df['color'].apply(lambda r : '#%02x%02x%02x' % (round(r),0,0))
    df['opacity'] = 0.5
    return df.to_dict(orient='index')

# the data dictionary shall have the following format
# { id ↦ { data ↦ { ‘color’ ↦ hex, ’opacity’ ↦ [0..1] } }
geodict = { iso3 : sort_df(df) for iso3,df in gdf.groupby(by='ISO_A3') }

mapa = folium.Map([0,0],zoom_start=2)

geodf = gpd.read_file('../../dados/countries.geojson')
geodf.set_index('ISO_A3',inplace=True)
print(geodf)
del geodf['ADMIN']
geojson = geodf.to_json()

# write the geojson data to a file in order to check that each feature has the necessary id field
with open('mapa.json', 'w') as outfile:
    json.dump(geojson, outfile)

folium.plugins.TimeSliderChoropleth(geojson,styledict=geodict).add_to(mapa)
mapa.save("mapa.html")