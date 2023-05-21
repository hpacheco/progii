import networkx as nx
import matplotlib.pyplot as plt

g = nx.karate_club_graph()

plt.figure(figsize=(9,6))

plt.subplot(2,3,1)
plt.title('random_layout')
nx.draw(g,pos=nx.random_layout(g))

plt.subplot(2,3,2)
plt.title('circular_layout')
nx.draw(g,pos=nx.circular_layout(g))

plt.subplot(2,3,3)
plt.title('spectral_layout')
nx.draw(g,pos=nx.spectral_layout(g))

plt.subplot(2,3,4)
plt.title('kamada_kawai_layout')
nx.draw(g,pos=nx.kamada_kawai_layout(g))

plt.subplot(2,3,5)
plt.title('spring_layout')
nx.draw(g,pos=nx.spring_layout(g))

plt.subplot(2,3,6)
plt.title('spiral_layout')
nx.draw(g,pos=nx.spiral_layout(g))

plt.show()