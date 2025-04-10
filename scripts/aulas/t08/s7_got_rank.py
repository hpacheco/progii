import networkx as nx
from s1_got_create import *

ranks = nx.pagerank(g)
sranks = sorted(ranks.items(),key=lambda x: x[1])
top5 = sranks[-5:]
for r in top5:
    print(r)
# ('Cersei Lannister', 0.012929139680036124)
# ('Eddard Stark', 0.017231486555328624)
# ('Arya Stark', 0.018049491729394615)
# ('Daenerys Targaryen', 0.025910182564731432)
# ('Jon Snow', 0.026336320077632543)