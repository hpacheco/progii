import networkx as nx
import matplotlib.pyplot as plt

g = nx.karate_club_graph()

ns = [[n for n in g.nodes() if n % i == 0] for i in range(1,3)]
nx.draw(g,pos=nx.shell_layout(g,ns))
plt.show()