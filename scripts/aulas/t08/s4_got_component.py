import networkx as nx
from s1_got_create import *

import matplotlib.pyplot as plt

c = nx.strongly_connected_components(g)
maxc = max(c,key=len)
print(maxc)
gc = g.subgraph(maxc)

nx.draw(gc,node_size=1)
plt.show()