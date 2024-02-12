import networkx as nx
import matplotlib.pyplot as plt
from s4_go_component import *

mingc = nx.minimum_spanning_tree(gc)

#nx.draw(mingc,node_size=1)
#plt.show()