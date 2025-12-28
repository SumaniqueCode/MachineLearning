import numpy as np

arr = np.arange(1,7)
arr2 = np.arange(7,13)
added_arr = arr + arr2 # Element-wise addition and in the same way subtraction, multiplication, division can be done
print("Element-wise addition:", added_arr)

squared_arr = arr ** 2 # Squaring each element
print("Squared array:", squared_arr)
sum_value = np.sum(arr) # Sum of all elements
print("Sum of elements:", sum_value)
sqrt_arr = np.sqrt(arr) # Square root of each element
print("Square root array:", sqrt_arr)
log_arr = np.log(arr) # Natural logarithm of each element
print("Natural logarithm array:", log_arr)
exp_arr = np.exp(arr) # Exponential of each element
print("Exponential array:", exp_arr)

unique_values = np.unique(arr) # Unique values in the array
print("Unique values:", unique_values)

mean_value = np.mean(arr) # Mean of the array
print("Mean value:", mean_value)
std_dev = np.std(arr) # Standard deviation of the array
print("Standard deviation:", std_dev)
max_value = np.max(arr) # Maximum value in the array
print("Maximum value:", max_value)
min_value = np.min(arr) # Minimum value in the array
print("Minimum value:", min_value)

sorted_arr = np.sort(arr)
print("Sorted array:", sorted_arr)

argmax_index = np.argmax(arr)
print("Index of maximum value in original array:", argmax_index)
argmin_index = np.argmin(arr)
print("Index of minimum value in original array:", argmin_index)
cumsum_arr = np.cumsum(arr) # Cumulative sum of the array
print("Cumulative sum array:", cumsum_arr)
cumprod_arr = np.cumprod(arr) # Cumulative product of the array
print("Cumulative product array:", cumprod_arr)
dot_product = np.dot(arr, arr2) # Dot product of two arrays
print("Dot product of arr and arr2:", dot_product)
cross_product = np.cross(arr[:3], arr2[:3]) # Cross product of first three elements of each array
print("Cross product of first three elements of arr and arr2:", cross_product)

print("Array size (number of elements):", arr.size)  # Total number of elements in the array
print("Array number of dimensions:", arr.ndim)  # Number of dimensions of the array
print("Array item size (in bytes):", arr.itemsize)  # Size of each element in bytes
print("Array total bytes:", arr.nbytes)  # Total bytes consumed by the array
print("Data buffer of the array:", arr.data)  # Data buffer of the array
