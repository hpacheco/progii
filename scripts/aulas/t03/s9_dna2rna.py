bases =  {'A':'U', 'T':'A', 'C':'G', 'G':'C'}
def base2rna(b): return bases.get(b)
def dna2rna(dna):
    return ''.join(map(base2rna,dna))

print(dna2rna('ATCG'))
# UAGC