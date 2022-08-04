import pandas as pd

from openpyxl.workbook import workbook

df = pd.read_csv("../Names.csv", header=None)

df.columns = ["First", "Last", "Address", "City", "State", "Area Code", "Salary"]

#print(df.columns)
#print(df["Last"])
#print(df[["State","Area Code"]])
#print(df["First"][0:3])
print(df.iloc[2,3])

required_dataset = df[['First', "Last", "Salary"]]
stored = required_dataset.to_excel('Salary.xlsx')

required_dataset = df[['First', "Last", "State"]]
stored = required_dataset.to_excel('State_Location.xlsx', index=None)