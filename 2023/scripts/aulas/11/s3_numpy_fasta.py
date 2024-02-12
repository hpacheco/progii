from Bio import AlignIO
import numpy as np

alignments = AlignIO.read(open("../../../dados/apoex.afa"), "fasta")
d = { a.id : np.array(a) for a in alignments }

a1 = d['APE_BOVIN']
a2 = d['APE_MOUSE']

alphas = np.vectorize(lambda c: c>='A' and c<='Z')
mask = alphas(a1) & alphas(a2) & (a1==a2)
score = sum(mask[mask]) / len(mask) * 100
print(score,'%')