import pandas as pd

#grouping by categorical columns
# data for sales by products
data = {
    'Category': ['Electronics', 'Electronics', 'Furniture', 'Furniture', 'Clothing', 'Clothing', 'Clothing', 'Electronics'],
    'Product': ['Laptop', 'Smartphone', 'Table', 'Chair', 'Shirt', 'Jeans', 'Jacket', 'Tablet'],
    'Sales': [1000, 1500, 700, 300, 200, 400, 600, 1200],
    'Age': [25, 30, 45, 50, 22, 28, 35, 40]
}
df = pd.DataFrame(data)
grouped = df.groupby('Category').sum()
print("Grouped by Category:\n", grouped)

# aggregating with multiple functions
stats = df.groupby('Category').agg({"Sales":['mean', 'max', 'min', 'sum', 'count']})
print("\nAggregated statistics:\n", stats)

# pivot table creation
pivot_table = pd.pivot_table(df, values='Sales', index='Category', columns='Product', aggfunc='sum', fill_value=0)
print("\nPivot Table:\n", pivot_table)

# custom aggregation function
def range_func(x):
    return x.max() - x.min()

custom_agg = df.groupby('Category').agg({'Sales': range_func})
print("\nCustom Aggregation (Range of Sales):\n", custom_agg)
