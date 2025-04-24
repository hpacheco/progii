import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

dfs = pd.read_excel("../t06/PT100-tx-tn-prec.xlsx", sheet_name=None)
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
ymonths = ['year'] + months

tmins = dfs['tmin']
tmins.rename(columns={'Dez':'Dec'},inplace=True)
tmins = tmins[ymonths].copy()
tmins.dropna(inplace=True)
tmins['year'] = tmins['year'].astype('uint16')
tmins.set_index('year',inplace=True)

tmaxs = dfs['tmax']
tmaxs = tmaxs[ymonths].copy()
tmaxs.dropna(inplace=True)
tmaxs['year'] = tmaxs['year'].astype('uint16')
tmaxs.set_index('year',inplace=True)

minyear = tmins.index[0]
maxyear = tmins.index[-1]
# cria um gráfico
_,ax = plt.subplots()
# desenha um ano
def draw_year(year):
    ax.fill_between(months,tmins.loc[year],alpha=0.5)
    ax.fill_between(months,tmins.loc[year],tmaxs.loc[year],alpha=0.5)
# desenha o ano mais recente por defeito
draw_year(maxyear)

# cria um novo slider
rect = plt.axes([0.3,0.9,0.5,0.04])
slider = Slider(rect,'Year',minyear,maxyear, valinit=maxyear, valstep=1)
# redesenha o gráfico para o ano atual
def reage(year):
    ax.clear()
    draw_year(year)
    plt.draw()
slider.on_changed(reage)
plt.show()