
from textblob import Word
import pyphen
import json

with open('dados/animals.json') as f:
    # uma lista de nomes de animais
    animals = json.load(f)

def singularize(w):
    """converte uma palavra em Inglês no plural na sua forma no singular"""
    return Word(w).singularize()

lang = pyphen.Pyphen(lang='en')
def syllables(word:str) -> list[str]:
    """parte uma palavra em Inglês em sílabas"""
    return lang.inserted(word).split("-")

## Parte I

### T1

def leParagrafos(ficheiro:str) -> list[str]:
    return None

### T2

# o tipo para um índice de animais
indice = list[tuple[dict[str,str],list[str]]]

def constroiIndiceAnimais(paragrafos:list[str]) -> indice:
    return None

### T3

def menorCapitulo(ind:indice) -> int:
    return None

def maiorMonologo(ind:indice) -> tuple[int,str]:
    return None

def outrasMencoes(ind:indice) -> dict[str,int]:
    return None

def fleschKincaid(ind:indice) -> float:
    return None

## Parte II

### T4

def leProteina(fasta:str) -> tuple[str,str]:
    return None

### T5

def findMotifs(dna:tuple[str,str]) -> str:
    return None

### T6

def overlappingMotifs(fasta:str) -> str:
    return None

def mostFrequentSites(fasta:str) -> dict[str,list[int]]:
    return None