import networkx as nx
import matplotlib.pyplot as plt

g = nx.karate_club_graph()

plt.figure(figsize=(9,6))

plt.subplot(2,3,1)
plt.title('neato (default)')
nx.draw(g,node_size=30,pos=nx.nx_agraph.pygraphviz_layout(g,prog='neato'))

plt.subplot(2,3,2)
plt.title('dot')
nx.draw(g,node_size=30,pos=nx.nx_agraph.pygraphviz_layout(g,prog='dot'))

plt.subplot(2,3,3)
plt.title('fdp')
nx.draw(g,node_size=30,pos=nx.nx_agraph.pygraphviz_layout(g,prog='fdp'))

plt.subplot(2,3,4)
plt.title('circo')
nx.draw(g,node_size=30,pos=nx.nx_agraph.pygraphviz_layout(g,prog='circo'))

plt.subplot(2,3,5)
plt.title('twopi')
nx.draw(g,node_size=30,pos=nx.nx_agraph.pygraphviz_layout(g,prog='twopi',root=0))

plt.subplot(2,3,6)
plt.title('osage')
nx.draw(g,node_size=30,pos=nx.nx_agraph.pygraphviz_layout(g,prog='osage'))

plt.show()