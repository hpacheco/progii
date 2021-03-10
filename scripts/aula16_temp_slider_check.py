import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, CheckButtons

# Temperatura

dfs = pd.read_excel("../dados/PT100-tx-tn-prec.xlsx", sheet_name=None)
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

# cria um novo slider
rect = plt.axes([0.3,0.9,0.5,0.04])
slider = Slider(rect,'Year',minyear,maxyear, valinit=maxyear, valstep=1)

#carrega dados precipitação
precs = dfs['prec']
precs = precs[ymonths].copy()
precs.dropna(inplace=True)
precs['year'] = precs['year'].astype('uint16')
precs.set_index('year',inplace=True)

# cria dois eixos nos Y
ax.set_yticks([])
# renomear ax no exemplo anterior para ax1
ax1 = ax.twinx()
ax2 = ax1.twinx()

# desenha um ano
def draw_year(year):
    ax1.fill_between(months,tmins.loc[year],alpha=0.5)
    ax1.fill_between(months,tmins.loc[year],tmaxs.loc[year],alpha=0.5)
# desenha o ano mais recente por defeito
draw_year(maxyear)

# desenha precipitação
lprec, = ax2.plot(months,precs.loc[maxyear],color='green')
# redesenha precipitação
def redraw_prec(year):
    lprec.set_ydata(precs.loc[year])
    ax2.set_ylim(0,precs.loc[year].max()+10)

# redesenha o gráfico para o ano atual e atualiza também precipitação
def reage(year):
    ax1.clear()
    draw_year(year)
    redraw_prec(year)
    plt.draw()
slider.on_changed(reage)

# um botão de seleção
rect = plt.axes([0.15,0.77,0.1,0.08])
button = CheckButtons(rect,('Temp','Prec'),(True,True))
def altera(label):
    if label=='Temp': ax1.set_visible(not ax1.get_visible())
    elif label=='Prec': ax2.set_visible(not ax2.get_visible())
    plt.draw()
button.on_clicked(altera)

plt.show()