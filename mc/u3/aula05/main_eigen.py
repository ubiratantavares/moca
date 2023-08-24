from decomposition.eigen import Eigen

matrix = [[6, 5, 1],
          [0, 3, 5],
          [2, 7, 2]]

decomposition = Eigen(matrix)
decomposition.decompose()

eigenvalues = decomposition.get_eigenvalues()
eigenvectors = decomposition.get_eigenvectors()

print("Matrix:")
for row in matrix:
    print(row)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)