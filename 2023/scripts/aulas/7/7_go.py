
with open('../../../dados/PZ.annot.txt','r') as f:
    linhas = f.read().splitlines()

genes = {}
for linha in linhas:
    id,go,name = linha.split('\t')
    genes[name] = genes.get(name,set()) | {id,go}

# gene com mais identificadores
maxg = max(genes,key=lambda g: len(genes[g]))
print(maxg,genes[maxg])