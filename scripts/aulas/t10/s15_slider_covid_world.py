import matplotlib.pyplot as plt
import matplotlib.dates
from matplotlib.widgets import Slider
import contextily as ctx
import geopandas as gpd
import pandas as pd

gdf3 = gpd.read_file("countries.geojson")
gdf3 = gdf3.rename(columns={'ADMIN':'Country'})
codes = pd.read_csv("country-codes.csv",usecols=['ISO3166-1-Alpha-3','ISO3166-1-Alpha-2'])
codes = codes.rename(columns={'ISO3166-1-Alpha-3':'ISO_A3','ISO3166-1-Alpha-2':'ISO_A2'})
gdf32 = pd.merge(gdf3,codes,how='left')
df = pd.read_csv("WHO-COVID-19-global-data.csv")
df = df.rename(columns={'Country_code':'ISO_A2'})
gdf = pd.merge(gdf32,df,how='inner')


# substituir datas por dias desde o dia 0
gdf['Date_reported'] = pd.to_datetime(gdf['Date_reported'])
gdf['day'] = matplotlib.dates.date2num(gdf['Date_reported'])
minday = gdf['day'].min()
gdf['day'] = gdf['day'] - minday
days = sorted(set(gdf['day']))

minx, miny, maxx, maxy = gdf.total_bounds

# desenhar mapa com slider
_,ax = plt.subplots(figsize=(30,10))
def draw_day(i):
    gdayf = gdf[gdf['day'] == days[i]]
    print(gdayf)
    gdayf.plot(ax=ax,column='New_deaths',cmap='Reds')
    ax.axis('off')
    ax.set_xlim(minx, maxx)
    ax.set_ylim(miny, maxy)
draw_day(len(days)-1)

rect = plt.axes([0.3,0.9,0.5,0.04])
slider = Slider(rect,'Day',0,len(days)-1,valinit=len(days)-1,valstep=1)

def reage(i):
    ax.clear()
    draw_day(i)
slider.on_changed(reage)
plt.show()