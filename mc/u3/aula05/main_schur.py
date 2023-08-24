from decomposition.schur import Schur
import numpy as np

matrix = [[4, 2, 1],
          [1, 3, 2],
          [0, 1, 5]]

decomposition = Schur(matrix)
decomposition.decompose()

T = decomposition.get_T()
P = decomposition.get_P()

print("Matrix:")
for row in matrix:
    print(row)

print("\nMatrix Schur T:")
for row in T:
    print(row)

print("\nMatrix Unitary P:")
for row in P:
    print(row)

# Retorna True se duas matrizes forem iguais em termos de elemento dentro de uma tolerância.
print(np.allclose(P.conj().T @ matrix @ P - T, np.zeros((3, 3)), atol = 1e-08 , equal_nan = False))
