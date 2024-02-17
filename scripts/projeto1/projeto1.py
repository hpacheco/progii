
# Parte 1

# T1

def leParagrafos(ficheiro:str) -> list[str]:
    return None

# T2

def organizaCapitulos(paragrafos:list[str]) -> dict[str,list[str]]:
    return None

# T3

def menorCapitulo(capitulos:dict[str,list[str]]) -> str:
    return None

def maiorDialogo(capitulos:dict[str,list[str]]) -> int:
    return None

def mencoesPersonagens(capitulos:dict[str,list[str]],personagens:set[str]) -> list[tuple[str,float]]:
    return None

def ohJacinto(capitulos:dict[str,list[str]]) -> list[str]:
    return None

# Parte 2

# T4

# the nucleotide complement of a DNA nucleotide in its bonded DNA strand
nucleotidePairs = {'A':'T','G':'C','Y':'R','W':'W','S':'S','K':'M','D':'H','V':'B','X':'X','N':'N'}
for k,v in list(nucleotidePairs.items()): nucleotidePairs[v] = k

def nucleotidePair(c):
    return nucleotidePairs[c]

def leDNA(ficheiro:str) -> tuple[str,str]:
    return None

# T5

def encontraProteinas(code:str,dna:str) -> list[tuple[int,int,str]]:
    return None

def orfFinder(code:str,dna:tuple[str,str]) -> list[tuple[int,int,str,str]]:
    l = len(dna[0])
    res = []
    for i,j,seq in encontraProteinas(code,dna[0]):
        res.append((i,j,seq,"+"))
    for i,j,seq in encontraProteinas(code,dna[1][::-1]):
        res.append((l-i+1, l-j+1, seq,"-"))
    return res

# T6

def intergenicRegions(dna:tuple[str,str],cds:str) -> str:
    return None