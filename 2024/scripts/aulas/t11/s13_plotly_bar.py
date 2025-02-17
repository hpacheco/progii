import pandas as pd
import plotly.express as px

x = ['Nuclear', 'Hydro', 'Gas', 'Oil', 'Coal', 'Biofuel']
energy = [5, 6, 15, 22, 24, 8]

df = pd.DataFrame(zip(x,energy),columns=['x','energy'])

fig = px.bar(df, x='x', y='energy')
fig.write_html("energy.html")