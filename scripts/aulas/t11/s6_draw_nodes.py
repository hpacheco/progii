import networkx as nx
import matplotlib.pyplot as plt

g = nx.karate_club_graph()
ns = g.nodes(data=True)
color = {'Mr. Hi':'red','Officer':'blue'}
his = [n for n,i in ns if i['club']=='Mr. Hi']
colors = [ color[i['club']] for n,i in ns ]
ls = { n : chr(n+65) for n,i in ns }

szs = [10 * n for n in g.nodes()]
nx.draw_networkx(g,pos=nx.bipartite_layout(g,his),labels=ls,node_size=szs,node_color=colors,font_color='yellow')
plt.show()