
import json
import numpy as np
from haversine import haversine, Unit

## T1

with open("dados/nextclade_sars-cov-2.json") as f:
    # a árvore filogenética do vírus Sars-Cov-2
    cov2 = json.load(f)["tree"]

def mostRecentStrains(tree) -> dict[str,int]:
    return None

def numberDescendantsOf(whoname:str,tree) -> int:
    return None

def longestEvolutionaryBranches(tree):
    return None

def mostCommonMutation(tree) -> tuple[str,int]:
    return None

## T2

def readMSA(file) -> dict[str,np.ndarray[np.char]]:
    """lê um ficheiro com alinhamentos no formato FASTA para um dicionário de sequências numpy de caracteres"""
    with (open(file,'r',encoding='utf-8') as f):
        ls = f.read().splitlines()
        d = {}
        n = None
        for l in ls:
            if l.startswith(">"):
                n = l[1:]
            else:
                if n in d: d[n] = np.concatenate([d[n],np.array(list(l))])
                else: d[n] = np.array(list(l))
    return d

def createBLOSUM(msa:dict[str,np.ndarray[np.char]]) -> np.ndarray[np.int8]:
    return None

def mostSimilarSequences(blosum: np.ndarray[np.int8]) -> tuple[str,str]:
    return None

## T3

# EuroVoc EU regions
regioesEuroVoc = {
    'Central and Eastern Europe':
        [ 'Albania', 'Armenia', 'Azerbaijan', 'Belarus', 'Bosnia and Herzegovina', 'Bulgaria', 'Czech Republic', 'Croatia', 'Georgia', 'Hungary', 'Moldova', 'Montenegro', 'North Macedonia', 'Poland', 'Romania', 'Russia', 'Serbia', 'Slovakia', 'Slovenia', 'Ukraine'],
    'Northern Europe':
        ['Denmark','Estonia','Finland','Iceland','Latvia','Lithuania','Norway','Sweden'],
    'Southern Europe':
        [ 'Cyprus', 'Greece', 'Holy See', 'Italy', 'Malta', 'Portugal', 'San Marino', 'Spain', 'Turkey'],
    'Western Europe':
        ['Andorra','Austria','Belgium','France','Germany','Ireland','Liechtenstein','Luxembourg','Monaco','Netherlands','Switzerland','United Kingdom']
    }

def piorAnoUE() -> int:
    return None

def paisMaisAgravado() -> str:
    return None

def registoAnual() -> dict[int,str]:
    return None

## T4

def habitatsMorcegos() -> int:
    return None

def corredorVidaSelvagem() -> list[str]:
    return None