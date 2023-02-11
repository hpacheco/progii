import json
import geopy.distance
import numpy as np
import pandas as pd

# Tarefa 1

with open('dados/nuclear_power_plants.json','r') as f:
    dados_str = f.read()
dados = json.loads(dados_str)

def paisMaisNuclear(centrais):
    return ""

def reatorMaisRecente(centrais):
    return ""

def paisTresMaioresCentrais(centrais):
    return ""

def geodist(coords_1,coords_2):
    """distance in km between two (latitude,longitude) coordinates"""
    return geopy.distance.distance(coords_1,coords_2).km

def centraisParis(centrais):
    return 0

# Tarefa 2

def formataCentral(central):
    return None

def formataCentralEstilo(central):
    return None

def formataCentrais(f,centrais):
    return None

geodados = formataCentrais(formataCentral,dados)
with open('centrais.geojson', 'w') as f:
  json.dump(geodados,f)

geodados2 = formataCentrais(formataCentralEstilo,dados)
with open('centrais2.geojson', 'w') as f:
  json.dump(geodados2,f)

# Tarefa 3

dados3 = np.genfromtxt('dados/nuclear_country_year.csv',delimiter=',',filling_values=0)
paises3 = np.genfromtxt('dados/nuclear_country_year.csv',delimiter=',',dtype=object,usecols=[0]).astype('str')

def trintaPorCento(arr):
    return 0

def anoMaisNuclear(arr):
    return 0

def nuclearDecadas(arr):
    return []

def naoMaisNuclear(arr,names):
    return []

# Tarefa 4

dados4 = pd.read_csv('dados/owid-energy-data.csv')

def maisRenovaveis2020(data):
    return ("",0)

def energiaPortugal2020(data):
    return []

def maisDependentesCarvao(data):
    return {}

eu_countries = {
    'AT': 'Austria',
    'BE': 'Belgium',
    'BG': 'Bulgaria',
    'HR': 'Croatia',
    'CY': 'Cyprus',
    'CZ': 'Czech Republic',
    'DK': 'Denmark',
    'EE': 'Estonia',
    'FI': 'Finland',
    'FR': 'France',
    'DE': 'Germany',
    'GR': 'Greece',
    'HU': 'Hungary',
    'IE': 'Ireland',
    'IT': 'Italy',
    'LV': 'Latvia',
    'LT': 'Lithuania',
    'LU': 'Luxembourg',
    'MT': 'Malta',
    'NL': 'Netherlands',
    'PL': 'Poland',
    'PT': 'Portugal',
    'RO': 'Romania',
    'SK': 'Slovakia',
    'SI': 'Slovenia',
    'ES': 'Spain',
    'SE': 'Sweden',
    'GB': 'United Kingdom'
  }

def gasEU(data):
    return {}

dados5 = pd.read_excel('dados/pordata_energy_import.xlsx',sheet_name='Table')

def anoMaisRenovavelEU(data1,data2):
    return {}


