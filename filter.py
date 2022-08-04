from email import header
import pandas as pd

from openpyxl.workbook import workbook

df_excel = pd.read_excel("regions.xlsx")
df_csv = pd.read_csv("Names.csv", header=None)
df_text = pd.read_csv("data.txt", delimiter = '\t')
#print(df_csv)
df_csv.columns = ["First", "Last", "Address", "City", "State", "Area Code", "Salary"]
df_csv.to_excel("Names_modified.xlsx")