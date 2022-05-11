import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors

dfs = pd.read_excel("../../dados/PT100-tx-tn-prec.xlsx", sheet_name=None)

season_color = {'Spring':'green','Summer':'goldenrod','Autumn':'darkred','Winter':'blue'}

seasons = ['Spring','Summer','Autumn','Winter']
yseasons = ['year'] + seasons

# temperaturas mínimas para cada ano e estação
tmins = dfs['tmin']
tmins = tmins[yseasons].copy()
tmins.dropna(inplace=True)
tmins['year'] = tmins['year'].astype('uint16')

# temperaturas máximas para cada ano e estação
tmaxs = dfs['tmax']
tmaxs = tmaxs[yseasons].copy()
tmaxs.dropna(inplace=True)
tmaxs['year'] = tmaxs['year'].astype('uint16')

# colapsar as estações para índices
tmins = tmins.melt(id_vars=["year"],var_name="season",value_name="tmin")
tmins.set_index('year',inplace=True)
years = tmins.groupby('season').idxmin().rename(columns={'tmin':'year'})
temps = tmins.groupby('season').min()
print(years,temps)
tmins = years.join(temps)

# colapsar as estações para índices
tmaxs = tmaxs.melt(id_vars=["year"],var_name="season",value_name="tmax")
tmaxs.set_index('year',inplace=True)
years = tmaxs.groupby('season').idxmax().rename(columns={'tmax':'year'})
temps = tmaxs.groupby('season').max()
tmaxs = years.join(temps)

for season in seasons:
    plt.scatter(tmins['year'][season],tmins['tmin'][season],c=season_color[season],s=200,marker="v")
    plt.scatter(tmaxs['year'][season],tmaxs['tmax'][season], c=season_color[season], s=200, marker="^")
    plt.scatter([],[],c=season_color[season],s=100,marker='s',label=season)
plt.legend()
plt.show()