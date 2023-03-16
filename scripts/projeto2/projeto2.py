import math
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# T1

with open('dados/mammals.json', 'r') as f:
    mammals = json.load(f)

def totalEspecies():
    return 0

def parenteMaisProximo(especie1,especie2):
    return ""

def desenhaGatos():
    with open('gatos.dot','w') as f:
        # acrescentar código que adapta a escrita para o ficheiro
        f.write("""graph G {
  layout=twopi
  ranksep=4;
  ratio=auto;
  
  n1 [root=True,label="label1",shape=plaintext]
  n1 -- { n2 n3 n4 }

}""")

# T2

# lê um ficheiro no formato FASTA para um array numpy de caracteres
def readFasta(file):
    with open(file,'r',encoding='utf-8') as f:
        ls = np.concatenate([np.array(list(s)) for s in f.read().splitlines()[1:]])
    return ls

def dotPlot(window,float,file1,file2):
    dna1 = readFasta(file1)
    dna2 = readFasta(file2)
    matriz = np.zeros((len(dna1), len(dna2)))
    # acrescentar código que preenche valores da matriz
    plt.imshow(matriz, cmap='binary');
    plt.savefig('dotplot.png')

# T3

sars_ani_data = pd.read_csv('dados/sars_ani_data.csv')

def casosCaes():
    return None

def eventosFelideos():
    return None

def maisHumanos():
    return None

def mediaQuintas():
    return None

# T4

# T5

def hubPorto():
    return None

def temCaminhoDireto(estacao1,estacao2):
    return None

def caminhoMaisRapido(estacao1,estacao2):
    return None