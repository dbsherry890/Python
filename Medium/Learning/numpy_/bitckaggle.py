from momentum import MomVectorBacktester as Mom
# import kagglehub
import numpy as np
import pandas as pd
# Download latest version
# path = kagglehub.dataset_download("prasoonkottarathil/btcinusd")

# print("Path to dataset files:", path)

df = pd.read_csv(
    "/Users/ds/.cache/kagglehub/datasets/prasoonkottarathil/btcinusd/versions/4/BTC-2020min.csv")
# print(df.columns)
df = df[["high", "low", "open", "close"]]
df["returns"] = np.log(df["close"] / df["close"].shift(1))
to_plot = df["returns"]

for m in [1, 3, 5, 7]:
    pass

print(df.head())
