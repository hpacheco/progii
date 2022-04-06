import numpy as np

data = np.genfromtxt('../../dados/mpdsi-1312-porto.csv',delimiter=',',skip_header=1)
print(data)
# coluna 4 = médias de índice de secura
medias = data[:,4]
print(medias)
# dias chuvosos têm índice >= 1
chuvosos = medias >= 1
print(chuvosos)
num_dias_chuvosos = (medias[chuvosos]).size
print(num_dias_chuvosos)

dates = np.genfromtxt('../../dados/mpdsi-1312-porto.csv',delimiter=',',dtype='datetime64',usecols=0,skip_header=1)
print(dates)
dias_chuvosos = dates[chuvosos]
print(dias_chuvosos)