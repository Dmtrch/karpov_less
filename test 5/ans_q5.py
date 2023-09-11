import pandas as pd
import numpy as np

def limit_gmv(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()
    df['gmv'] = np.clip(df['gmv'], 0, float('inf'))

    calc_gmv = df['price'] * df['stock']

    gmv_is_more = df['gmv'] > calc_gmv
    remainder = (df['gmv'] / df['price']) - np.floor(df['gmv'] / df['price']) > 0

    df['gmv'] = np.where(gmv_is_more, calc_gmv,
                         np.where(remainder, np.floor(df['gmv'] / df['price']) * df['price'], df['gmv']))
    return df
