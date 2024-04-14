import pandas as pd
import sqlalchemy


engine = sqlalchemy.create_engine("postgresql://postgres:root@localhost:5432/alchemy", echo=False)



# To read a specific table
df = pd.read_sql_table("people", engine)
print(df.head(5))

# To get specific column from that table, use "columns" parameter
df2 = pd.read_sql_table("people", engine, columns=['ssn','firstname','age'])
print(df2.head(5))

# To get sql queries output in pd dataframe
query = '''
SELECT * FROM people a
LEFT JOIN cityinfo b
ON a.firstname=b.name
'''

# query is fetched from db, and execute in engine, result stored in df
df3 = pd.read_sql_query(query, engine)
print(df3.head(5))
# Use 'chunksize=' if the data is huge and this would read the data in batches


# Rename Columns of df to same as sql if needed before sql table insertion
df4 = pd.read_csv("C:\\Users\ZS174XZ\Downloads\RCCP_Feasible_Rolling_production_PVBU_4 Apr.csv")
print(df4.head())

# To rename use :
# df4 = df4.rename(columns={'VC ' : 'vc_code'}), this can also be used if "inplace=true" is not used
df4.rename(columns={'VC ' : 'vc_code'}, inplace=True)
print(df4.head())


# Inserting to DATABASE, index is to be put false,
# and if_exist= fail is by default, so if the table exist use append or replace,
# but replace also drops the tables
# """
# if_exists : {'fail', 'replace', 'append'}, default 'fail'
#     - fail: If table exists, do nothing.
#     - replace: If table exists, drop it, recreate it, and insert data.
#     - append: If table exists, insert data. Create if does not exist.
# """
df4.to_sql(name='dlp_indent', con=engine, index=False, if_exists='append')



# read_sql() : it mergers read_sql_query() and read_sql_table(),
# so you can give query as well as table name, and it would work in both

# pd.read_sql(sq.table_name, engine(session.bind))