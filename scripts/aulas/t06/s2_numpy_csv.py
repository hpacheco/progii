import urllib.request
import numpy as np
import ssl

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

url = 'https://api.ipma.pt/open-data/observation/climate/mpdsi/porto/mpdsi-1312-porto.csv'
filename = 'mpdsi-1312-porto.csv'

with urllib.request.urlopen(url, context=context) as response, open(filename, 'wb') as out_file:
    out_file.write(response.read())

data = np.genfromtxt('mpdsi-1312-porto.csv',delimiter=',',skip_header=1)
print(data)
# coluna 4 = médias de índice de secura
medias = data[:,4]
print(medias)
# dias chuvosos têm índice >= 1
chuvosos = medias >= 1
print(chuvosos)
num_dias_chuvosos = (medias[chuvosos]).size
print(num_dias_chuvosos)

dates = np.genfromtxt('mpdsi-1312-porto.csv',delimiter=',',dtype='datetime64',usecols=0,skip_header=1)
print(dates)
dias_chuvosos = dates[chuvosos]
print(dias_chuvosos)