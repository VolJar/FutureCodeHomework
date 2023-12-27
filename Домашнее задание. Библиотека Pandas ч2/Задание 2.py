import pandas as pd

tbl = pd.read_csv("Customers.csv", sep=";")
print(tbl[(tbl['Age'] > 30) & (tbl['Income'] < 30000)], end='\n\n')
print(tbl[(tbl['Profession'] == "Lawyer") & (tbl['Work Experience'] > 5)])
