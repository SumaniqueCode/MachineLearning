import pandas as pd

# URL of the Iris dataset (no column headers in the raw data)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# Column names for the dataset
columns = ["sepal length", "sepal width", "petal length", "petal width", "species"]

# Read the CSV file and assign column names
df = pd.read_csv(url, header=None, names=columns)

print(df.head(10)) # Print the first 10 rows of the dataset (default is 5 if no number is given)
print(df.tail(3)) # Print the last 3 rows of the dataset (default is 5 if no number is given)

print(df.info()) # Display concise information about the DataFrame (columns, data types, memory usage)
print(df.describe()) # Generate descriptive statistics (mean, min, max, std, etc.) for numerical columns

print(df[['species', 'petal length']]) # Select and display only the 'species' and 'petal length' columns
print(df[df['sepal length'] > 2]) # Filter and display rows where sepal length is greater than 2

print(df.iloc[0]) # Select and print the first row using integer-based indexing
print(df.iloc[:, 3]) # Select and print all rows from the 4th column (petal width) using integer-based indexing
print(df.loc[0]) # Select and print the first row using label-based indexing
print(df.loc[:, "species"]) # Select and print all rows from the 'species' column using label-based indexing

filtered_data = df[(df['sepal length']>4) & (df['species']=='Iris-setosa') ] # multiple filter
print(filtered_data)
