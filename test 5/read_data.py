import pandas as pd

# Замените 'путь_к_файлу' на фактический путь к вашему файлу
file_path = 'data.txt'

# Чтение файла и создание DataFrame
df = pd.read_table(file_path, sep='|', header=0, skiprows=[1], engine='python')

# Удаление лишних столбцов
df = df.dropna(axis=1, how='all')

# Удаление лишних строк
df = df.dropna(axis=0, how='all')

# # Переименование столбцов
# new_columns = ['sku', 'gmv', 'price', 'stock']
# df.columns = new_columns

# Сброс индекса
df.reset_index(drop=True, inplace=True)

# Вывод DataFrame
print(df)