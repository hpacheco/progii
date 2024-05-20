import urllib.request
from biopandas.mol2 import PandasMol2
import matplotlib.pyplot as plt
import numpy as np
import regex as re
import pandas as pd
import networkx as nx


def mol2Atoms(filename):
    return PandasMol2().read_mol2(filename).df

def mol2Bonds(filename):
    with open(filename, 'r') as f:
        f_text = f.read()
    bonds =  np.array(re.sub(r'\s+', ' ', re.search(r'@<TRIPOS>BOND([a-z0-9\s]*)@', f_text).group(1)).split()).reshape((-1, 4))
    df_bonds = pd.DataFrame(bonds, columns=['bond_id', 'atom1', 'atom2', 'bond_type'])
    df_bonds[['bond_id','atom1','atom2']] = df_bonds[['bond_id','atom1','atom2']].astype(dtype=int)
    df_bonds.set_index(['bond_id'], inplace=True)
    return df_bonds

#url = 'https://raw.githubusercontent.com/choderalab/openmoltools/master/openmoltools/chemicals/benzene/benzene.mol2'
#urllib.request.urlretrieve(url,'benzene.mol2')

atoms = mol2Atoms('benzene.mol2')
print(atoms)

bonds = mol2Bonds('benzene.mol2')
print(bonds)

g = nx.Graph()
nodes = [ (r['atom_id'],{ c : r[c] for c in atoms.columns if c != 'atom_id' }) for i,r in atoms.iterrows() ]
g.add_nodes_from(nodes)
edges = [ (r['atom1'],r['atom2'],{ 'bond_type' : r['bond_type'] }) for i,r in bonds.iterrows() ]
g.add_edges_from(edges)

xys = { n : (i['x'],i['y']) for n,i in nodes }
names = { n : i['atom_name'][0] for n,i in nodes }

# anel de átomos que formal formam um ciclo
aromatics = [ (i,j) for i,j,k in edges if k['bond_type'] == 'ar' ]

arcycle = nx.find_cycle(g,aromatics[0])
print(arcycle)
def arwidth(i,j):
    e = (i,j) if (i,j) in arcycle else (j,i)
    idx = arcycle.index(e)
    return 3 if (idx % 2) == 0 else 1
ws = [ arwidth(i,j) if k['bond_type']=='ar' else int(k['bond_type']) for i,j,k in edges ]

print(nodes)
colors = [ 'grey' if d['atom_name'][0]=='H' else 'black' for i,d in nodes ]

nx.draw_networkx(g,pos=xys,with_labels=False,node_color=colors)

for i,d in nodes:
    x = d['x']; y = d['y']
    lcolor = 'black' if d['atom_name'][0]=='H' else 'white'
    plt.text(x, y, d['atom_name'][0],va='center',ha='center',color=lcolor)

nx.draw_networkx_edges(g,pos=xys,width=ws)
plt.show()