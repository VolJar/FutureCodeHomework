import pandas as pd

df = pd.read_csv('Customers.csv', sep=';')
df.dropna(inplace=True)
print(df.groupby('Profession')['Income'].mean())
