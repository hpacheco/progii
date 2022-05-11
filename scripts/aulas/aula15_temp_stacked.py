import pandas as pd
import matplotlib.pyplot as plt

dfs = pd.read_excel("../../dados/PT100-tx-tn-prec.xlsx", sheet_name=None)
years = ['year','Annual']

tmins = dfs['tmin']
tmins = tmins[years].copy()
tmins.dropna(inplace=True)

tmaxs = dfs['tmax']
tmaxs = tmaxs[years].copy()
tmaxs.dropna(inplace=True)

temps = pd.merge(tmins,tmaxs,on='year',suffixes=('_tmin','_tmax'))
temps['year'] = temps['year'].astype('uint16')
temps.set_index('year',inplace=True)
temps['Annual_tmax'] = temps['Annual_tmax'] - temps['Annual_tmin']
temps.plot(kind='area',alpha=0.3,stacked=True,legend=False,ylabel='Temp (ºC)')

#plt.show()
plt.savefig('plot.png')