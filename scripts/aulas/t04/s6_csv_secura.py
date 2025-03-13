import urllib.request
import ssl
import csv

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

url = 'https://api.ipma.pt/open-data/observation/climate/mpdsi/porto/mpdsi-1312-porto.csv'
filename = 'mpdsi-1312-porto.csv'

with urllib.request.urlopen(url, context=context) as response, open(filename, 'wb') as out_file:
    out_file.write(response.read())

with open('mpdsi-1312-porto.csv','r') as f:
    table = csv.reader(f)
    data = list(table)
print(data)

cabecalho=data[0]
meses = data[1:]

def classifica(n):
    if n>=4: return 'chuva extrema'
    elif n>=3: return 'chuva severa'
    elif n>=2: return 'chuva moderada'
    elif n>=1: return 'chuva fraca'
    elif n>-1: return 'normal'
    elif n>-2: return 'seca fraca'
    elif n>-3: return 'seca moderada'
    elif n>-4: return 'seca severa'
    else : return 'seca extrema'

meses_cs = { mes[0] : [classifica(float(n))\
             for n in mes[1:]] for mes in meses }

print(meses_cs)

def count(xs):
    c = {}
    for x in xs: c[x] = 1 + c.get(x,0)
    return c

def max_count(xs):
    c = count(xs)
    return max(c,key=lambda k : c[k])

xs = ['chuva fraca', 'chuva fraca', 'normal', 'chuva fraca', 'normal']
print(max_count(xs))

meses_c = { mes : max_count(cs) for mes,cs in meses_cs.items() }

print(meses_c)

import dateutil.parser as date

meses_date = { date.parse(mes) : c for mes,c in meses_c.items() }

print(meses_date)

meses_2024 = { mes.month : c for mes,c in meses_date.items() if mes.year == 2024 }

print(meses_2024)

def desclassifica(s):
    if s=='chuva extrema' : return 4
    elif s=='chuva severa' : return 3
    elif s=='chuva moderada' : return 2
    elif s=='chuva fraca': return 1
    elif s=='normal': return 0
    elif s=='seca fraca': return -1
    elif s=='seca moderada' : return -2
    elif s=='seca severa': return -3
    elif s=='seca extrema' : return -4
    else: return None

mais_seco_2024 = min(meses_2024.values(),key=desclassifica)
meses_mais_secos_2024 = { k for k,v in meses_2024.items() if v==mais_seco_2024 }
print (mais_seco_2024,meses_mais_secos_2024)

meses_2024_tbl = [['mes','secura']] + [ [m,s] for m,s in meses_2024.items() ]

print(meses_2024_tbl)

with open('test.csv','w') as f:
    wr = csv.writer(f,delimiter=',')
    wr.writerows(meses_2024_tbl)