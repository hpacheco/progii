import networkx as nx
import matplotlib.pyplot as plt

g = nx.karate_club_graph()
l = nx.nx_agraph.pygraphviz_layout(g)
nx.draw(g,pos=l)
plt.show()