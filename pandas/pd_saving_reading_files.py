import pandas as pd

data = {'Name':['Ram', 'Shayam', 'Hari', 'Sita'], 'Age':[21,22,25,19]}
dataframe = pd.DataFrame(data)

dataframe.to_csv('data.csv', index=False) # saving data frame in csv file and index=false for avoiding index in table
df = pd.read_csv('data.csv') #loading data from csv file
print(df)

# Additional pandas save and load functions

# Excel
dataframe.to_excel('data.xlsx')  # saving data frame to excel file
df1 = pd.read_excel('data.xlsx')  # loading data from excel
print(df1)

# JSON
dataframe.to_json('data.json')  # saving data frame to JSON file
df2 = pd.read_json('data.json')  # loading data from JSON file
print(df2)

# SQL (requires connection object, e.g., engine)
# dataframe.to_sql('table_name', con=connection)  # saving data frame to SQL database
# df3 = pd.read_sql('SELECT * FROM table_name', con=connection)  # loading data from SQL database

# HTML
dataframe.to_html('data.html')  # saving data frame to HTML file
df4 = pd.read_html('data.html')  # loading data from HTML tables
print(df4)

# Tab-separated (table)
dataframe.to_csv('data.txt', sep='\t', index=False)  # saving data frame to tab-separated file
df5 = pd.read_table('data.txt', sep='\t')  # loading data from tab-separated file
print(df5)

# Pickle
dataframe.to_pickle('data.pkl')  # saving data frame to pickle file
df6 = pd.read_pickle('data.pkl')  # loading data from pickle file
print(df6)

# Parquet
# dataframe.to_parquet('data.parquet')  # saving data frame to Parquet file
# df6 = pd.read_parquet('data.parquet')  # loading data from Parquet file

# Feather
# dataframe.to_feather('data.feather')  # saving data frame to Feather file
# df7 = pd.read_feather('data.feather')  # loading data from Feather file

# HDF5
# dataframe.to_hdf('data.h5', key='df')  # saving data frame to HDF5 file
# df8 = pd.read_hdf('data.h5', key='df')  # loading data from HDF5 file

# Stata
# dataframe.to_stata('data.dta')  # saving data frame to Stata file
# df9 = pd.read_stata('data.dta')  # loading data from Stata file

# Note: pandas does not have to_sas or to_fwf methods, so only read functions are available for SAS and fixed-width files
# df10 = pd.read_sas('data.sas7bdat')  # loading data from SAS file
# df12 = pd.read_fwf('data.fwf', widths=[10, 20, 30])  # loading data from fixed-width file