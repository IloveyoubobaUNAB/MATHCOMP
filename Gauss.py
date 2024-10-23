import numpy as np # type: ignore

# Define the matrix of coefficients
A = np.array([[1, 0, 1],
              [3, 4, 3],
              [4, 1, 0]])

# Define the vector of constants
b = np.array([2.5, 11.5, 15])

# Create the augmented matrix
augmented_matrix = np.concatenate((A, b[:, np.newaxis]), axis=1)

# Perform Gaussian elimination
n = len(augmented_matrix)
for i in range(n):
  # Make the diagonal element 1
  pivot = augmented_matrix[i, i]
  augmented_matrix[i, :] = augmented_matrix[i, :] / pivot
  # Eliminate the elements below the diagonal
  for j in range(i + 1, n):
    factor = augmented_matrix[j, i]
    augmented_matrix[j, :] = augmented_matrix[j, :] - factor * augmented_matrix[i, :]

# Perform back substitution
x = np.zeros(n)
for i in range(n - 1, -1, -1):
  x[i] = augmented_matrix[i, n]
  for j in range(i + 1, n):
    x[i] = x[i] - augmented_matrix[i, j] * x[j]

# Print the solution
print("La solución del sistema es:")
print("x1 = ", x[0])
print("x2 = ", x[1])
print("x3 = ", x[2])