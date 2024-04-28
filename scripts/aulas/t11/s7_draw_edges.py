import networkx as nx
import matplotlib.pyplot as plt

g = nx.karate_club_graph()
es = g.edges(data=True)
ws = [ (i+j)/40 for i,j,d in es ]
cs = [ i for i in range(len(es)) ]
ls = { (i,j) : d['weight'] for i,j,d in es }
ps = nx.spiral_layout(g)
nx.draw_networkx(g,pos=ps,width=ws,edge_color=cs)
nx.draw_networkx_edge_labels(g,pos=ps,edge_labels=ls,font_color='red')
plt.show()