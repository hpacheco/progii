
# Parte 1

# T1

def leTexto(ficheiro):
    return None

# T2

def constroiIndice():
    reliquia = leTexto('dados/areliquia.txt')
    return ""

# T3

def normalizaPalavra(palavra):
    pre = ""
    core = ""
    pos = ""
    l = 0
    for c in palavra:
        if not c.isalnum():
            l=l+1
            pre=pre+c
        else: break
    core=palavra[l:]
    i=len(core)-1
    while i >= 0 and not core[i].isalnum():
        pos = core[i]+pos
        i=i-1
    core=core[0:i+1]
    return core.lower()

def totais():
    reliquia = leTexto('dados/areliquia.txt')
    return (0,0,0)

def maisFrequente():
    reliquia = leTexto('dados/areliquia.txt')
    return ("",0)

def camisinhaMary():
    reliquia = leTexto('dados/areliquia.txt')
    return 0

def menorCapitulo():
    reliquia = leTexto('dados/areliquia.txt')
    return ""

# Parte 2

# the nucleotide complement of a DNA nucleotide in its bonded DNA strand
nucleotidePairs = {'A':'T','G':'C','Y':'R','W':'W','S':'S','K':'M','D':'H','V':'B','X':'X','N':'N'}
for k,v in list(nucleotidePairs.items()): nucleotidePairs[v] = k

def nucleotidePair(c):
    return nucleotidePairs[c]

# all possible base instantiations for each nucleotide
nucleotideBases = {'A':'A','T':'T','C':'C','G':'G','Y':'CT','R':'AG','W':'AT','S':'GC','K':'TG','M':'CA','D':'AGT','V':'ACG','H':'ACT','B':'CGT','X':'ATGC','N':'ATGC'}

# T4

def leDNA(fasta):
    texto = leTexto(fasta)
    return None

# T5

def leEnzimas(staden):
    texto = leTexto(staden)
    return None

# T6

def oneCutters(enzimas,dna):
    return None