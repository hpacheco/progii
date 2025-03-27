import urllib.request
import pandas as pd
import numpy as np
from prophet import Prophet
import ssl

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

url = 'https://api.ipma.pt/open-data/observation/climate/monthly-long-series/PT100-tx-tn-prec.xlsx'
filename ='PT100-tx-tn-prec.xlsx'

with urllib.request.urlopen(url, context=context) as response, open(filename, 'wb') as out_file:
    out_file.write(response.read())

years = pd.read_excel('PT100-tx-tn-prec.xlsx',sheet_name=1,usecols=["year"],dtype="str").to_numpy()[:-1,0]
years = np.vectorize(lambda x:np.datetime64(x,'Y'))(years)
print(years)

temps = pd.read_excel('PT100-tx-tn-prec.xlsx',sheet_name=1,usecols=["Annual"]).to_numpy()[:-1,0]
print(temps)

df_for_prophet = pd.DataFrame({"ds":years,"y":temps})
model = Prophet()
model.fit(df_for_prophet)

forecast_df = model.make_future_dataframe(periods=10,freq='Y')
forecast = model.predict(forecast_df)
print(forecast)