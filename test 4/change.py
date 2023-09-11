import pandas as pd
import numpy as np

# Создание DataFrame
data = {'A': ['foo', 'bar', 'baz', 'foo'],
        'B': ['bar', 'baz', 'foo', 'bar']}

df = pd.DataFrame(data)

# Установка значения NaN в столбце 'A' для ячеек со значением 'foo'
df.loc[df['A'] == 'foo', 'A'] = np.nan

print(df)
