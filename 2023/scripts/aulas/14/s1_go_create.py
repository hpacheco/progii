import networkx as nx

g = nx.Graph()

with open('../../../dados/PZ.annot.txt','r') as f:
    linhas = f.read().splitlines()

pzs = {}; names = {}
for linha in linhas:
    pz,go,name = linha.split('\t')
    pzs[pz] = pzs.get(pz, []) + [go]
    g.add_node(go)
    names[name] = names.get(name, []) + [go]

for pz,gos in pzs.items():
    g.add_edges_from([(go1,go2,{'same':'pz'}) for go1 in gos for go2 in gos if go1!=go2])
for name,gos in names.items():
    g.add_edges_from([(go1,go2,{'same':'name'}) for go1 in gos for go2 in gos if go1!=go2])

