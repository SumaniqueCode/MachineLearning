import numpy as np

arr = np.arange(1, 7)

reshaped_arr = arr.reshape((3, 2)) # Reshaping to 3 rows and 2 columns
print("Reshaped array:\n", reshaped_arr)

expanded_arr = arr[:, np.newaxis] # Adding a new axis
print("Expanded array with new axis:\n", expanded_arr)

transposed_arr = arr.T # Transposing the array
print("Transposed array:\n", transposed_arr)

flattened_arr = transposed_arr.flatten() # Flattening the array
print("Flattened array:", flattened_arr)
print("Array shape:", reshaped_arr.shape)  # Shape of the reshaped array
