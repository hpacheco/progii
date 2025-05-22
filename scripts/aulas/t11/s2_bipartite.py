import networkx as nx
import matplotlib.pyplot as plt

g = nx.karate_club_graph()

ns = [n for n in g.nodes() if n < 20 ]
nx.draw(g,pos=nx.bipartite_layout(g,ns))
plt.show()