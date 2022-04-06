import json

with open('../../dados/1131200.json','r') as f:
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

with open('../../dados/weather-type-classe.json','r') as f:
    data = json.load(f)['data']

print(data)
#
# classe = { d['idWeatherType'] : d['descIdWeatherTypePT'] for d in data }
# print(classe)
# tempo = classe[previsao]
# print(tempo)
#
# import calendar
#
# def day_month(d):
#     return str(d.day)+' '+calendar.month_abbr[d.month]
#
# weather_dif = { day_month(d) : classe[w] for d,w in weather.items() }
# print(weather_dif)
#
# with open("test.json","w") as f:
#     json.dump(weather_dif,f)
#
# with open("test.json","r") as f:
#     weather_dif2 = json.load(f)
# print(weather_dif2 == weather_dif)