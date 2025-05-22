import networkx as nx
import matplotlib.pyplot as plt

g = nx.karate_club_graph()

for n in g.nodes():
    g.nodes[n]["layer"] = n // 10
nx.draw(g,pos=nx.multipartite_layout(g,subset_key="layer",align="horizontal"))

plt.show()