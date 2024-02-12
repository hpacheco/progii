import fastf1
import fastf1.plotting
import os
import numpy as np
import pandas as pd
import math
import plotly.express as px

# usar a cache acelera o processo de correr os testes repetidamente
# no replit, se ficar sem espaço disponível, deve desativar este feature
if not os.path.exists("cache"): os.mkdir("cache")
fastf1.Cache.enable_cache('cache')  # replace with your cache directory

# for a given year, returns a list of events
def getSchedule(year):
    schedule = pd.DataFrame(fastf1.events._get_schedule_ff1(year))
    schedule.dropna(inplace=True)
    return list(schedule['EventName'])

# for a given event in a given year, returns qualifying times per team, per driver and per qualifying session
def getQualifyingLapTimes(year,eventName):
    session = fastf1.get_session(year, eventName, 'Q')
    session.load()
    laps = session.results[['TeamName','Abbreviation','Q1','Q2','Q3']].copy()
    def groupDriver(df):
        df = pd.DataFrame(df)
        df.dropna(axis=1,inplace=True)
        del df['TeamName']
        del df['Abbreviation']
        return { k : v[0] for k,v in df.to_dict(orient='list').items() }
    def groupTeam(df):
        return df.groupby('Abbreviation').apply(groupDriver).to_dict()
    return laps.groupby('TeamName').apply(groupTeam).to_dict()

# for a given event in a given year, returns fastest qualifying lap telemetry information per driver
def getQualifyingFastestLaps(year,eventName):
    session = fastf1.get_session(year, eventName, 'Q')
    session.load()
    drivers = pd.unique(session.laps['Driver'])
    fastest_laps = {}
    for driver in drivers:
        lap = session.laps.pick_driver(driver).pick_fastest()
        team = lap['Team']
        color = fastf1.plotting.team_color(team)
        tel = lap.get_telemetry()
        tel['Seconds'] = tel['Time'] / np.timedelta64(1,'s')
        #tel.set_index('Seconds',inplace=True)
        tabr = None
        for short,long in fastf1.plotting.TEAM_TRANSLATE.items():
            if long in team.lower(): tabr = short; break;
        fastest_laps[driver] = { 'TeamName' : team, 'TeamAbbreviation':tabr, 'TeamColor' : color, 'Telemetry' : tel }
    return fastest_laps

def teamDuels(year):

    return None

def drawFastestLaps(year,eventName):
    laps = getQualifyingFastestLaps(year,eventName)
    df = None # construir dataframe a partir das
    fig = px.bar(df, orientation='h')  # acrescentar outros parâmetros para configurar o gráfico
    fig.write_html("quali.html")



