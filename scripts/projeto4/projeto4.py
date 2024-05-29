import pandas as pd
import plotly.express as px

# T1

def dueloEquipas(pais1,pais2) -> tuple[str,list[str]]:
    return None

# T2

def desenhaGrupos():
    df : pd.DataFrame = None # construa um dataframe com as propriedades necessárias à visualização (ver o enunciado)
    fig = px.sunburst(df, path=['group','team']) # acrescente outras configurações do gráfico (ver a documentação)
    fig.show()