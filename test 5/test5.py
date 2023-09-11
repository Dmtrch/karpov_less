import sys

import pandas as pd
import numpy as np

def limit_gmv(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()
    df['gmv'] = np.clip(df['gmv'], 0, float('inf'))

    calc_gmv = df['price'] * df['stock']

    gmv_is_more = df['gmv'] > calc_gmv
    remainder = (df['gmv'] / df['price']) - np.floor(df['gmv'] / df['price']) > 0

    calc_gmv = np.floor(df['gmv'] / df['price']) * df['price']
    df['gmv'] = np.where(gmv_is_more, calc_gmv,
                         np.where(remainder, calc_gmv , df['gmv']))

    return df

def read_dataframe(file_name_in) -> pd.DataFrame:
    df = pd.read_table(file_name_in, sep='|', header=0, skiprows=[1], engine='python')

    # удаление пустых столбцов
    df = df.dropna(axis=1, how='all')
    #  удаление пустых строк
    df = df.dropna(axis=0, how='all')
    # удаление пробелов до и после названия столбца
    df.rename(columns=lambda x: x.strip(), inplace=True)
    # Сброс индекса
    df.reset_index(drop=True, inplace=True)

    return df


df = read_dataframe('data.txt')
print(df)

df = limit_gmv(df)
print(df)

