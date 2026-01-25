import time
import numpy as np
import pandas as pd

df = pd.DataFrame(data=np.random.randint(
    1, 11, (100000, 4)), columns=list('ABCD'))

def normal_loop():
    start = time.perf_counter()

    for idx, row in df.iterrows():
        df.at[idx, 'ratio'] = (row['D'] / row['C']) * 100 # new column
    end = time.perf_counter()
    print(end - start)

def vectorization():
    start = time.process_time()

    df["ratio2"] = (df['D'] / df['C']) * 100 # new column

    end = time.process_time()
    print(end - start)
    print(df.head(10))

if __name__ == '__main__':
    normal_loop() # 1.42 seconds
    vectorization() # .00056 seconds
