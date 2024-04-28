import matplotlib.colors as pltcolors
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons
from matplotlib.widgets import Button
import contextily as ctx
import pandas as pd
import urllib.request
import zipfile
import numpy as np

#url = 'https://opendata.porto.digital/dataset/5275c986-592c-43f5-8f87-aabbd4e4f3a4/resource/f6b85210-3b86-4617-8327-405f50791cf0/download/gtfs-stcp-2023-09.zip'
#urllib.request.urlretrieve(url,'stops-stcp.zip')
with zipfile.ZipFile('stops-stcp.zip', 'r') as r: r.extractall("stops-stcp")

stop_times = pd.read_csv("stops-stcp/stop_times.txt")
stops = pd.read_csv("stops-stcp/stops.txt")
stops = stops[["stop_id","stop_lat","stop_lon"]]
trips = pd.read_csv("stops-stcp/trips.txt")
trips = trips[["route_id","trip_id"]]

df = pd.merge(stop_times,stops,how="left")
df = pd.merge(df,trips,how="left")

routes = sorted(set(df["route_id"]))

fig,ax = plt.subplots(figsize=(10,8))
ax.axis('off')

colors = pltcolors.ListedColormap(plt.get_cmap("nipy_spectral")(np.linspace(0,1,len(routes)))).colors
routecolors = {}
for i,route in enumerate(routes):
    routecolors[route] = colors[i]

buttons = CheckButtons(plt.axes([0.9, 0, 0.1, 1]),routes,[True]*len(routes),check_props={'color': colors},label_props={'color':colors})
checkall = Button(plt.axes([0.2, 0.9, 0.2, 0.05]),"Check All")
uncheckall = Button(plt.axes([0.5, 0.9, 0.2, 0.05]),"Uncheck All")

lns = {}
for trip_id,trip in df.groupby(by="trip_id"):
    #print(trip_id,trip)
    trip_lons = trip["stop_lon"]
    trip_lats = trip["stop_lat"]
    route = trip["route_id"].iloc[0]
    ln, = ax.plot(trip_lons,trip_lats,color=routecolors[route])
    lns[route] = lns.get(route,[]) + [ln]

visibles = { route : True for route in routes }

def redrawRoute(route):
    b = visibles[route]
    for ln in lns[route]:
        ln.set_visible(b)

def reage(route):
    visibles[route] = not visibles[route]
    redrawRoute(route)
    plt.draw()
buttons.on_clicked(reage)
def reageCheck(b):
    global visibles
    visibles = { route : b for route in routes }
    for route in routes:
        redrawRoute(route)
    for i in range(len(routes)):
        buttons.eventson = False
        status = buttons.get_status()
        for i,stat in enumerate(status):
            if ((b and not stat) or (not b and stat)):
                buttons.set_active(i)
        buttons.eventson = True
    plt.draw()
checkall.on_clicked(lambda info:reageCheck(True))
uncheckall.on_clicked(lambda info:reageCheck(False))

ctx.add_basemap(ax,zoom=12,crs=4326,source=ctx.providers.CartoDB.Positron)

plt.show()
