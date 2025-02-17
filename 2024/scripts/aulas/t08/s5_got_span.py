import networkx as nx
from s2_got_path import mkWeight
from s4_got_component import *

import matplotlib.pyplot as plt

G = nx.Graph()
for x,y in gc.edges():
    if gc.has_edge(y,x):
        w = min(mkWeight(gc.edges[x,y]),mkWeight(gc.edges[y,x]))
        G.add_edge(x,y,weight=w)

minG = nx.minimum_spanning_tree(G,weight="weight")

nx.draw(minG,node_size=1)
plt.show()