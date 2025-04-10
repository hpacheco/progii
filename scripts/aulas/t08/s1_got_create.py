import json
import networkx as nx
import urllib.request
import ssl

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

url = "https://raw.githubusercontent.com/jeffreylancaster/game-of-thrones/master/data/characters.json"
filename = 'got.json'

#with urllib.request.urlopen(url, context=context) as response, open(filename, 'wb') as out_file:
#    out_file.write(response.read())

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

#print(g)
#print(g.nodes(data=False))
#print(g.edges(data=True))