import matplotlib.pyplot as plt
import contextily as ctx
import geopandas as gpd
import pandas as pd


data = pd.read_csv('pt.csv')
data.fillna(1000,inplace=True)

lons = data['lng']
lats = data['lat']
pops = data['population'] / 1000
maxpop = data['population'].max()

fig,ax = plt.subplots(figsize=(30,15))
for i,row in data.iterrows():
    ax.text(row['lng'],row['lat'],row['city'],fontsize=row['population']*12/maxpop)
    #ax.scatter(lons[i],lats[i],s=pops[i],c=pops[i],cmap='Reds', alpha=0.5)
circles = ax.scatter(lons,lats,s=pops,c=pops,cmap='Reds', alpha=0.5)
plt.colorbar(circles,label='population')
ctx.add_basemap(ax,crs=4326,source=ctx.providers.OpenStreetMap.Mapnik)

plt.savefig('cidades.png')