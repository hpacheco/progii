import networkx as nx
from s1_go_create import *

ranks = nx.pagerank(g)
sranks = sorted(ranks.items(),key=lambda x: x[1])
top5 = sranks[-5:]
for r in top5:
    print(r)
# ('GO:0005829', 0.0061690493264429345)
# ('GO:0005634', 0.007587975063755939)
# ('GO:0005737', 0.007665482985638903)
# ('GO:0005524', 0.008231140227958476)
# ('GO:0005515', 0.00986441224680668)