import networkx as nx
import pygraphviz as pgv

g = nx.karate_club_graph()
nodes = { i : k['club'] for i,k in g.nodes(data=True) }
edges = { (i,j) : k['weight'] for i,j,k in g.edges(data=True) }
# criar um grafo graphviz
ag=pgv.AGraph(splines='ortho')

clubs = { club for n,club in nodes.items() }
# adiciona cada club como um cluster (um sub-grafo especial) do grafo graphviz
gclubs = { club : ag.add_subgraph(name='cluster_'+club,label=club) for club in clubs }

# adiciona nodos a cada cluster
for n,club in nodes.items():
    sg = gclubs[club]
    sg.add_node(n)
    sg.get_node(n).attr['shape'] = 'doublecircle' if club=='Mr. Hi' else 'Msquare'

# adiciona arestas dentro do cluster ou entre clusters
for (i,j),w in edges.items():
    if nodes[i] == nodes[j]:
        gclubs[nodes[i]].add_edge(i,j,penwidth=w,style='dashed')
    else:
        ag.add_edge(i,j,penwidth=w,style='dotted')

ag.layout(prog='dot')
ag.draw('karate.png')