import networkx as nx

g = nx.karate_club_graph()
ag = nx.nx_agraph.to_agraph(g)
ag.write('karate.dot')