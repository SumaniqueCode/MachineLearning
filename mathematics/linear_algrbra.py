import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
# Matrix addition
add = A + B
print("Matrix addition:\n", add)
# Matrix Subtraction
sub = B - A
print("Matrix subtraction:\n", sub)

# Matrix Multiplication
mul = np.dot(A, B)
print("Matrix multiplication:\n", mul)

# Scalar Multiplication
scalar_mul = 2 * A
print("Scalar multiplication:\n", scalar_mul)

# identity Matrix
identity = np.eye(2)
print("Identity Matrix:\n", identity)

# zero Matrix
zero = np.zeros((2, 3))
print("Zero Matrix:\n", zero)

# diagonal Matrix
diagonal = np.diag([1, 2])
print("Diagonal Matrix:\n", diagonal)

# matrix vector multiplication
M = np.array([[1, 2], [3, 4], [5, 6]])
v = np.array([1, 2])
mv_mul = np.dot(M, v)
print("Matrix-vector multiplication:\n", mv_mul)

# block diagonal matrix
block_diag = np.block([[A, np.zeros((2, 2))], [np.zeros((2, 2)), B]])
print("Block diagonal matrix:\n", block_diag)
