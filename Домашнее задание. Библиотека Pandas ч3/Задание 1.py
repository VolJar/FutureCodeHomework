import pandas as pd

df = pd.read_csv('Customers.csv', sep=';')
print(df.isna().sum())  # Вывод количества пропустов
df.fillna(valve='???', inplace=True)  # Замена пустышок на ???
