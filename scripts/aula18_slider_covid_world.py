import matplotlib.pyplot as plt
import matplotlib.dates
from matplotlib.widgets import Slider
import contextily as ctx
import geopandas as gpd
import pandas as pd

gdf3 = gpd.read_file("../dados/countries.geojson")
gdf3 = gdf3.rename(columns={'ADMIN':'Country'})
codes = pd.read_csv("../dados/country-codes.csv",usecols=['ISO3166-1-Alpha-3','ISO3166-1-Alpha-2'])
codes = codes.rename(columns={'ISO3166-1-Alpha-3':'ISO_A3','ISO3166-1-Alpha-2':'ISO_A2'})
gdf32 = pd.merge(gdf3,codes,how='left')
df = pd.read_csv("../dados/WHO-COVID-19-global-data.csv")
df = df.rename(columns={'Country_code':'ISO_A2'})
gdf = pd.merge(gdf32,df,how='inner')


# substituir datas por dias desde o dia 0
gdf['Date_reported'] = pd.to_datetime(gdf['Date_reported'])
gdf['day'] = matplotlib.dates.date2num(gdf['Date_reported'])
minday = gdf['day'].min()
gdf['day'] = gdf['day'] - minday
minday = 0
maxday = gdf['day'].max()

# desenhar mapa com slider
_,ax = plt.subplots(figsize=(30,10))
def draw_day(day):
    gdf[gdf['day'] == day].plot(ax=ax,column='New_deaths',cmap='Reds')
    ax.axis('off')
draw_day(maxday)

rect = plt.axes([0.3,0.9,0.5,0.04])
slider = Slider(rect,'Day',minday,maxday,valinit=maxday,valstep=1)

def reage(day):
    ax.clear()
    draw_day(day)
slider.on_changed(reage)
plt.show()