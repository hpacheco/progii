import networkx as nx
from s1_got_create import *

def mkWeight(d):
    return 1 if d["kinds"] & family_relations else 2

for x,y,d in g.edges(data=True):
    g.edges[x,y]["weight"] = mkWeight(d)

p = nx.shortest_path(g,"Margaery Tyrell","Jon Snow",weight="weight")
print(p)
gp = nx.subgraph(g,p)
print(gp.edges(data=True))

prev = None
path = []
for x in p:
    if prev: path.append((prev,x,gp.edges[prev,x]["kinds"]))
    prev = x
print(path)
