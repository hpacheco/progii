import json
import pandas as pd
import numpy as np
from numpy import asarray
from PIL import Image # python package Pillow

# T1

with open('dados/prize.json','r') as f:
    prizes = json.load(f)["prizes"]

with open('dados/laureate.json','r') as f:
    laureates = json.load(f)["laureates"]

def maisPartilhados() -> tuple[int,set[tuple[int,str]]]:
    return None

def multiLaureados() -> dict[str,set[str]]:
    return None

def anosSemPremio() -> tuple[int,int] :
    return None

def rankingDecadas() -> dict[str,tuple[str,int]]:
    return None

# T2

def toGrayscale(rgb:np.ndarray) -> np.ndarray:
    return None

def converteGrayscale(fromimg:str,toimg:str) -> None:
    # a 3D numpy array of type uint8
    rgb: np.ndarray = asarray(Image.open(fromimg))
    # a 2D numpy array of type uint8
    grayscale: np.ndarray = toGrayscale(rgb)
    Image.fromarray(grayscale, mode="L").save(toimg)

def toBW(gray:np.ndarray,threshold:tuple[int,int]) -> np.ndarray:
    return None

def converteBW(fromimg:str,toimg:str,threshold:tuple[int,int]) -> None:
    # a 2D numpy array of type uint8
    grayscale : np.ndarray = asarray(Image.open(fromimg))
    # a 2D numpy array of type uint8 (but with values being only 0 or 255)
    bw : np.ndarray = toBW(grayscale,threshold)
    Image.fromarray(bw,mode="L").save(toimg)

def autoThreshold(fromimg:str,tolerance:int) -> tuple[int,int]:
    grayscale: np.ndarray = asarray(Image.open(fromimg))
    return None

def toContour(bw:np.ndarray) -> np.ndarray:
    return None

def converteContour(fromimg:str,toimg:str) -> None:
    # a 2D numpy array of type uint8 (but with values being only 0 or 255)
    bw : np.ndarray = asarray(Image.open(fromimg).convert("L"))
    # a 2D numpy array of type uint8 (but with values being only 0 or 255)
    contour : np.ndarray = toContour(bw)
    Image.fromarray(contour,mode="L").save(toimg)

# T3

legislativas = pd.read_excel("dados/legislativas.xlsx",header=[0,1],sheet_name="Quadro")

def eleitoresPorto() -> int:
    return None

def taxaAbstencao() -> list[tuple[int,float]]:
    return None

def perdaGrandesMunicipios() -> dict[str,int]:
    return None

def demografiaMunicipios() -> dict[str,tuple[str,str]]:
    return None

# T4

nominations = pd.read_csv("dados/nominations.csv")

def maisNomeado() -> tuple[str,int]:
    return None

def nomeacoesCruzadas() -> tuple[int,set[str]]:
    return None

def caminhoEinsteinFeynman() -> list[str]:
    return None