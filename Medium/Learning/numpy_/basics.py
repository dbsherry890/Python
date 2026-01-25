import numpy as np
import pandas as pd

v = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

v = v.reshape(2, 5)
print(v)

index = pd.date_range('2-2-2025', periods=10, freq='B')
print(index)

raw = pd.read_csv("http://hilpisch.com/pyalgo_eikon_eod_data.csv",
                  index_col=0, parse_dates=True).dropna()
# print(raw.head())
# print(raw.columns)
raw.rename(columns={"AAPL.O": "AAPL"}, inplace=True)
df = pd.DataFrame(raw["AAPL"])
# print(df)

df = pd.DataFrame({'A': [10, 20, 30, 40, 50]})
df['shifted_A'] = df['A'].shift(1)
print(df)
