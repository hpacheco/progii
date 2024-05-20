import pandas as pd
import plotly.express as px

men_means = (20, 35, 30, 35, 27)
women_means = (25, 32, 34, 20, 25)
men = pd.DataFrame(men_means,columns=['age'])
men['sex'] = 'man'
women = pd.DataFrame(women_means,columns=['age'])
women['sex'] = 'woman'
df = pd.concat([men,women]) # junta linhas dos DataFrames
df.reset_index(inplace=True,names='country')

fig = px.bar(df, x='country', y='age',color='sex')
fig.write_html("demography.html")
