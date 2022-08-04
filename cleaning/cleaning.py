import pandas as pd
import numpy as np

from openpyxl.workbook import workbook

df = pd.read_csv("../Names.csv", header=None)

df.columns = ["First", "Last", "Address", "City", "State", "Area Code", "Income"]

df.drop(columns='Address', inplace=True)
df = df.set_index('Area Code')
#print(df)
#print(df.loc[9119])
#print(df.iloc[1])
#print(df.iloc[1,2])
#print(df.loc[8074:,'First'])

df.First = df.First.str.split(expand=True)[0]
#print(df)

df = df.replace(np.nan, "N/A", regex=True)
to_excel = df.to_excel("Cleaning_modified.xlsx")