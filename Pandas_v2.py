import pandas as pd
import numpy as np


df = pd.DataFrame({
    "name": ["Sam","matthew","leon","po", "Sam"],
    "age": [20,21,23,9, 8],
    "town" : ["Goa","Delhi","Pune","Gujrat","PMO"]
    })



df2 = pd.read_csv("C:\\Users\ZS174XZ\Downloads\RCCP_Feasible_Rolling_production_PVBU_4 Apr.csv")

print(df2.head(15))

df3 = pd.read_csv("C:\\Users\ZS174XZ\Downloads\RCCP_Feasible_Rolling_production_PVBU_22 Mar.csv")

print(df3.head())

df4 = pd.read_sql()




