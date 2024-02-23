import urllib.request
import json

url = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1131200.json'
urllib.request.urlretrieve(url,'1131200.json')

with open('1131200.json','r') as f:
    dict = json.load(f)
    print(dict)

data = dict['data']
print(data)

import dateutil.parser as date

weather = { date.parse(dia['forecastDate']) : dia['idWeatherType'] for dia in data }
print(weather)

import datetime

hoje = datetime.datetime.today()
dia = min(weather,key=lambda d : abs(hoje-d))
print(dia)
previsao = weather[dia]
print(previsao)

url = 'https://api.ipma.pt/open-data/weather-type-classe.json'
urllib.request.urlretrieve(url,'weather-type-classe.json')

with open('weather-type-classe.json','r') as f:
    data = json.load(f)['data']

print(data)

classe = { d['idWeatherType'] : d['descWeatherTypePT'] for d in data }
print(classe)
tempo = classe[previsao]
print(dia,previsao,tempo)

import calendar

def day_month(d):
    return str(d.day)+' '+calendar.month_abbr[d.month]

weather_dif = { day_month(d) : classe[w] for d,w in weather.items() }
print(weather_dif)

with open("test.json","w") as f:
    json.dump(weather_dif,f)

with open("test.json","r") as f:
    weather_dif2 = json.load(f)

print(weather_dif2 == weather_dif)