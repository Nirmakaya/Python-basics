import pandas as pd



df2 = pd.read_csv("C:\\Users\ZS174XZ\Downloads\RCCP_Feasible_Rolling_production_PVBU_4 Apr.csv")

df3 = pd.read_csv("C:\\Users\ZS174XZ\Downloads\RCCP_Feasible_Rolling_production_PVBU_22 Mar.csv")

print(df2.head())
print(df3.head())


# Here we can use any of the two syntax to merge
# df4 = df3.merge(df2, how='outer')
df4 = pd.merge(df3, df2, how='outer')

print(df2.shape)
print(df3.shape)
print(df4.shape)

df4.drop_duplicates(subset=['VC_CODE'], keep='last', inplace=True)
print(df4.shape)










