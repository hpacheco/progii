import networkx as nx
import pandas as pd
import plotly.express as px
import math

g = nx.karate_club_graph()
ns = dict(g.nodes(data=True))
es = g.edges(data=True)
ps = nx.spiral_layout(g)

df = pd.DataFrame(columns=['node','x','y','club','size'])

def add_node(i):
    x,y = ps[i]
    club = ns[i]['club']
    return [i,x,y,club,20]

idx = 0
for i,j,d in es:
    df.loc[idx] = add_node(i)
    df.loc[idx+1] = add_node(j)
    df.loc[idx+2] = math.nan
    idx = idx+3

print(df)

fig = (px.scatter(df, x="x", y="y",color='club',text='node',size='size').update_traces(mode='lines+markers+text',line_color="#6A6F00"))
fig.write_html("test.html")