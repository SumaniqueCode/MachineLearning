import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# determinant of a matrix
det = np.linalg.det(A)
print("Determinant of A:\n", det)

# inverse of a matrix
inv = np.linalg.inv(A)
print("Inverse of A:\n", inv)

# transpose of a matrix
trans = A.T
print("Transpose of A:\n", trans)

# eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues of A:\n", eigenvalues)
print("Eigenvectors of A:\n", eigenvectors)

# Singular Value Decomposition
U, S, V = np.linalg.svd(A)
print("U matrix:\n", U)
print("Singular values:\n", S)
print("V matrix:\n", V)

# Reconstruction of the original matrix from SVD components
sigma = np.zeros((2, 2))
np.fill_diagonal(sigma, S)
reconstructed = U @ sigma @ V
print("Reconstructed matrix from SVD:\n", reconstructed)
