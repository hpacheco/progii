import folium
import pandas as pd
import geopandas as gpd
import json


codes = pd.read_csv("../t10/country-codes.csv",usecols=['ISO3166-1-Alpha-3','ISO3166-1-Alpha-2'])
codes = codes.rename(columns={'ISO3166-1-Alpha-3':'ISO_A3','ISO3166-1-Alpha-2':'ISO_A2'})
df = pd.read_csv("../t10/WHO-COVID-19-global-data.csv")
df = df.groupby(by='Country').tail(1)
df = df.rename(columns={'Country_code':'ISO_A2','Cumulative_deaths':'Deaths'})
df = df[['ISO_A2','Deaths']]
gdf = pd.merge(codes,df,how='inner')

print(gdf)

with open('../t10/countries.geojson','r') as f: geojson = json.load(f)

mapa = folium.Map([41.1579,-8.6291],zoom_start=3)

folium.Choropleth(
    geo_data=geojson,
    data=gdf,
    columns=["ISO_A3","Deaths"],
    key_on="feature.properties.ISO_A3",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Accumulated Deaths (%)",
).add_to(mapa)

mapa.save("mapa.html")