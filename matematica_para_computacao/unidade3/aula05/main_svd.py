from decomposition.svd import SVD
import numpy as np

matrix = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

decomposition = SVD(matrix)
decomposition.decompose()

U = decomposition.get_U()
S = decomposition.get_S()
Vt = decomposition.get_Vt()

print("Matrix A:")
print(matrix)

print("\nMatrix U:")
print(U)

print("\nMatrix S:")
print(np.diag(S))

print("\nMatrix Vt:")
print(Vt)