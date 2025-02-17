
import networkx as nx
from s1_got_create import *
import matplotlib.pyplot as plt

# 1. Sub-grafo de relações de parentalidade

for n1,n2,d in list(g.edges(data=True)):
    if "parentOf" not in d["kinds"]: g.remove_edge(n1,n2)
for n,d in list(g.degree()):
    if d == 0: g.remove_node(n)

# 2. Maior componente (fracamente) conexo

c = nx.weakly_connected_components(g)
maxc = max(c,key=len)
gc = g.subgraph(maxc)
print(gc)
print(nx.is_directed_acyclic_graph(gc))

# 3. Raízes (grau de entrada = 0)

roots = { x for x,d in gc.in_degree() if d == 0 }
print(roots)

# 4. Para cada raiz, árvore desde a raiz

Ts = { nx.algorithms.traversal.breadth_first_search.bfs_tree(gc,source=root) for root in roots }

# 5. Encontrar a maior árvore

T = max(Ts,key=lambda x:len(x.nodes()))

# Desenhar

plt.figure(figsize=(10,7))
pos = nx.nx_agraph.pygraphviz_layout(T, prog="dot")
nx.draw_networkx(T,pos,node_size=0)
plt.show()
