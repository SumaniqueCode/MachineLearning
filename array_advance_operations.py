import numpy as np

arr = np.arange(1, 11)

evens = arr[arr % 2 == 0]  # Extract even numbers
print("Even numbers:", evens)

greater_than_five = arr[arr > 5]  # Extract numbers greater than 5
print("Numbers greater than 5:", greater_than_five)

random_arr = np.random.rand(3,3) # 3x3 array of random floats between 0 and 1
print(random_arr)

random_int_arr = np.random.randint(1, 100, size=(4,4)) # 4x4 array of random integers between 1 and 100
print(random_int_arr)

#Broadcasting example
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vector = np.array([1, 0, 1])
result = matrix + vector  # Broadcasting addition
print("Result of broadcasting addition:\n", result)