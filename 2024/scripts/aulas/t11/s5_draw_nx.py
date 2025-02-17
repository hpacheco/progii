import networkx as nx
import matplotlib.pyplot as plt

g = nx.karate_club_graph()

nx.draw_networkx(g,node_shape='s',style="--")
plt.show()