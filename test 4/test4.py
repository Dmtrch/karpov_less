import pandas as pd
import numpy as np




def fillna_with_mean(df: pd.DataFrame, target: str, group: str) -> pd.DataFrame:
    df = df.copy()
    df[target] = pd.to_numeric(df[target], errors='coerce')
    group_means = df.groupby(group)[target].transform('mean')
    df[target] = df[target].fillna(np.floor(group_means))
    return df
def read_dataframe(file_name_in) -> pd.DataFrame:
    with open(file_name_in, 'r') as file:
        lines = file.readlines()

    data = []
    for line in lines:
        items = line.strip().split()
        data.append(items)

    data[0].insert(0, "ID")
    # Создание DataFrame
    columns = data[0]
    data.pop(0)

    df = pd.DataFrame(data, columns=columns)
    df = df.drop(columns[0],axis=1)

    name_sales = columns[4]

    df.loc[df[name_sales] == "NaN", name_sales] = np.nan


    return df

df = read_dataframe("in_data.txt")

print(df)

df_f = fillna_with_mean(df, "sales", "category")

print(df_f)