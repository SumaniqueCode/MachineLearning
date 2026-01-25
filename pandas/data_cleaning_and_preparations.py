import pandas as pd

data = {
    'name': [ 'NewYork', 'Chinatown', 'Kathmandu', 'Toronto', 'Delhi', 'Tokyo', 'Barcelona', 'London', 'Sydney', 'Paris', 'Berlin', 'Dubai', 'Seoul', 'Mumbai', 'Rome'],
    'country': [ 'USA', 'USA', 'Nepal', 'Canada', 'India', 'Japan', 'Spain', 'UK', 'Australia', 'France', 'Germany', 'UAE', 'South Korea', 'India', 'Italy'],
    'continent': [ 'North America', 'North America', 'Asia', 'North America', 'Asia', 'Asia', 'Europe', 'Europe', 'Australia', 'Europe', 'Europe', 'Asia', 'Asia', 'Asia', 'Europe'],
    'population': [ 21728378, 22292010, 25280139, 19297361, 299108371, 13929286, None, 8982000, None, 2140526, None, 3331420, 9720846, None, 2873000],
    'area_sq_km': [ 783.8, 67.1, 50.7, 630.2, None, 2191, 101.9, 1572, 12367.7, None, 891.8, 4114, 605.2, None, 1285],
    'is_capital': [ False, False, True, False, True, True, False, True, True, True, True, False, True, False, True],
    }
df = pd.DataFrame(data)

# # Handling the missig values
# df = df.dropna() # drops row with missing values
# df = df.dropna(axis=1) # drops columns with missing values

# df = df.fillna(method = 'ffill') # forward fill: fills the data similar previos data
# df = df.fillna(method = 'bfill') # backward fill: fills the data similar to next data

# if you want to fill the missing value
# df['population'] = df['population'].fillna(0) #fills the missing value by 0
df['area_sq_km'] = df['area_sq_km'].interpolate() # fills the value based interpolation (fills based on similar data)

print(df)

# data transformation
df = df.rename(columns={'name': 'city_name', 'population': 'pop_total'}) # renaming the columns
# df['column_name'] = pd.to_datetime(df['column_name']) # changing the data type of a column
df['pop_total'] = df['pop_total'].astype('Int64') # changing the data type of a column
df['mul_area_sq_km'] = df['area_sq_km'] * 2 # creating a new column by transforming existing column

#combining and merging data frames
combine_data = pd.concat([df['city_name'], df['country']], axis=1) # combining two data frames side by side
merged_df = pd.merge(df, combine_data, on='city_name', how='left') # merging two data frames based on a common column
left_joined_df = pd.merge(df, combine_data, on='city_name', how='left') # left join
right_joined_df = pd.merge(df, combine_data, on='city_name', how='right') # right join
inner_joined_df = pd.merge(df, combine_data, on='city_name', how='inner') # inner join
outer_joined_df = pd.merge(df, combine_data, on='city_name', how='outer') # outer join

joined_df = df.join(combine_data, how='left') # joining two data frames based on index