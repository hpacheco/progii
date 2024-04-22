import json
import networkx as nx

import urllib.request
#urllib.request.urlretrieve("https://raw.githubusercontent.com/jeffreylancaster/game-of-thrones/master/data/characters.json",'got.json')

with open('got.json','r') as f:
    characters = json.load(f)["characters"]

family_relations = {'parentOf','parents','siblings','sibling','marriedEngaged'}
other_relations = {'killedBy','killed','abductedBy','abducted','allies','guardianOf','serves','servedBy'}
relations = family_relations | other_relations
g = nx.DiGraph()

for character in characters:
    me = character["characterName"]
    g.add_nodes_from([(me,character)])
    for relation in relations:
        if relation in character:
            for other in character[relation]:
                if g.has_edge(me,other): g.edges[me,other]["kinds"].add(relation)
                else: g.add_edge(me,other,kinds={relation})

print(g)