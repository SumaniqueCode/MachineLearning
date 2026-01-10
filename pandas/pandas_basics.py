import pandas as pd

series = pd.Series([1,2,3,4,5], index=['a', 'b', 'c', 'd', 'e'])
print(series)

data = {'Name':['Ram', 'Shayam', 'Hari', 'Sita'], 'Age':[21,22,25,19]}
dataframe = pd.DataFrame(data) #conveting the data into tabulated dataframe
print(dataframe)
