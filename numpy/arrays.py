import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print(arr) 
print(arr.dtype)

#indexing and slicing follows simple python list rules
print(arr[1]) # Accessing second element
print(arr[0:4]) # Slicing first four elements
print(arr[-2]) # Accessing second last element

zeros = np.zeros(5)  # Array of 5 zeros
print("Array of zeros:", zeros)

ones = np.ones([3, 4])  # 3x4 Array of ones
print("Array of ones\n", ones)

range_arr = np.arange(1, 10, 2)  # 1 to 9 with step 2
print(range_arr)

linspace_arr = np.linspace(0, 1, 5)  # 5 values from 0 to 1
print(linspace_arr)

arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:\n", arr2d)
print("Element at (1,2):", arr2d[1, 2])  # Accessing element at row 1, column 2
print("First row:", arr2d[0, :])  # Accessing first row
print("Second column:", arr2d[:, 1])  # Accessing second column
print("Array data type:", arr2d.dtype)  # Data type of the array elements
