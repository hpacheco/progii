import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# paises com códigos 3-dígitos
gdf3 = gpd.read_file("../../dados/countries.geojson")
#gdf3 = gdf3.rename(columns={'ADMIN':'Country'})
#print(gdf3)

# conversão códigos
codes = pd.read_csv("../../dados/country-codes.csv",usecols=['ISO3166-1-Alpha-3','ISO3166-1-Alpha-2'])
codes = codes.rename(columns={'ISO3166-1-Alpha-3':'ISO_A3','ISO3166-1-Alpha-2':'ISO_A2'})
#print(codes)

# países com códigos 2- e 3-dígitos
gdf32 = pd.merge(gdf3,codes,how='left')
#print(gdf32)

# dados covid-19 WHO, apenas precisamos dos dados mais recentes para cada país
df = pd.read_csv("../../dados/WHO-COVID-19-global-data.csv")
df = df.groupby(by='Country').tail(1)

df = df.rename(columns={'Country_code':'ISO_A2','Cumulative_deaths':'Deaths'})
df = df[['ISO_A2','Deaths']]
gdf = pd.merge(gdf32,df,how='inner')

ax = gdf.plot(cmap='Reds',column='Deaths')
ax.axis('off')
plt.show()