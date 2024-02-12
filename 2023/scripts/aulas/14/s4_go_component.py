import networkx as nx
import matplotlib.pyplot as plt
from s1_go_create import *

c = nx.connected_components(g)
maxc = max(c,key=len)
gc = g.subgraph(maxc)

#nx.draw(gc,node_size=1)
#plt.show()