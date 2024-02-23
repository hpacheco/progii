
with open('../t03/PZ.annot.txt','r') as f:
    linhas = f.read().splitlines()

pzs = {}
gos = {}
names = {}
for linha in linhas:
    pz,go,name = linha.split('\t')
    pzs[pz] = pzs.get(pz,[]) + [(go,name)]
    gos[go] = gos.get(go,[]) + [(pz,name)]
    names[name] = names.get(name,[]) + [(pz,go)]

# find gene with uniq pzid, goid and name (first version, super slow)
#res = { (pz,go,name) for pz,xs in pzs.items() for go,ys in gos.items() for name,zs in names.items()\
#        if xs==[(go,name)] and ys==[(pz,name)] and zs==[(pz,go)] }
#print(res)

# find gene with uniq pzid, goid and name (second version, much faster)
res = { (pz,go,name) for pz,xs in pzs.items() if len(xs)==1 for go,name in xs \
        if gos[go]==[(pz,name)] and names[name]==[(pz,go)] }
print(res)

