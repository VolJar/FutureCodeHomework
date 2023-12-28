import pandas as pd

df = pd.read_csv('Customers.csv', sep=';')
df.dropna(axis=0, inplace=True)
print(df.groupby('Profession')['Income'].mean())
