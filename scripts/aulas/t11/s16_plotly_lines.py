import pandas as pd
import plotly.express as px

vacinas = pd.read_csv('../t08/vacinas.csv')
vacinas = vacinas[[col for col in vacinas.columns if col=='data' or col.startswith('doses')]]
vacinas = vacinas.dropna()

print(vacinas)

df = vacinas.melt(id_vars=['data'],var_name='tipo',value_name='num')

print(df)

fig = px.line(df, x="data", y="num",color='tipo')
fig.write_html("vacinas.html")