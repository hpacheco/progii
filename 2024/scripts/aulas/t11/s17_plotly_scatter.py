import pandas as pd
import plotly.express as px

dfs = pd.read_excel("../t06/PT100-tx-tn-prec.xlsx", sheet_name=None)

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
tmins = tmins.melt(id_vars=["year"],var_name="season",value_name="temp")
tmins.set_index('year',inplace=True)
years = tmins.groupby('season').idxmin().rename(columns={'temp':'year'})
temps = tmins.groupby('season').min()
tmins = years.join(temps)
tmins['type'] = 'min'

# colapsar as estações para índices
tmaxs = tmaxs.melt(id_vars=["year"],var_name="season",value_name="temp")
tmaxs.set_index('year',inplace=True)
years = tmaxs.groupby('season').idxmax().rename(columns={'temp':'year'})
temps = tmaxs.groupby('season').max()
tmaxs = years.join(temps)
tmaxs['type'] = 'max'

df = pd.concat([tmins,tmaxs])
df.reset_index(inplace=True)

print(df)

fig = px.scatter(df, x="year", y="temp",color='season',symbol='type')
fig.write_html("ipma.html")

