import pandas as pd
import numpy as np


'''
install -- openpyxl, xlrd, pandas, numpy, jupyter, jupyter notebook
'''

## Open in Jupyter by 'jupyter notebook' cmd in powershell
## Refer to Official Documentation
## Link = 'https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html'

dict = {
    "name": ['sam', 'rock', 'kia'],
    "city": ['Las', 'Lock', 'Wood']
}

## Comma seperated value (CSV)
## Camel Case : asHere, DataFrame,

df = pd.DataFrame(dict)         # Create a DataFrame using pandas

df.to_csv('first.csv')          # To save as csv file in pd folder

df.to_csv('first_index_removed.csv', index=False)           # To save without index number

df.head(2)
df.tail(1)
df.describe()       ## Gives the mathematical functions
df.median()
df.corr()               ## Statistic Methods : For Statical Analysis


Train = pd.read_csv('Ticket.csv')       ## To make jupyter read a excel placed in pd folder

## Write Train or df to see the Tables in jupyter

Train['Name'][0] # To access a particular cell, column=name, and row=0 index

Train.index = ['first', 'second', 'third'] # To change index type of row


newdf = pd.DataFrame(np.random.rand(344,5), index=np.arange(344))
# arange > arrange

type(newdf)


## Chaining : changing values again and again
newdf2 = newdf
                # This newdf2 will point to newdf and memory will not be created
               # for nedf2 and newdf2 is not an actual Dataframe
                # So newdf2 value change will change newdf value
newdf[0][0] = 900 # This will throw  SettingWithCopyWarning: , because it
                  # will not change the actual newdf and only store in a copy/image
newdf2=newdf.copy()
newdf2[0][0]=9783


## So, best is the use 'loc' or 'iloc' for value change\
newdf.loc[0,0]=654
newdf.loc[0,'C']=200
newdf.iloc[0,4] # for a particular value
newdf.iloc[[0,5],[1,2]]


## Checking null/NaN
newdf['B'].isnull()
newdf['B'].notnull()
newdf['B']= None            # To set value none
newdf.loc[:,'B']=None       # Always best to use loc while chaining



## loc used to look into a specific Dataframe values
newdf.loc[[1,2],['C','D']]
# use colon : for all
newdf.loc[:,['C','D']]
newdf.loc[[1,2],:]
# complex DBMS queries can also be run through jupyter
newdf.loc[(newdf['A']<0.3) & (newdf['C']>0.1)]


## Deletion
newdf.drop('A', axis=1)
newdf.drop(['A', 'D'], axis=1, inplace=True)    # To directly change in main file add inplace=True


## Reset index
newdf.reset_index()
newdf.rest_index(drop=True)                      # to get reset index without reset index column add drop=True
newdf.rest_index(drop=True, inplace=True)

## Basics cmds
newdf.T                      #Transpose
newdf.index
newdf.columns
newdf.dtypes                    #To see the Data type of data


## Sorting
newdf.sort_index(axis=0, ascending=False)       # Bydefault ascending is on, to backward sort
newdf.sort_index(axis=1, ascending=False)       # axis=1 is for column


## Column and row name modification
newdf.columns = list("ABCDE")



## More functions
df.dropna()
#
df.dropna(how='all', axis=1)
#
df.drop_duplicates(subset=['name'], keep=False)                     # To remove all duplicates use keep=false
df.drop_duplicates(subset=['name'], keep='first')              # To remove all except first or last use this keep
df.drop_duplicates(subset=['name'], keep='last')
# To Inspect
df.shape
df.info()


## Count
df['toy'].value_counts(dropna=False)            # To remove NaN count from list use dropna=False


## To read excel and it's different workbook
data = pd.read_excel('Data.xlsx', sheet_name='Sheet1')
# To overide
data.to_excel('Data.xlsx', sheet_name='Sheet1', index=False)
# To overide and keep the other workspace
df2 = df.copy()
df1 = df.copy()
with pd.ExcelWriter('output.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sheet_name_1')
    df2.to_excel(writer, sheet_name='Sheet_name_2')





### Numpy Command

#Numpy uses C++, so it's faster, and we use numpy for it's speed

ser = pd.Series(np.random.rand(34))

type(ser)



