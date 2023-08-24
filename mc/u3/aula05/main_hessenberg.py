from decomposition.hessenberg import Hessenberg
import numpy as np

matrix = [[4, 2, 1],
          [1, 3, 2],
          [0, 1, 5]]


decomposition = Hessenberg(matrix)
decomposition.decompose()

H = decomposition.get_H()
P = decomposition.get_P()

print("Matrix:")
for row in matrix:
    print(row)

print("\nMatrix Hessenberg H:")
for row in H:
    print(row)

print("\nMatrix Unitary P:")
for row in P:
    print(row)

# Retorna True se duas matrizes forem iguais em termos de elemento dentro de uma tolerância.
print(np.allclose(P @ H @ P.conj().T - matrix, np.zeros((3, 3)), atol = 1e-08 , equal_nan = False))