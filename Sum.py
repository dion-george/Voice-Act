import pandas as pd
import numpy as np
df = pd.read_excel("1.xlsx")


df["values"].sum(), df["values"].mean(),df["values"].min(),df["values"].max()
df.head()
print(df["values"].sum())
print(df["values"].mean())
print(df["values"].min())
print(df["values"].max())

#Trying to print data to cell directly--------------NOT WORKING :(
df['A16'] = df["values"].sum()

