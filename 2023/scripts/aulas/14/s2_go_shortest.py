import networkx as nx
from s1_go_create import *

p = nx.shortest_path(g,'GO:0003824','GO:0004449')
print(p)
# ['GO:0003824', 'GO:0055114', 'GO:0004449']
gp = nx.subgraph(g,p)
print(gp.nodes())
# ['GO:0004449', 'GO:0055114', 'GO:0003824']
print(gp.edges(data=True))
# [('GO:0004449', 'GO:0055114', {'same': 'name'}), ('GO:0055114', 'GO:0003824', {'same': 'name'})]