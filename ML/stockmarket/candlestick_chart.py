import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpl
import yfinance as yfin

yfin.pdr_override()
# Set the API parameters
end = dt.datetime.now() # period start date
start = "2020-01-01" # period end date
stocks = ["AAPL"]

# Send the request to the yahoo finance api endpoint
df = pdr.get_data_yahoo("SPY", start, end)

df = df[['Open', 'High', 'Low', 'Close']]

df.reset_index(inplace=True)
df['Date'] = df['Date'].map(mdates.date2num)

print(df.tail())

